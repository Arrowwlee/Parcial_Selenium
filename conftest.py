
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura una pantalla automáticamente cuando una prueba falla."""

    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        # Comprobar si la prueba utiliza la fixture driver
        driver = item.funcargs.get("driver")

        if driver is not None:
            try:
                screenshot = driver.get_screenshot_as_base64()

                html = (
                    '<div><img '
                    f'src="data:image/png;base64,{screenshot}" '
                    'alt="screenshot" '
                    'style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" '
                    'align="right"/></div>'
                )

                extras.append(pytest_html.extras.html(html))

            except Exception as error:
                print(f"No se pudo tomar la captura: {error}")

    report.extras = extras


@pytest.fixture
def driver():
    """Configura el navegador para cada prueba."""

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()
