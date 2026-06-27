from selenium import webdriver


def get_browser():
    options = webdriver.ChromeOptions()

    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)