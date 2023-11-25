from selenium import webdriver

from base.base_class import Base
from pages.favourite_page import Favourite
from pages.main_page import Main_page
from pages.product_page import Product_page


def test_add_to_favourite():
    driver = webdriver.Chrome()
    mp = Main_page(driver)
    mp.way_to_product_woman()
    pp = Product_page(driver)
    pp.add_to_favourite()
    fp = Favourite(driver)
    fp.get_favourite_product()
    if pp.add_to_favourite() == fp.get_favourite_product():
        print("Add Fovourite Success Test")
    else: print("Something Wrong")
