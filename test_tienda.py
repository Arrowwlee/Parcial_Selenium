import pytest
from selenium import webdriver

from login_page import LoginPage


@pytest.fixture
def driver():
    """Configura el navegador para cada prueba."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login_fallido(driver):
    """Comprueba el acceso de un usuario bloqueado."""
    driver.get("https://saucedemo.com")
    login = LoginPage(driver)

    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    assert "locked out" in login.obtener_error()


def test_login_exitoso(driver):
    """Comprueba el acceso de un usuario válido."""
    driver.get("https://saucedemo.com")
    login = LoginPage(driver)

    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    # Fallo controlado para comprobar la captura de pantalla de conftest.py.
    assert "url_inexistente.html" in driver.current_url
