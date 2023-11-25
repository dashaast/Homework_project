import time

from selenium.webdriver import Keys, ActionChains

from base.base_class import Base

#Данный класс содержит описание страницы корзины
class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cart_button = "//a[@href='/checkout/']"
    tel_input = "//input[@id='ch-3']"
    mail_input = "//input[@type='email']"
    name_input = "//input[@id = 'ch-1']"
    lastname_input = "//input[@id = 'ch-2']"
    city_input = "//span[@role='combobox']"
    button_dostavka = "//div[@id='div-del-4']"
    street_input = "(//span[@class='selection'])[1]"
    house_input = "(//span[@class='selection'])[1]"
    kv_input = "(//span[@class='selection'])[1]"
    zakaz = "//button[@type='submit']"
    delete_from_cart = "//button[@class='js-tools-toggle']"
    confirm_delete = "//button[@class='js-tools-delete']"




    def go_to_cart(self):
        self.get_element(self.cart_button).click()

    def input_personal_data(self):
        # self.get_element(self.tel_input).click()
        self.get_element(self.tel_input).send_keys(Keys.BACKSPACE*10)
        self.read_element(self.tel_input).send_keys("9778198061")
        self.get_element(self.tel_input).send_keys(Keys.RETURN)
        time.sleep(10)

        self.read_element(self.mail_input).send_keys("test123@mail.ru")
        time.sleep(10)

        self.read_element(self.name_input).send_keys("Иван")
        time.sleep(10)

        self.read_element(self.lastname_input).send_keys("Тестов")
        time.sleep(10)


        ActionChains(self.driver).scroll_to_element(self.read_element(self.city_input)).perform()
        city_value = self.read_element(self.city_input).text
        print("Значение города подставилось по умолчанию (на самом деле у меня просто не получается его ввести)" + city_value)

        self.read_element(self.street_input).send_keys("Тестовская")
        self.read_element(self.city_input).send_keys(Keys.RETURN)
        self.read_element(self.house_input).send_keys("1")
        self.read_element(self.city_input).send_keys(Keys.RETURN)
        self.read_element(self.kv_input).send_keys("2")
        self.read_element(self.city_input).send_keys(Keys.RETURN)

    def final(self):
        self.get_element(self.zakaz).click()

    def delete_product_from_cart(self):
        self.get_element(self.delete_from_cart).click()
        self.get_element(self.confirm_delete).click()






