import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


VALID_USER     = "standard_user"
VALID_PASSWORD = "secret_sauce"


class TestCarrito:
    """Casos de prueba para la interacción con el carrito de compras."""

    @pytest.fixture(autouse=True)
    def login(self, driver):
        """Fixture que hace login antes de cada test de este módulo."""
        self.driver = driver
        login_page = LoginPage(driver)
        login_page.login(VALID_USER, VALID_PASSWORD)
        self.inventory = InventoryPage(driver)

    def test_agregar_producto_actualiza_contador(self):
        """
        Verifica que al agregar un producto al carrito,
        el badge del ícono muestra '1'.
        """
        # Act
        self.inventory.add_first_item_to_cart()

        # Assert
        badge_count = self.inventory.get_cart_badge_count()
        assert badge_count == "1", (
            f"Se esperaba badge '1', se obtuvo: '{badge_count}'"
        )

    def test_producto_aparece_en_carrito(self):
        """
        Verifica que el producto agregado aparece efectivamente
        en la página del carrito.
        """
        # Arrange: obtener el nombre del primer producto antes de agregarlo
        nombres_inventario = self.inventory.get_item_names()
        primer_producto = nombres_inventario[0]

        # Act
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()

        # Assert
        cart = CartPage(self.driver)
        nombres_carrito = cart.get_item_names()
        assert primer_producto in nombres_carrito, (
            f"'{primer_producto}' no se encontró en el carrito. "
            f"Productos en carrito: {nombres_carrito}"
        )

    def test_carrito_tiene_un_item(self):
        """
        Verifica que después de agregar un producto,
        el carrito contiene exactamente 1 ítem.
        """
        # Act
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()

        # Assert
        cart = CartPage(self.driver)
        assert cart.get_item_count() == 1, (
            f"Se esperaba 1 item en el carrito, se encontraron: {cart.get_item_count()}"
        )
