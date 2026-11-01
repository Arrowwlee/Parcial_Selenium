
from login_page import LoginPage


def test_ejecucion_pom(driver):
    driver.get("https://www.saucedemo.com")

    # Caso de uso: login fallido
    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    mensaje = login.obtener_error()
    print(f"Resultado de la prueba: {mensaje}")

    assert "locked out" in mensaje.lower()
