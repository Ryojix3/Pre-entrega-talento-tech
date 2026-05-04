import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


VALID_USER     = "standard_user"
VALID_PASSWORD = "secret_sauce"


class TestCatalogo:
    """Casos de prueba para la navegación y verificación del catálogo."""

    @pytest.fixture(autouse=True)
    def login(self, driver):
        """Fixture que hace login antes de cada test de este módulo."""
        self.driver = driver
        login_page = LoginPage(driver)
        login_page.login(VALID_USER, VALID_PASSWORD)
        self.inventory = InventoryPage(driver)

    def test_titulo_pagina_es_correcto(self):
        """Verifica que el título de la sección es 'Products'."""
        title = self.inventory.get_title()
        assert title == "Products", (
            f"Se esperaba 'Products', se obtuvo: '{title}'"
        )

    def test_hay_productos_visibles(self):
        """Verifica que el catálogo muestra al menos un producto."""
        items = self.inventory.get_all_items()
        assert len(items) > 0, "No se encontraron productos en el catálogo."

    def test_productos_tienen_nombre(self):
        """Verifica que todos los productos tienen nombre visible."""
        names = self.inventory.get_item_names()
        assert len(names) > 0, "No se encontraron nombres de productos."
        for name in names:
            assert name.strip() != "", "Se encontró un producto sin nombre."

    def test_productos_tienen_precio(self):
        """Verifica que todos los productos tienen precio visible."""
        prices = self.inventory.get_item_prices()
        assert len(prices) > 0, "No se encontraron precios de productos."
        for price in prices:
            assert "$" in price, f"Precio con formato inesperado: '{price}'"

    def test_dropdown_de_filtro_es_visible(self):
        """Verifica que el dropdown de ordenamiento está disponible."""
        assert self.inventory.is_sort_dropdown_visible(), (
            "El dropdown de filtro/ordenamiento no está visible."
        )
