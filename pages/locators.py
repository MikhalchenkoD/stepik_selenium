from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ItemPageLocators:
    CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner strong')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner p strong')