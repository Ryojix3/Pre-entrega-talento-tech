from selenium.webdriver.common.by import By


class InventoryPage:
    """Page Object para la página de inventario/catálogo."""

    # Locators
    PAGE_TITLE        = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS   = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES        = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES       = (By.CLASS_NAME, "inventory_item_price")
    ITEM_IMAGES       = (By.CLASS_NAME, "inventory_item_img")
    SORT_DROPDOWN     = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BTN   = (By.CSS_SELECTOR, ".inventory_item button")
    CART_BADGE        = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON         = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self) -> str:
        return self.driver.find_element(*self.PAGE_TITLE).text

    def get_all_items(self):
        return self.driver.find_elements(*self.INVENTORY_ITEMS)

    def get_item_names(self) -> list[str]:
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def get_item_prices(self) -> list[str]:
        return [el.text for el in self.driver.find_elements(*self.ITEM_PRICES)]

    def get_item_images(self):
        return self.driver.find_elements(*self.ITEM_IMAGES)

    def add_first_item_to_cart(self):
        """Agrega el primer producto al carrito."""
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        buttons[0].click()

    def get_cart_badge_count(self) -> str:
        return self.driver.find_element(*self.CART_BADGE).text

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    def is_sort_dropdown_visible(self) -> bool:
        return len(self.driver.find_elements(*self.SORT_DROPDOWN)) > 0
