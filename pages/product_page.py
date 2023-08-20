import locators
from locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def get_product_name(self):
        product_name = (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
                        .get_attribute("innerHTML"))
        return product_name

    def get_product_price(self):
        product_price = (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
                         .get_attribute("innerHTML"))
        return product_price

    def get_basket_price_from_alert(self):
        basket_price_from_alert = (self.browser.find_element(*ProductPageLocators.BASKET_PRICE_FROM_ALERT)
                                   .get_attribute("innerHTML"))
        return basket_price_from_alert

    def check_added_product_name_equal_to_product_name(self):
        product_name = (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
                        .get_attribute("innerHTML"))
        product_added_to_basket_alert = (self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_ALERT)
                                         .get_attribute("innerHTML"))

        assert product_name == product_added_to_basket_alert, \
            f"Wrong product name added to the basket. Expected {product_name}. Actual {product_added_to_basket_alert}"

    def check_basket_price_equal_to_product_price(self):
        product_price = (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
                         .get_attribute("innerHTML"))
        basket_price_from_alert = (self.browser.find_element(*ProductPageLocators.BASKET_PRICE_FROM_ALERT)
                                   .get_attribute("innerHTML"))

        assert product_price == basket_price_from_alert, \
            f"Wrong basket price after adding product. Expected {product_price}. Actual {basket_price_from_alert}"
