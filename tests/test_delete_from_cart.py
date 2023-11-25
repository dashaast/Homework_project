import time

from selenium import webdriver

from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.product_page import Product_page


def test_delete_from_cart():
    driver = webdriver.Chrome()
    text_delete = "//div[@class='b-empty__head']"

    mp = Main_page(driver)
    pp = Product_page(driver)

    mp.way_to_product_woman()
    pp.select_product_parameters_w()

    cp = Cart_page(driver)
    cp.get_element(cp.cart_button).click()
    cp.delete_product_from_cart()
    if "Ваша корзина пуста" in cp.get_element(text_delete).text:
        print("Deleted Successful")
    else: print("Something went wrong")
