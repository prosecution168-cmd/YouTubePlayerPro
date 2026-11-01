import os
import sys
import subprocess
import shutil

print("=" * 60)
print("Building Setup_YouTubePlayerPro.exe (Windows Installer GUI)")
print("=" * 60)

cmd = [
    sys.executable, "-m", "PyInstaller",
    "--noconsole",
    "--onefile",
    "--name=Setup_YouTubePlayerPro",
    "--icon=app.ico",
    "--add-data=dist/YouTubePlayerPro.exe;.",
    "--add-data=app.ico;.",
    "--clean",
    "setup_wizard.py"
]

print("Running command:")
print(" ".join(cmd))
res = subprocess.run(cmd)

if res.returncode == 0:
    print("\n[SUCCESS] Setup_YouTubePlayerPro.exe built successfully!")
    setup_path = os.path.abspath(os.path.join("dist", "Setup_YouTubePlayerPro.exe"))
    print(f"Location: {setup_path}")
    print(f"Size: {os.path.getsize(setup_path) / (1024 * 1024):.2f} MB")
    
    # Copy both to root folder for easy access
    root_exe = os.path.join(os.path.dirname(__file__), "YouTubePlayerPro.exe")
    root_setup = os.path.join(os.path.dirname(__file__), "Setup_YouTubePlayerPro.exe")
    shutil.copy2(os.path.join("dist", "YouTubePlayerPro.exe"), root_exe)
    shutil.copy2(setup_path, root_setup)
    print(f"Copied to root folder:\n -> {root_exe}\n -> {root_setup}")
else:
    print(f"\n[ERROR] Setup build failed with code {res.returncode}")
    sys.exit(res.returncode)

