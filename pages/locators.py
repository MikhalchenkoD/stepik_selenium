from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BTN = (By.CSS_SELECTOR, ".basket-mini .btn-group a.btn.btn-default")

class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner strong')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages')


class BasketPageLocators:
    MESSAGE_EMPTY_CART = (By.CSS_SELECTOR, '#content_inner > p')