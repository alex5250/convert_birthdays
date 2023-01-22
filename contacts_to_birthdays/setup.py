import sys
from cx_Freeze import setup, Executable
import pandas


build_exe_options = {
    "packages": ["os","sys","datetime","dateutil","xlwt","pandas"],
    "zip_include_packages": ["encodings", "bs4","ics","openpyxl","xlwt","pandas"],
}




setup(
    name="cbt",
    version="0.1",
    description="converts birthdays to table",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")],
)