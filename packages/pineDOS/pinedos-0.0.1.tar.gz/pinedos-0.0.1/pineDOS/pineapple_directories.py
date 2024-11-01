import os
from pineapple_error import *

class DirectoryControllerClass():
    """Easy directory controller to create folders"""

    @staticmethod
    def create_directory(name: str, path = str(os.path.abspath("./"))) -> None:
        """Creates directory by name, path (optional)"""

        if not os.path.exists(f"{path}/{name}"):
            os.makedirs(f"{path}/{name}")
        else:
            Errors.dir_exist()

    @staticmethod
    def delete_directory(path: str) -> None:
        """Deletes directory by path"""

        if os.path.exists(path):
            os.removedirs(path)
        else:
            Errors.dir_non_exist()

    @staticmethod
    def remane_directory(name: str, new_name: str, path = str(os.path.abspath("./"))) -> None:
        """Renames directory by path"""

        if os.path.exists(f"{path}/{name}"):
            os.chdir(path)
            os.rename(name, new_name)
        else:
            Errors.dir_non_exist()

def current_directory(directory_path: str) -> str:
    """Checks if directory exists and saves it in variable"""

    if os.path.exists(directory_path):
        curent_directory = directory_path
        return curent_directory
    else:
        Errors.dir_non_exist()

def directory_content(path: str) -> list:
    """Returns a list of content of a directory by path"""

    dir_content_list = []
    if os.path.exists(path):
        with os.scandir(path) as dir_content:
            for file in dir_content:
                dir_content_list.append(file.name)
        return dir_content_list
    else:
        Errors.dir_non_exist()
