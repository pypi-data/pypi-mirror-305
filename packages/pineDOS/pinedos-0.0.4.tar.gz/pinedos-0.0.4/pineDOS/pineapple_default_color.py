class SetColor:
    """Class to set default console color or console bg color"""

    default_color = "\033[0m{}"
    default_bg = ""

    @classmethod
    def set_default_color(cls, color: str) -> None:
        """Sets default text color"""
        if color != None:
            cls.default_color = color
    
    @classmethod
    def set_default_bg(cls, bg: str) -> None:
        """Sets default bg color"""
        if bg != None:
            cls.default_bg = bg
