import os
import sys
import shutil
import time
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

# Enable High-DPI awareness on Windows so UI elements and Khmer fonts are crisp and never clipped
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    try:
        import ctypes
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

def create_windows_shortcut(target_path: str, shortcut_path: str, icon_path: str = None, description: str = ""):
    """Create a Windows .lnk shortcut using VBScript."""
    vbs_content = f'''
Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "{shortcut_path}"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{target_path}"
oLink.WorkingDirectory = "{os.path.dirname(target_path)}"
oLink.Description = "{description}"
'''
    if icon_path and os.path.exists(icon_path):
        vbs_content += f'oLink.IconLocation = "{icon_path}, 0"\n'
    vbs_content += 'oLink.Save\n'

    temp_vbs = os.path.join(os.environ.get("TEMP", "C:\\Temp"), "create_shortcut.vbs")
    try:
        with open(temp_vbs, "w", encoding="utf-8") as f:
            f.write(vbs_content)
        subprocess.run(["cscript", "//nologo", temp_vbs], check=False, creationflags=0x08000000)
    except Exception:
        pass
    finally:
        if os.path.exists(temp_vbs):
            try:
                os.remove(temp_vbs)
            except Exception:
                pass

class SetupInstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Player Pro - Setup Wizard")
        
        # Generous dimensions so all text, badges, and buttons have plenty of room with zero clipping
        win_w, win_h = 660, 570
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = max(0, int((screen_w - win_w) / 2))
        y = max(0, int((screen_h - win_h) / 2))
        self.root.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.root.minsize(600, 500)
        self.root.resizable(True, True)
        self.root.configure(bg="#0f0f0f")

        # Locate bundled or adjacent YouTubePlayerPro.exe
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        self.source_exe = os.path.join(base_dir, "YouTubePlayerPro.exe")
        if not os.path.exists(self.source_exe):
            self.source_exe = os.path.join(base_dir, "dist", "YouTubePlayerPro.exe")

        # Set taskbar and window icon
        ico_candidates = [
            os.path.join(base_dir, "app.ico"),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.ico"),
            os.path.abspath("app.ico")
        ]
        self.source_ico = None
        for p in ico_candidates:
            if p and os.path.exists(p):
                self.source_ico = p
                try:
                    self.root.iconbitmap(p)
                except Exception:
                    pass
                break

        # Default installation directory
        default_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:\\"), "Programs", "YouTubePlayerPro")
        self.install_dir = default_dir

        self.create_widgets()

    def create_widgets(self):
        # 1. Header Banner (Top)
        header = tk.Frame(self.root, bg="#212121", height=95)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        # Golden Owner Badge (Right)
        owner_frame = tk.Frame(header, bg="#2a2205", bd=1, relief="solid")
        owner_frame.pack(side="right", padx=20, pady=24)
        owner_lbl = tk.Label(
            owner_frame,
            text="👑 ម្ចាស់កម្មសិទ្ធិ៖ លោក សុង ហួរ",
            font=("Khmer OS Siemreap", 9, "bold"),
            fg="#ffd700",
            bg="#2a2205",
            padx=10,
            pady=4
        )
        owner_lbl.pack()

        # Titles (Left)
        title_lbl = tk.Label(
            header,
            text="YouTube Player Pro",
            font=("Segoe UI", 16, "bold"),
            fg="#ffffff",
            bg="#212121"
        )
        title_lbl.pack(anchor="w", padx=22, pady=(16, 2))

        sub_lbl = tk.Label(
            header,
            text="កម្មវិធីដំឡើងលើកុំព្យូទ័រ (Setup Wizard) • គ្មានពាណិជ្ជកម្ម & ចាក់ពេលបិទអេក្រង់",
            font=("Khmer OS Siemreap", 9),
            fg="#aaaaaa",
            bg="#212121"
        )
        sub_lbl.pack(anchor="w", padx=22)

        # 2. Bottom Button Bar (Packed FIRST with side="bottom" so it is ALWAYS visible)
        bottom = tk.Frame(self.root, bg="#181818", height=72, bd=1, relief="ridge")
        bottom.pack(fill="x", side="bottom")
        bottom.pack_propagate(False)

        self.install_btn = tk.Button(
            bottom,
            text="ដំឡើងឥឡូវនេះ (Install Now)",
            font=("Khmer OS Siemreap", 10, "bold"),
            fg="#ffffff",
            bg="#ff0000",
            activebackground="#cc0000",
            activeforeground="#ffffff",
            relief="flat",
            padx=22,
            pady=8,
            cursor="hand2",
            command=self.run_install
        )
        self.install_btn.pack(side="right", padx=20, pady=16)

        self.cancel_btn = tk.Button(
            bottom,
            text="បោះបង់ (Cancel)",
            font=("Khmer OS Siemreap", 9),
            fg="#aaaaaa",
            bg="#2a2a2a",
            activebackground="#3a3a3a",
            activeforeground="#ffffff",
            relief="flat",
            padx=16,
            pady=8,
            cursor="hand2",
            command=self.root.destroy
        )
        self.cancel_btn.pack(side="right", padx=6, pady=16)

        # 3. Main Content Frame (Center - takes remaining space)
        content = tk.Frame(self.root, bg="#0f0f0f", padx=28, pady=20)
        content.pack(fill="both", expand=True)

        info_lbl = tk.Label(
            content,
            text="ទីតាំងដំឡើងកម្មវិធី (Installation Folder):",
            font=("Khmer OS Siemreap", 10, "bold"),
            fg="#f1f1f1",
            bg="#0f0f0f"
        )
        info_lbl.pack(anchor="w", pady=(0, 6))

        # Path display box
        path_frame = tk.Frame(content, bg="#1a1a1a", bd=1, relief="solid")
        path_frame.pack(fill="x", pady=(0, 16))

        self.path_entry = tk.Entry(
            path_frame,
            font=("Consolas", 9),
            fg="#cccccc",
            bg="#1a1a1a",
            bd=0
        )
        self.path_entry.insert(0, self.install_dir)
        self.path_entry.config(state="readonly")
        self.path_entry.pack(fill="x", padx=10, pady=8)

        # Options Checkboxes
        self.cb_desktop_var = tk.BooleanVar(value=True)
        cb_desktop = tk.Checkbutton(
            content,
            text="  បង្កើតផ្លូវកាត់លើ Desktop (Create Desktop Shortcut)",
            variable=self.cb_desktop_var,
            font=("Khmer OS Siemreap", 9),
            fg="#ffffff",
            bg="#0f0f0f",
            selectcolor="#212121",
            activebackground="#0f0f0f",
            activeforeground="#ff0000"
        )
        cb_desktop.pack(anchor="w", pady=4)

        self.cb_start_var = tk.BooleanVar(value=True)
        cb_start = tk.Checkbutton(
            content,
            text="  បន្ថែមក្នុង Start Menu (Add to Start Menu)",
            variable=self.cb_start_var,
            font=("Khmer OS Siemreap", 9),
            fg="#ffffff",
            bg="#0f0f0f",
            selectcolor="#212121",
            activebackground="#0f0f0f",
            activeforeground="#ff0000"
        )
        cb_start.pack(anchor="w", pady=4)

        self.cb_launch_var = tk.BooleanVar(value=True)
        cb_launch = tk.Checkbutton(
            content,
            text="  ចាប់ផ្តើមដំណើរការភ្លាមៗក្រោយដំឡើងរួច (Launch immediately)",
            variable=self.cb_launch_var,
            font=("Khmer OS Siemreap", 9),
            fg="#ffffff",
            bg="#0f0f0f",
            selectcolor="#212121",
            activebackground="#0f0f0f",
            activeforeground="#ff0000"
        )
        cb_launch.pack(anchor="w", pady=4)

        # Status text during install
        self.status_lbl = tk.Label(
            content,
            text="",
            font=("Khmer OS Siemreap", 9),
            fg="#3ea6ff",
            bg="#0f0f0f"
        )
        self.status_lbl.pack(anchor="w", pady=(12, 2))

        # Progress bar (pre-created)
        self.progress = ttk.Progressbar(content, orient="horizontal", mode="indeterminate")

    def run_install(self):
        self.install_btn.config(state="disabled", text="កំពុងដំឡើង...")
        self.cancel_btn.config(state="disabled")
        self.status_lbl.config(text="កំពុងរៀបចំចម្លងឯកសារកម្មវិធី...")
        self.progress.pack(fill="x", pady=5)
        self.progress.start(10)
        self.root.after(200, self._do_install)

    def _do_install(self):
        try:
            target_dir = self.install_dir
            os.makedirs(target_dir, exist_ok=True)

            target_exe = os.path.join(target_dir, "YouTubePlayerPro.exe")
            target_ico = os.path.join(target_dir, "app.ico")

            # 1. Close any running instances first so Windows doesn't lock the executable!
            self.status_lbl.config(text="កំពុងបិទកម្មវិធីចាស់ (ប្រសិនបើមាន)...")
            try:
                subprocess.run(
                    ["taskkill", "/f", "/im", "YouTubePlayerPro.exe"],
                    capture_output=True,
                    creationflags=0x08000000
                )
                time.sleep(0.4)
            except Exception:
                pass

            # 2. Copy files safely
            self.status_lbl.config(text="កំពុងចម្លង YouTubePlayerPro.exe...")
            if not os.path.exists(self.source_exe):
                raise FileNotFoundError(f"រកមិនឃើញ file YouTubePlayerPro.exe សម្រាប់ដំឡើងទេ!\n{self.source_exe}")

            shutil.copy2(self.source_exe, target_exe)

            if os.path.exists(self.source_ico):
                shutil.copy2(self.source_ico, target_ico)

            # 3. Desktop Shortcut
            if self.cb_desktop_var.get():
                self.status_lbl.config(text="កំពុងបង្កើត Shortcut លើ Desktop...")
                desktop = os.path.join(os.environ.get("USERPROFILE", "C:\\"), "Desktop")
                shortcut_path = os.path.join(desktop, "YouTube Player Pro.lnk")
                create_windows_shortcut(
                    target_exe,
                    shortcut_path,
                    target_ico,
                    "YouTube Player Pro - ម្ចាស់កម្មសិទ្ធិ៖ លោក សុង ហួរ"
                )

            # 4. Start Menu Shortcut
            if self.cb_start_var.get():
                self.status_lbl.config(text="កំពុងបង្កើត Shortcut ក្នុង Start Menu...")
                start_menu = os.path.join(
                    os.environ.get("APPDATA", "C:\\"),
                    "Microsoft", "Windows", "Start Menu", "Programs"
                )
                shortcut_path = os.path.join(start_menu, "YouTube Player Pro.lnk")
                create_windows_shortcut(
                    target_exe,
                    shortcut_path,
                    target_ico,
                    "YouTube Player Pro - ម្ចាស់កម្មសិទ្ធិ៖ លោក សុង ហួរ"
                )

            # 5. Create Uninstaller script
            uninstaller_bat = os.path.join(target_dir, "Uninstall.bat")
            with open(uninstaller_bat, "w", encoding="utf-8") as f:
                f.write(f'''@echo off
title Uninstall YouTube Player Pro
echo Stopping YouTube Player Pro...
taskkill /f /im YouTubePlayerPro.exe >nul 2>&1
echo Removing shortcuts...
del "%USERPROFILE%\\Desktop\\YouTube Player Pro.lnk" >nul 2>&1
del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\YouTube Player Pro.lnk" >nul 2>&1
echo Removing files...
timeout /t 2 >nul
rd /s /q "{target_dir}" >nul 2>&1
echo YouTube Player Pro uninstalled successfully.
pause
''')

            # 6. Success State
            self.progress.stop()
            self.progress.pack_forget()
            self.status_lbl.config(text="✅ ការដំឡើងបានជោគជ័យ ១០០%!", fg="#4ade80")
            self.install_btn.config(text="រួចរាល់ (Finished)", state="normal", bg="#16a34a", command=self.root.destroy)
            self.cancel_btn.pack_forget()

            # 7. Launch if checked
            if self.cb_launch_var.get():
                try:
                    subprocess.Popen([target_exe], creationflags=0x08000000)
                except Exception as e:
                    print("Launch error:", e)

            messagebox.showinfo(
                "ជោគជ័យ",
                "🎉 ការដំឡើង YouTube Player Pro បានជោគជ័យ!\n\nផ្លូវកាត់ Shortcut ត្រូវបានបង្កើតលើ Desktop រួចរាល់។"
            )
            self.root.destroy()

        except Exception as err:
            self.progress.stop()
            self.progress.pack_forget()
            self.status_lbl.config(text="❌ កំហុសក្នុងការដំឡើង", fg="#f87171")
            self.install_btn.config(state="normal", text="សាកល្បងម្ដងទៀត (Retry)")
            self.cancel_btn.config(state="normal")
            messagebox.showerror(
                "កំហុសក្នុងការដំឡើង",
                f"ការដំឡើងមិនជោគជ័យទេ៖\n{err}\n\nសូមព្យាយាមម្ដងទៀត។"
            )

def main():
    root = tk.Tk()
    app = SetupInstallerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
