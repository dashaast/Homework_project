import time

from base.base_class import Base


class Favourite(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    favourite_page = "(//a[@class='header__link mod-no-sm'])[1]"
    favourite_product = "//a[@class='header__link mod-no-sm']"

    def get_favourite_product(self):
        self.get_element(self.favourite_page).click()
        time.sleep(30)
        self.get_element(self.favourite_product).click()
        return self.get_url()
