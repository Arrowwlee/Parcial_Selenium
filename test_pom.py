from selenium import webdriver

from login_page import LoginPage


def test_ejecucion_pom() -> None:
    driver = webdriver.Chrome()

    try:
        driver.get("https://saucedemo.com")

        # Caso de uso: login fallido
        login = LoginPage(driver)
        login.ingresar_credenciales("locked_out_user", "secret_sauce")
        login.click_login()

        mensaje = login.obtener_error()
        print(f"Resultado de la prueba: {mensaje}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_ejecucion_pom()
