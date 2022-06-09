import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

CHROME_DRIVER_PATH = 'C:\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
driver.get("http://selenium1py.pythonanywhere.com/ru/")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.mark.regression
def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        driver.get("http://selenium1py.pythonanywhere.com/ru/")
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
