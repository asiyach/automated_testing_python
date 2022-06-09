import math
from selenium import webdriver
import time

CHROME_DRIVER_PATH = 'C:\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

try:
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/find_link_text")
    input11 = driver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    input11.click()

    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")

    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")

    input6 = driver.find_element_by_class_name("city")
    input6.send_keys("Smolensk")

    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    # browser.quit()

# не забываем оставить пустую строку в конце файла


