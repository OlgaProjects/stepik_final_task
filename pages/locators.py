from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//span[@class="btn-group"]/a')


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//div[@class="alertinner "]/strong[1]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET = (By.XPATH, '//div[@id="content_inner"]/p')
