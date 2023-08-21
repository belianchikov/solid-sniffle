from locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        empty_basket_message = (self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
                                .get_attribute("innerHTML"))
        assert ("Your basket is empty." in empty_basket_message), \
            f"Wrong message for empty basket. Expected 'Ваша корзина пуста'. Actual {empty_basket_message}"

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_name()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Wrong URL for basket page"

    def should_be_basket_name(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NAME), "There is no basket name"
