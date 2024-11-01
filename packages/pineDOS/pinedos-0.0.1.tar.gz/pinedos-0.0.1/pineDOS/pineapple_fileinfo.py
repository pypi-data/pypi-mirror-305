import os
import time
from pineapple_error import *

class file_info():
    """Get base info of the file you want"""

    @staticmethod
    def file_date(path: str, type = "modification_date") -> str:
        """Returns the date of the file
            Types:
                modification_date,
                creation_date
        """

        if os.path.exists(path):
            file_mdate = os.path.getmtime(path)
            file_cdate = os.path.getctime(path)
            modify_date = time.ctime(file_mdate)
            creation_date = time.ctime(file_cdate)
            if type == "modification_date":
                return modify_date
            elif type == "creation_date":
                return creation_date
            else:
                Errors.unknown_argument()
        else:
            Errors.dir_non_exist()

    @staticmethod
    def file_size(path: str, unit = "bytes") -> int:
        """Returns the size of the file
            Units:
                bytes,
                kilobytes,
                megabytes,
                gigabytes,
                terabytes
        """

        if os.path.exists(path):
            if unit == "bytes":
                file_size = os.path.getsize(path)
                return file_size
            elif unit == "kilobytes":
                file_size = os.path.getsize(path) * 0.0009765625
                return file_size
            elif unit == "megabytes":
                file_size = os.path.getsize(path) * 0.0009765625 ** 2
                return file_size
            elif unit == "gigabytes":
                file_size = os.path.getsize(path) * 0.0009765625 ** 3
                return file_size
            elif unit == "terabytes":
                file_size = os.path.getsize(path) * 0.0009765625 ** 4
                return file_size
            else:
                Errors.unknown_argument()
        else:
            Errors.dir_non_exist()
