import os
import platform
import pkgutil
import argparse

def is_nuitka_installed():
    return pkgutil.find_loader("nuitka") is not None

def version():
    """
    Prints the current version of the project.
    """
    print("v0.0.1 alpha by alex5250")

def build_docs():
    """
    Builds the documentation for the project using pdoc.
    """
    os.system('pdoc -d markdown ./contacts_to_birthdays/main.py -o ./docs --logo "https://placedog.net/300?random"')

def install_deps():
    os.system("python -m pip install -U nuitka")


def build_binary():
    # Check the operating system
    os_system = platform.system()
    platform_info = platform.platform()
    os.system("pip install .")
    file_name = f"contacts_birthdays_x64_{os_system}_{platform_info}_{platform.python_version()}"
    if os_system == "Windows":
        file_name += "_"+platform.win32_edition()
        file_name += ".exe"

    if is_nuitka_installed():
        print("Nuitka is installed.")
        cli_command = f"python -m nuitka --follow-imports --onefile --enable-console contacts_birthdays.py --output-filename=\"{file_name}\""
        os.system(cli_command)
    else:
        print("Nuitka is not installed.")
        install_deps()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build binary and generate documentation for contacts_to_birthdays.")
    parser.add_argument("--build-binary", help="Build the binary executable.", action="store_true")
    parser.add_argument("--output-filename", help="Output filename for the binary executable.")
    parser.add_argument("--build-docs", help="Build project documentation.", action="store_true")

    args = parser.parse_args()

    if args.build_binary:
        build_binary()


    if args.build_docs:
        build_docs()
    
    if not (args.build_binary or args.build_docs):
        version()
