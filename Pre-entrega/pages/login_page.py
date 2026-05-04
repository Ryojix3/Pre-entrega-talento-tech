from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object para la página de login de SauceDemo."""

    URL = "https://www.saucedemo.com"

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.ID, "login-button")
    ERROR_MESSAGE  = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.URL)

    def enter_username(self, username: str):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        """Método de conveniencia: hace el flujo completo de login."""
        self.navigate()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        return self.driver.find_element(*self.ERROR_MESSAGE).text
