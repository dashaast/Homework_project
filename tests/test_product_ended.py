import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from pages.main_page import Main_page
from pages.product_page import Product_page

def test_product_ended():

    driver = webdriver.Chrome()
    mp = Main_page(driver)
    pp = Product_page(driver)

    mp.way_to_product_woman()

    try:
        pp.get_element(pp.size_unavailable).click()
        time.sleep(3)
        assert pp.read_element(pp.button_disable).text == "СООБЩИТЬ О ПОСТУПЛЕНИИ"
        print("The Text Anavailable Is Good")
    except NoSuchElementException:
        print("All the items of this product are available! OR The Text Is Not Correct!")
