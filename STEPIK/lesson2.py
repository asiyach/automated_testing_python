# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
# В награду за заполнение формы становится доступен код на скидку.
# Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и ограничив время на ее заполнение.
# Теперь эта задача под силу только роботам ﻿🤖﻿.

from selenium import webdriver
import time

CHROME_DRIVER_PATH = 'C:\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


try:
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements_by_tag_name('input[type="text"]')
    for element in elements:
        element.send_keys("yra")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
