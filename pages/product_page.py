import time
from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
# Локаторы цветов, размеров и размеров, которых нет в наличии везде одинаковые (мужчины, женщины, дети)
# Для проверки нужно заранее знать, каких товаров нет в наличии и подставлять нужные индексы в локаторы (например, по базе
#     нет размера s конкретной вещи, значит подставляем в локатор [2])

    color = "(//button[@class='colors__button'])[1]"
    size = "(//button[@class='offers__button'])[4]"
    size_unavailable = "//button[@data-not-available='true']"
    button_buy = "(//div[@class='add'])[1]"
    button_disable = "//button[@class='form-button']"
    favourite_add = "//button[@class='fav-icon form-button']"
    popup_close = "//button[@class='popup__close']"

    def select_colors(self):
        self.get_element(self.color).click()

    def select_size(self):
        self.get_element(self.size).click()

    def press_button_buy(self):
        self.get_element(self.button_buy).click()

    def add_favourite(self):
        self.get_element(self.favourite_add).click()


    def select_product_parameters_w(self):
        self.select_size()
        self.select_colors()
        self.get_element(self.button_buy).click()
        time.sleep(20)
        self.get_element(self.popup_close).click()

    def select_product_parameters_m(self):
        self.select_size()
        self.select_colors()
        self.get_element(self.button_buy).click()
        time.sleep(20)
        self.get_element(self.popup_close).click()

    def select_product_parameters_g(self):
        self.select_size()
        self.select_colors()
        self.get_element(self.button_buy).click()
        time.sleep(20)
        self.get_element(self.popup_close).click()

    def add_to_favourite(self):
        self.add_favourite()
        return self.get_url()

