from selenium import webdriver

from pages.main_page import Main_page
from pages.product_page import Product_page


def test_add_product_to_cart():
    driver = webdriver.Chrome()

    mp = Main_page(driver)
    pp = Product_page(driver)

    mp.way_to_product_woman()
    pp.select_product_parameters_w()
    mp.way_to_product_man()
    pp.select_product_parameters_m()
    mp.way_to_product_girl()
    pp.select_product_parameters_g()




