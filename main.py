import os
import sys

# Ensure sys.stdout and sys.stderr exist (crucial for PyInstaller --noconsole)
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w", encoding="utf-8")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w", encoding="utf-8")

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import time
import socket
import threading
import webbrowser
from PIL import Image
import pystray
import uvicorn

# Helper for resource path inside PyInstaller bundle
def get_resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

# Check if port 8000 is already in use (app already running)
def is_port_in_use(port: int = 8000) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

class ServerRunner:
    def __init__(self):
        self.server = None
        self.thread = None

    def start(self):
        from server import app
        config = uvicorn.Config(
            app=app,
            host="0.0.0.0",
            port=8000,
            log_config=None,
            access_log=False
        )
        self.server = uvicorn.Server(config)
        self.thread = threading.Thread(target=self.server.run, daemon=True)
        self.thread.start()

    def stop(self):
        if self.server:
            self.server.should_exit = True

def open_browser(url: str = "http://127.0.0.1:8000"):
    """Ultra-fast browser launch using direct Windows ShellExecute (0.01s)."""
    if sys.platform == "win32":
        try:
            os.startfile(url)
            return
        except Exception:
            pass
    try:
        webbrowser.open(url)
    except Exception:
        pass

def open_mobile_info():
    open_browser("http://127.0.0.1:8000/api/system/ip")

def create_tray_icon(runner):
    icon_path = get_resource_path("app.ico")
    if os.path.exists(icon_path):
        image = Image.open(icon_path)
    else:
        # Fallback 32x32 red circle if icon missing
        image = Image.new('RGB', (32, 32), color=(255, 0, 0))

    def on_open(icon, item):
        open_browser()

    def on_exit(icon, item):
        icon.stop()
        if runner:
            runner.stop()
        sys.exit(0)

    menu = pystray.Menu(
        pystray.MenuItem("▶ បើក YouTube Player Pro", on_open, default=True),
        pystray.MenuItem("👑 ម្ចាស់កម្មសិទ្ធិ៖ លោក សុង ហួរ", None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("🌐 Open in Browser", on_open),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("❌ បិទកម្មវិធី (Exit)", on_exit)
    )

    icon = pystray.Icon("YouTubePlayerPro", image, "YouTube Player Pro", menu)
    return icon

def main():
    target_url = "http://127.0.0.1:8000"

    # 1. If server is already running, open browser instantly and exit in 0.01s
    if is_port_in_use(8000):
        open_browser(target_url)
        sys.exit(0)

    # 2. Parallel Instant Browser Launcher:
    # Continuously probes port 8000 every 15ms so the millisecond uvicorn binds,
    # the browser opens instantly with zero artificial delay!
    def _instant_browser_opener():
        start_t = time.time()
        while time.time() - start_t < 12.0:
            if is_port_in_use(8000):
                break
            time.sleep(0.015)
        open_browser(target_url)

    threading.Thread(target=_instant_browser_opener, daemon=True).start()

    # 3. Start server
    runner = ServerRunner()
    runner.start()

    # 4. Start system tray icon (keeps app alive in background without CMD window)
    tray = create_tray_icon(runner)
    tray.run()

if __name__ == "__main__":
    main()

