import pytest
from pages.login_page import LoginPage


VALID_USER     = "standard_user"
VALID_PASSWORD = "secret_sauce"


class TestLogin:
    """Casos de prueba para la autenticación de usuario."""

    def test_login_exitoso(self, driver):
        """
        Verifica que un usuario válido puede iniciar sesión
        y es redirigido a la página de inventario.
        """
        # Arrange
        login_page = LoginPage(driver)

        # Act
        login_page.login(VALID_USER, VALID_PASSWORD)

        # Assert
        assert "/inventory.html" in driver.current_url, (
            f"Se esperaba redirección a /inventory.html, pero la URL es: {driver.current_url}"
        )

    def test_validacion_con_credenciales_invalidas(self, driver):
        """
        Verifica que se muestra un mensaje de error
        cuando las credenciales son incorrectas.
        """
        # Arrange
        login_page = LoginPage(driver)

        # Act
        login_page.login("usuario_invalido", "clave_incorrecta")

        # Assert
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text, (
            f"Mensaje de error inesperado: {error_text}"
        )

    def test_login_redirige_a_pagina_correcta(self, driver):
        """
        Verifica que tras el login exitoso el título de la página
        contiene 'Products'.
        """
        # Arrange
        login_page = LoginPage(driver)

        # Act
        login_page.login(VALID_USER, VALID_PASSWORD)

        # Assert
        assert "Swag Labs" in driver.title, (
            f"Título de página inesperado: {driver.title}"
        )
