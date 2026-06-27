from selenium.webdriver.common.by import By
from tests.utils.browser import get_browser


def test_swagger_ui_loads():
    driver = get_browser()

    try:
        driver.get("http://127.0.0.1:8000/docs")

        assert "Swagger UI" in driver.title
        assert driver.find_element(By.TAG_NAME, "body").is_displayed()

    finally:
        driver.quit()