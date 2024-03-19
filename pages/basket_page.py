from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_empty_cart(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_CART), \
            "Empty message is not presented, but should be"


    def should_not_empty_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_EMPTY_CART), \
            "Empty message is presented, but should not be"