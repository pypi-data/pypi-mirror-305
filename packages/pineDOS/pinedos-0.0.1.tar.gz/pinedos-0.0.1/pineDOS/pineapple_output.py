from string import ascii_letters, punctuation, digits
from pineapple_error import *
from pineapple_default_color import *
import time
import os

#Gets all ascii characters
class AsciiCharactersList():
    """Table of ascii letters"""
    
    @property
    def ascii_table(self) -> list:
        """Creates list of Ascii characters"""
        
        ascii_chars_list = []

        ascii_chars_str = ascii_letters + punctuation + digits

        for i in range(0, len(ascii_chars_str)):
            ascii_chars_list.append(ascii_chars_str[i : i + 1])
        
        return ascii_chars_list

#Customisible text color
class Color():
    """Color codes for text"""

    red = "\033[31m"
    blue = "\033[34m"
    yellow = "\033[33m"
    green = "\033[32m"
    purple = "\033[35m"
    cyan = "\033[36m"
    black = "\033[30m"
    white = "\033[37m"

    @staticmethod
    def reset():
        """Resets output color"""

        print(f"{SetColor.default_color}{SetColor.default_bg}".format(""))

#Customisible background color
class BGColor():
    """Color codes for output background"""

    bg_red = "\033[41m{}"
    bg_blue = "\033[44m{}"
    bg_yellow = "\033[43m{}"
    bg_green = "\033[42m{}"
    bg_purple = "\033[45m{}"
    bg_cyan = "\033[46m{}"
    bg_white = "\033[47m{}"

#Text output command (text can be stylized)
def cout(text, color = "", bg = "") -> None:
    """Customisible print() function"""

    if color == "" and bg == "":
        print(text)
    else:
        print(f"{color}{bg}".format(text))
        Color.reset()

#Text input command
def cin(placeholder = ">>>  ", type = str, ascii_check = False, color = "", bg = "") -> type:
    """Input command that checks for ascii characters"""
    if color != "" or bg != "":
        print(f"{color}{bg}".format(""))

    if ascii_check:
        while True:
            error = False
            cin_var = input(placeholder)
            for char in cin_var:
                if char not in AsciiCharactersList().ascii_table:
                    Errors.not_in_ascii()
                    error = True
            if not error:
                break
            else:
                continue
    else:
        cin_var = input(placeholder)
    Color.reset()
    return type(cin_var)

#delay
def delay(seconds: float) -> None:
    """Delay"""

    time.sleep(seconds)

#Clears output (supports Unix)
def clear_output() -> None:
    """Clears output (supports Unix)"""

    os.system('cls' if os.name == 'nt' else "clear")

def cute() -> None:
    print(":3")
