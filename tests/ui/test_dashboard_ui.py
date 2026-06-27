from selenium.webdriver.common.by import By
from tests.utils.browser import get_browser


def test_streamlit_dashboard_loads():
    driver = get_browser()

    try:
        driver.get("http://localhost:8501")

        body = driver.find_element(By.TAG_NAME, "body")

        assert body.is_displayed()

    finally:
        driver.quit()