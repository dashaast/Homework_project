import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    woman = "//a[@href='/catalog/zhenshchiny/']"
    man = "//a[@href='/catalog/muzhchiny/']"
    children = "(//li[@class='menu__item-1'])[3]"
    trikotazh_w = "//a[@href='/catalog/zhenshchiny/trikotazh/']"
    rubashki_m = "//a[@href='/catalog/muzhchiny/rubashki/']"
    girls_limit_six = "(//li[@class='menu__item-1'])[7]"
    girls_leggins = "//a[@href='/catalog/deti/devochki/12_18_mes_5_6_let/legginsy/']"
    woman_product = "(//a[@class='preview__title t-bold'])[1]"
    man_product = "(//a[@class='preview__title t-bold'])[1]"
    child_product = "(//a[@class='preview__title t-bold'])[6]"
    url = "https://ru.benetton.com/"

    def open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def get_element(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, value=locator)))

    def hovering(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def way_to_product_woman(self):
        self.open_url()
        self.hovering(self.get_element(self.woman))
        time.sleep(10)
        self.hovering(self.get_element(self.trikotazh_w))
        self.get_element(self.trikotazh_w).click()
        self.get_element(self.woman_product).click()

    def way_to_product_man(self):
        self.hovering(self.get_element(self.man))
        time.sleep(10)
        self.hovering(self.get_element(self.rubashki_m))
        self.get_element(self.rubashki_m).click()
        self.get_element(self.man_product).click()

    def way_to_product_girl(self):
        self.hovering(self.get_element(self.children))
        time.sleep(3)
        self.hovering(self.get_element(self.girls_limit_six))
        time.sleep(3)
        self.get_element(self.girls_leggins).click()
        self.get_element(self.child_product).click()
