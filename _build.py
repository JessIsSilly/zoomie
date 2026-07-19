import PyInstaller.__main__
import os
import shutil

PyInstaller.__main__.run([
    "--clean",
    "--onefile",
    "--collect-all", "apple_fm_sdk",
    "--add-data", "www:www",
    "--name", "Zoomie Server",
    "web.py"
])

shutil.copyfile(os.path.join(os.path.dirname(__file__), "config.py"), os.path.join(os.path.dirname(__file__), "dist", "config.py"))