from SeleniumLibrary import SeleniumLibrary
from .keywords import TableKeyword

__version__ = '1.0.0'


class ICOLibrary(SeleniumLibrary):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        SeleniumLibrary.__init__(self, 30)
        self.add_library_components(
            [
                TableKeyword(self),
            ]
        )