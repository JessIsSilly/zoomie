import PyInstaller.__main__
import config

PyInstaller.__main__.run([
    "--clean",
    "--onefile",
    "--collect-all", "apple_fm_sdk",
    "--add-data", "www:www",
    "--name", "Zoomie Server",
    "web.py"
])