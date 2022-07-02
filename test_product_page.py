from .pages.base_page import BasePage
from .pages.locators import BusketPageLocators
from .pages.product_page import ProductPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_message_product_in_basket()
    product_page.check_message_product_price_in_basket()