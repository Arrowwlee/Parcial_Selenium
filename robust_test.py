from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://saucedemo.com"
PASSWORD = "secret_sauce"
WAIT_TIMEOUT = 10


def ejecutar_pruebas() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    try:
        # Caso 1: login seguro
        driver.get(URL)

        user_input = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        user_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        # Caso 2: agregar al carrito con verificación de clic
        btn_add = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )
        btn_add.click()

        badge = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )
        print(f"✅ Prueba exitosa: Carrito tiene {badge.text} producto(s).")

        # Caso 3: validar error de usuario bloqueado
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        error_container = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "h3[data-test='error']")
            )
        )
        print(f"✅ Validación de error correcta: {error_container.text}")
    finally:
        driver.quit()


if __name__ == "__main__":
    ejecutar_pruebas()
