import os
import sys
import subprocess
import shutil

print("=" * 60)
print("Building YouTube Player Pro Standalone Executable (.exe)")
print("=" * 60)

# Build command with PyInstaller
cmd = [
    sys.executable, "-m", "PyInstaller",
    "--noconsole",                           # NO CMD WINDOW!
    "--onefile",                             # Single portable .exe
    "--name=YouTubePlayerPro",
    "--icon=app.ico",
    "--add-data=public;public",
    "--add-data=app.ico;.",
    "--hidden-import=uvicorn.logging",
    "--hidden-import=uvicorn.loops",
    "--hidden-import=uvicorn.loops.auto",
    "--hidden-import=uvicorn.protocols",
    "--hidden-import=uvicorn.protocols.http",
    "--hidden-import=uvicorn.protocols.http.auto",
    "--hidden-import=uvicorn.protocols.websockets",
    "--hidden-import=uvicorn.protocols.websockets.auto",
    "--hidden-import=uvicorn.lifespan",
    "--hidden-import=uvicorn.lifespan.on",
    "--hidden-import=fastapi",
    "--hidden-import=fastapi.staticfiles",
    "--hidden-import=httpx",
    "--hidden-import=yt_dlp",
    "--hidden-import=qrcode",
    "--hidden-import=pystray",
    "--hidden-import=PIL",
    "--hidden-import=PIL.Image",
    "--hidden-import=static_ffmpeg",
    "--clean",
    "main.py"
]

print("Running command:")
print(" ".join(cmd))
res = subprocess.run(cmd)

if res.returncode == 0:
    print("\n[SUCCESS] YouTubePlayerPro.exe built successfully!")
    exe_path = os.path.abspath(os.path.join("dist", "YouTubePlayerPro.exe"))
    print(f"Location: {exe_path}")
    print(f"Size: {os.path.getsize(exe_path) / (1024 * 1024):.2f} MB")
else:
    print(f"\n[ERROR] Build failed with return code {res.returncode}")
    sys.exit(res.returncode)

