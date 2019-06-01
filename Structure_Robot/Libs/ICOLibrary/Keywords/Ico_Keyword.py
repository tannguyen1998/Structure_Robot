from SeleniumLibrary.base import keyword, LibraryComponent
from selenium.common.exceptions import ElementNotVisibleException


class TableKeyword(LibraryComponent):

    @keyword
    def click_element_page(self, locator):
        """Click element on page"""
        try:
            self.find_element(locator).click()
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def verify_title_page(self):
        """Verify title on page current"""
        try:
            if self.driver.title != "":
                print(self.driver.title)
                return self.driver.title
            else:
                raise ElementNotVisibleException
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def input_text_element(self, locator, text_input):
        """Input text on page"""
        try:
            element = self.driver.find_element_by_name(locator)
            element.send_keys(text_input)
        except ElementNotVisibleException as err:
            print(str(err))