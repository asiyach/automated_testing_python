# Задание: https://stepik.org/lesson/138920/step/11?unit=196194
from selenium import webdriver
import time
CHROME_DRIVER_PATH = 'C:\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

try:
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/registration1.html") #код срабатывает верно
    # driver.get(" http://suninjuly.github.io/registration2.html") #код срабатывает с ошибкой


    input1 = driver.find_element_by_tag_name('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")

    input2 = driver.find_element_by_tag_name('[placeholder="Input your last name"]')
    input2.send_keys("Petrov")

    input3 = driver.find_element_by_tag_name('[placeholder="Input your email"]')
    input3.send_keys("stepik@gmail.com")

    input4 = driver.find_element_by_tag_name('[placeholder="Input your phone:"]')
    input4.send_keys("+48269365856")

    input5 = driver.find_element_by_tag_name('[placeholder="Input your address:"]')
    input5.send_keys("Krakow")

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector(".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
