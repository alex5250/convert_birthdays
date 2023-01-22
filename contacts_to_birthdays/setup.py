import sys
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["os","sys","datetime","dateutil","xlwt"],
    "zip_include_packages": ["encodings", "bs4","ics","openpyxl","xlwt"],
}




setup(
    name="cbt",
    version="0.1",
    description="converts birthdays to table",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")],
)