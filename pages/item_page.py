from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def click_to_cart_btn(self):
        btn = self.browser.find_element(*ItemPageLocators.CART_BTN)
        btn.click()

    def get_title(self):
        title = self.browser.find_element(*ItemPageLocators.TITLE)
        return title.text

    def get_price(self):
        price = self.browser.find_element(*ItemPageLocators.PRICE)
        return price.text

    def get_title_in_message(self):
        title = self.browser.find_element(*ItemPageLocators.TITLE_IN_MESSAGE)
        return title.text

    def get_price_in_message(self):
        price = self.browser.find_element(*ItemPageLocators.PRICE_IN_MESSAGE)
        return price.text

    def check_item_value_and_message_value(self):
        item_price = self.get_price()
        message_price = self.get_price_in_message()

        item_title = self.get_title()
        message_title = self.get_title_in_message()

        assert item_title == message_title, 'Название не соответствует названию в сообщении'
        assert message_price == item_price, 'Цена не соответствует цене в сообщении'
