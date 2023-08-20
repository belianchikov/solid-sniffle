import time

import pytest

from pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # time.sleep(1)
    page.solve_quiz_and_get_code()
    # print("product name is ", page.get_product_name())
    # print("product price is ", page.get_product_price())
    # print("basket price from alert is ", page.get_basket_price_from_alert())
    page.check_added_product_name_equal_to_product_name()
    page.check_basket_price_equal_to_product_price()

    time.sleep(2)
