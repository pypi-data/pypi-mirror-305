import os
from .pineapple_error import *

class FileController():
    """Easy directory controller to create files"""

    @staticmethod
    def create_file(name: str, path = str(os.path.abspath("./"))) -> None:
        """Creates file by name, path"""

        if os.path.exists(path):
            with open(f"{path}/{name}", "a+"):
                pass
        else:
            Errors.dir_non_exist()
    
    @staticmethod
    def delete_file(path = str(os.path.abspath("./"))) -> None:
        """Deletes file by path"""

        if os.path.isfile(path):
            os.remove(path)
        else:
            Errors.file_non_exist()
    
    @staticmethod
    def rename_file(name: str, new_name: str, path = str(os.path.abspath("./"))) -> None:
        """Renames file by name, new name, path"""

        if os.path.exists(path):
            if os.path.isfile(f"{path}/{name}"):
                os.chdir(path)
                os.rename(name, new_name)
            else:
                Errors.file_non_exist()
        else:
            Errors.dir_non_exist()
