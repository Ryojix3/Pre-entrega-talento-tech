from selenium.webdriver.common.by import By


class CartPage:
    """Page Object para la página del carrito."""

    # Locators
    CART_ITEMS   = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES   = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES  = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QTY     = (By.CLASS_NAME, "cart_quantity")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def get_item_names(self) -> list[str]:
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def get_item_count(self) -> int:
        return len(self.get_cart_items())
