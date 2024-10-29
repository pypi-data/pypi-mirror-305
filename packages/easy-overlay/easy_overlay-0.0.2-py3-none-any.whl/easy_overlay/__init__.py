import win32gui
import win32con
import win32api
from ctypes import windll, Structure, byref, create_string_buffer
from ctypes.wintypes import DWORD, LONG, BYTE, WCHAR, UINT, HANDLE
import threading
import time

class LOGFONT(Structure):
    _fields_ = [
        ('lfHeight', LONG),
        ('lfWidth', LONG),
        ('lfEscapement', LONG),
        ('lfOrientation', LONG),
        ('lfWeight', LONG),
        ('lfItalic', BYTE),
        ('lfUnderline', BYTE),
        ('lfStrikeOut', BYTE),
        ('lfCharSet', BYTE),
        ('lfOutPrecision', BYTE),
        ('lfClipPrecision', BYTE),
        ('lfQuality', BYTE),
        ('lfPitchAndFamily', BYTE),
        ('lfFaceName', WCHAR * 32)
    ]

class Overlay:
    def __init__(self):
        self._running = False
        self._hwnd = None
        self._thread = None
        self._dc = None
        self._width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        self._height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        self._draw_queue = []
        self._lock = threading.Lock()

    def _create_window(self):
        wc = win32gui.WNDCLASS()
        wc.lpszClassName = "PyOverlayClass"
        wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wc.hbrBackground = win32con.COLOR_WINDOW
        wc.lpfnWndProc = self._wnd_proc

        win32gui.RegisterClass(wc)

        style = win32con.WS_POPUP | win32con.WS_VISIBLE
        style_ex = (win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT | 
                   win32con.WS_EX_TOPMOST)

        self._hwnd = win32gui.CreateWindowEx(
            style_ex,
            wc.lpszClassName,
            "PyOverlay",
            style,
            0, 0,
            self._width, self._height,
            0, 0,
            0, None
        )

        # Make the window transparent and click-through
        win32gui.SetLayeredWindowAttributes(
            self._hwnd,
            win32api.RGB(0, 0, 0),
            0,
            win32con.LWA_COLORKEY
        )

        win32gui.ShowWindow(self._hwnd, win32con.SW_SHOW)
        self._dc = win32gui.GetDC(self._hwnd)

    def _wnd_proc(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
            return 0
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    def start(self):
        if self._running:
            return
        
        self._running = True
        self._thread = threading.Thread(target=self._window_loop)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()
            win32gui.ReleaseDC(self._hwnd, self._dc)
            win32gui.DestroyWindow(self._hwnd)

    def _window_loop(self):
        self._create_window()
        
        while self._running:
            try:
                # Process Windows messages
                msg = win32gui.PeekMessage(None, 0, 0, 0)
                if msg[0]:
                    win32gui.TranslateMessage(msg[1])
                    win32gui.DispatchMessage(msg[1])

                # Process draw queue
                with self._lock:
                    for draw_func in self._draw_queue:
                        try:
                            draw_func(self._dc)
                        except Exception as e:
                            print(f"Draw error: {e}")
                    self._draw_queue.clear()

            except Exception as e:
                pass

            time.sleep(0.001)

    def draw_line(self, start_pos, end_pos, color=(255, 0, 0), thickness=2):
        def _draw(dc):
            pen = win32gui.CreatePen(win32con.PS_SOLID, thickness, 
                                   win32api.RGB(*color))
            old_pen = win32gui.SelectObject(dc, pen)
            
            win32gui.MoveToEx(dc, int(start_pos[0]), int(start_pos[1]))
            win32gui.LineTo(dc, int(end_pos[0]), int(end_pos[1]))
            
            win32gui.SelectObject(dc, old_pen)
            win32gui.DeleteObject(pen)

        with self._lock:
            self._draw_queue.append(_draw)

    def draw_rectangle(self, start_pos, end_pos, color=(255, 0, 0), thickness=2):
        def _draw(dc):
            pen = win32gui.CreatePen(win32con.PS_SOLID, thickness, 
                                   win32api.RGB(*color))
            old_pen = win32gui.SelectObject(dc, pen)
            
            win32gui.Rectangle(dc, 
                             int(start_pos[0]), int(start_pos[1]),
                             int(end_pos[0]), int(end_pos[1]))
            
            win32gui.SelectObject(dc, old_pen)
            win32gui.DeleteObject(pen)

        with self._lock:
            self._draw_queue.append(_draw)
    
    # Add this method to the Overlay class
    def draw_circle(self, center, radius, color=(255, 0, 0), thickness=2):
        def _draw(dc):
            pen = win32gui.CreatePen(win32con.PS_SOLID, thickness, 
                                win32api.RGB(*color))
            old_pen = win32gui.SelectObject(dc, pen)
            
            # Draw circle using Ellipse
            left = int(center[0] - radius)
            top = int(center[1] - radius)
            right = int(center[0] + radius)
            bottom = int(center[1] + radius)
            
            win32gui.Arc(dc, left, top, right, bottom,
                        left, top, left, top)  # Full circle
            
            win32gui.SelectObject(dc, old_pen)
            win32gui.DeleteObject(pen)

        with self._lock:
            self._draw_queue.append(_draw)

    def draw_text(self, text, pos, color=(255, 255, 255), size=16):
        def _draw(dc):
            # Create LOGFONT structure
            lf = LOGFONT()
            lf.lfHeight = size
            lf.lfWidth = 0
            lf.lfWeight = 400
            lf.lfQuality = win32con.ANTIALIASED_QUALITY
            lf.lfCharSet = win32con.ANSI_CHARSET
            
            # Use ctypes to create a wide string
            from ctypes import create_unicode_buffer
            font_name = create_unicode_buffer("Arial")
            lf.lfFaceName = font_name.value

            hfont = windll.gdi32.CreateFontIndirectW(byref(lf))
            old_font = win32gui.SelectObject(dc, hfont)
            
            windll.gdi32.SetTextColor(dc, win32api.RGB(*color))
            windll.gdi32.SetBkMode(dc, win32con.TRANSPARENT)
            
            # Create wide string buffer for the text
            text_buffer = create_unicode_buffer(text)
            windll.gdi32.TextOutW(dc, int(pos[0]), int(pos[1]), text_buffer, len(text))
            
            win32gui.SelectObject(dc, old_font)
            win32gui.DeleteObject(hfont)

        with self._lock:
            self._draw_queue.append(_draw)

    def clear(self):
        def _draw(dc):
            rect = win32gui.GetClientRect(self._hwnd)
            brush = win32gui.CreateSolidBrush(win32api.RGB(0, 0, 0))
            win32gui.FillRect(dc, rect, brush)
            win32gui.DeleteObject(brush)

        with self._lock:
            self._draw_queue.append(_draw)

    def draw_crosshair(self, center, size=24, color=(0, 255, 0), thickness=1):
        def _draw(dc):
            # Create pen for drawing
            pen = win32gui.CreatePen(win32con.PS_SOLID, thickness, 
                                    win32api.RGB(*color))
            old_pen = win32gui.SelectObject(dc, pen)
            
            # Draw outer circle
            radius = size // 2
            left = int(center[0] - radius)
            top = int(center[1] - radius)
            right = int(center[0] + radius)
            bottom = int(center[1] + radius)
            
            win32gui.Arc(dc, left, top, right, bottom,
                        left, top, left, top)  # Full circle
            
            # Draw center dot
            dot_radius = 1
            dot_left = int(center[0] - dot_radius)
            dot_top = int(center[1] - dot_radius)
            dot_right = int(center[0] + dot_radius)
            dot_bottom = int(center[1] + dot_radius)
            
            # Create brush for filled dot
            brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
            old_brush = win32gui.SelectObject(dc, brush)
            
            win32gui.Ellipse(dc, dot_left, dot_top, dot_right, dot_bottom)
            
            # Cleanup
            win32gui.SelectObject(dc, old_pen)
            win32gui.SelectObject(dc, old_brush)
            win32gui.DeleteObject(pen)
            win32gui.DeleteObject(brush)

        with self._lock:
            self._draw_queue.append(_draw)
