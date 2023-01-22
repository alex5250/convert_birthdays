import os
import datetime

def version():
    """
    Prints the current version of the project.
    """
    print("v0.0.1 alpha by alex5250")
    pass

def build_docs():
    """
    Builds the documentation for the project using pdoc.
    """
    os.system('pdoc -d markdown ./contacts_to_birthdays/main.py  -o ./docs --logo "https://placedog.net/300?random"')
    pass
