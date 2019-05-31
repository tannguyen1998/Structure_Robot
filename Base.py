from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InvalidArgumentException


class Base(object):

    def __init__(self):
        self.driver = None

    def open_browser(self, url, de_play_time=5):
        """Open browser on page"""
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(de_play_time)
        except ElementNotVisibleException as err:
            self.driver.save_screenshot("screen_shot.png")
            print(str(err))

    def close_browser(self):
        """Close browser on page"""
        try:
            self.driver.quit()
        except ElementNotVisibleException as err:
            self.driver.save_screenshot("screen_shot.png")
            print(str(err))

    def verify_title_on_page(self):
        """Verify title on page current"""
        try:
            if self.driver.title != "":
                return self.driver.title
            else:
                raise Exception
        except ElementNotVisibleException as err:
            print(str(err))

    def element_class_name(self, element):
        """Find Element By Class Name"""
        try:
            find_element = self.driver.find_element(By.CLASS_NAME, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def element_css_selector(self, element):
        """Find Element By CSS Selector"""
        try:
            find_element = self.driver.find_element(By.CSS_SELECTOR, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def element_id(self, element):
        """Find Element By ID"""
        try:
            find_element = self.driver.find_element(By.ID, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def element_link_text(self, element):
        """Find Element By Link Text"""
        try:
            find_element = self.driver.find_element(By.LINK_TEXT, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def element_name(self, element):
        """Find Element By Name"""
        try:
            find_element = self.driver.find_element(By.NAME, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def element_partial_link_text(self, element):
        """Find Element By Partial Link Text"""
        try:
            find_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def element_tag_name(self, element):
        """Find Element By Tag Name"""
        try:
            find_element = self.driver.find_element(By.TAG_NAME, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def element_xpath(self, element):
        """Find Element By XPATH"""
        try:
            find_element = self.driver.find_element(By.XPATH, element)
            return find_element
        except ElementNotVisibleException as err:
            print(str(err))

    def locate_element(self, element):
        """Locating Element"""
        try:
            if self.element_id(element):
                return self.element_id(element)
            elif self.element_name(element):
                return self.element_name(element)
            elif self.element_class_name(element):
                return self.element_class_name(element)
            elif self.element_tag_name(element):
                return self.element_tag_name(element)
            elif self.element_link_text(element):
                return self.element_link_text(element)
            elif self.element_partial_link_text(element):
                return self.element_partial_link_text(element)
            elif self.element_xpath(element):
                return self.element_xpath(element)
            elif self.element_css_selector(element):
                return self.element_css_selector(element)
            else:
                raise Exception
        except ElementNotVisibleException as err:
            print("Element %s doesn't exist" % element)
            print(str(err))

    def input_value(self, element, value):
        """Fill out a value to element"""
        try:
            find_element = self.locate_element(element)
            find_element.send_keys(value)
        except InvalidArgumentException as err:
            print(str(err))

    def click_element(self, element):
        """Click Element"""
        try:
            find_element = self.locate_element(element)
            find_element.click()
        except ElementClickInterceptedException as err:
            print(str(err))

    def wait_element_is_visible(self, element, dep_lay_time=20):
        try:
            element_wait = WebDriverWait(self.driver, dep_lay_time).until(
                EC.presence_of_element_located((By.NAME, element))
            )
            return element_wait
        except ElementNotVisibleException as err:
            print(str(err))
