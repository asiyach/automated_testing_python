import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
#import ipdb;ipdb.set_trace()
driver.get("https://www.saucedemo.com/")
login = driver.find_element_by_id("user-name")
login.send_keys("standard_user")
password = driver.find_element_by_id("password")
password.send_keys("secret_sauce")

login_btn = driver.find_element_by_id("login-button")
login_btn.click()
time.sleep(3)

add_button1 = driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
add_button1.click()
add_button2 = driver.find_element_by_id("add-to-cart-sauce-labs-bike-light")
add_button2.click()
add_button3 = driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket")
add_button3.click()

driver.get("https://www.saucedemo.com/cart.html")

items_count = driver.find_elements_by_class_name("cart_item")


if len(items_count) == 6:
    print("В корзине 3 товара")

else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))

driver.quit()
