import pytest
# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

#
@pytest.fixture(scope="function", autouse=True)
def chrome_driver(request):
    # Создание объекта ChromeOptions и добавление опций
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    # Создание объекта ChromeService с использованием ChromeDriverManager
    chrome_service = ChromeService(ChromeDriverManager().install())
    # Создание объекта webdriver.Chrome с передачей options и service
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    request.cls.chrome_driver = driver
    yield driver
    driver.quit()
#
# @pytest.fixture(scope="function", autouse=True)
# def chrome_driver(request):
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()

