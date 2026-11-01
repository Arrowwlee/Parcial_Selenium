
from login_page import LoginPage


def test_login_fallido(driver):
    """Comprueba el acceso de un usuario bloqueado."""
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)

    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    assert "locked out" in login.obtener_error().lower()


def test_login_exitoso(driver):
    """Comprueba el acceso de un usuario válido."""
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)

    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    assert "inventory.html" in driver.current_url
