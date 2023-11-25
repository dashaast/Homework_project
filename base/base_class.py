from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():

    def __init__(self, driver):
        self.driver = driver

    def hovering(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_element(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, value=locator)))

    def read_element(self, locator):
        return self.driver.find_element(By.XPATH, value=locator)

    def get_url(self):
        return self.driver.current_url


