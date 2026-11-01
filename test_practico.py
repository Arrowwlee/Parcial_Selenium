from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://saucedemo.com"
PASSWORD = "secret_sauce"


def ejecutar_pruebas() -> None:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        # Caso 1: login exitoso
        print("Ejecutando Caso 1: Login...")
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        assert "inventory.html" in driver.current_url
        print("✅ Caso 1 completado con éxito.")

        # Caso 2: agregar un producto al carrito
        print("Ejecutando Caso 2: Agregar producto...")
        boton_agregar = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        boton_agregar.click()

        badge_carrito = driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge"
        ).text
        assert badge_carrito == "1"
        print("✅ Caso 2 completado con éxito.")

        # Caso 3: login fallido con usuario bloqueado
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        error_msg = driver.find_element(
            By.CSS_SELECTOR, '[data-test="error"]'
        ).text
        assert "Sorry, this user has been locked out" in error_msg
        print("✅ Caso 3 completado con éxito.")
    except Exception as error:
        print(f"❌ Error durante la ejecución: {error}")
    finally:
        driver.quit()


if __name__ == "__main__":
    ejecutar_pruebas()
