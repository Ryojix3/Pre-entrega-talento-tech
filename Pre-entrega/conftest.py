import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Inicializa y cierra el WebDriver para cada test."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")          # Sin ventana (útil en CI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)  # Espera implícita de 10 segundos

    yield driver  # El test se ejecuta aquí

    driver.quit()  # Teardown: cierra el navegador al terminar
