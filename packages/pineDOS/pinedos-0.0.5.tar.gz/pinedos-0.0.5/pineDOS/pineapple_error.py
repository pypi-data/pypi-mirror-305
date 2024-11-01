import logging
from .pineapple_default_color import *

logging.basicConfig(level=logging.INFO, filename="errors.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")

class Errors():
    """Error notifications"""

    enable_logging = True

    @staticmethod
    def __notificate_error(error):
        print('\033[31m{}'.format(error))
        print(f"{SetColor.default_color}{SetColor.default_bg}".format(""))

    @classmethod
    def not_in_ascii(cls) -> None:
        """Error notifies that there are unicode characters were entered instead of ascii"""

        cls.__notificate_error("Error! Invalid characters were entered!")
        if cls.enable_logging:
            logging.error("Invalid characters were entered!")

    @classmethod
    def dir_non_exist(cls) -> None:
        """Error notifies that such derictory don't exist"""

        cls.__notificate_error("Error! No such derictory exist!")
        if cls.enable_logging:
            logging.error("No such derictory exist!")
    
    @classmethod
    def dir_exist(cls) -> None:
        """Error notifies that derictory already exists"""

        cls.__notificate_error("Error! Derictory already exists!")
        if cls.enable_logging:
            logging.error("Derictory already exists!")
    
    @classmethod
    def file_non_exist(cls) -> None:
        """Error notifies that file doesn't exist"""

        cls.__notificate_error("Error! That file doesn't exist!")
        if cls.enable_logging:
            logging.error("That file doesn't exist!")
    
    @classmethod
    def unknown_argument(cls) -> None:
        """Error notifies that argument is unknown"""

        cls.__notificate_error("Error! Unknown argument!")
        if cls.enable_logging:
            logging.error("Unknown argument!")
    
    @classmethod
    def invalid_file_type(cls) -> None:
        """Error notifies that file type is invalid"""

        cls.__notificate_error("Error! Invalid file type!")
        if cls.enable_logging:
            logging.error("Invalid file type!")
