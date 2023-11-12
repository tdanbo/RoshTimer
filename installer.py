import subprocess
import os
import shutil
import constants as const
def compile_exe() -> None:   
    cleanup()
    subprocess.call(["pyinstaller", "installer.spec"])
    shutil.move(f"dist/{const.SCRIPT_NAME}.exe", f"{const.SCRIPT_NAME}.exe")
    cleanup()

def cleanup() -> None:
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")


compile_exe()