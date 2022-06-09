import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
import ipdb;ipdb.set_trace()
ipdb.set_trace()
driver.get("https://opensource-demo.orangehrmlive.com/")
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList/reset/1")

exists = False
try:
    driver.find_element_by_link_text("0345")
    exists = True
except NoSuchElementException:
    pass
if exists:
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployee/empNumber/2")
else:
    create_user = driver.find_element_by_css_selector(".top #btnAdd")
    create_user.click()
    create_user_firstname = driver.find_element_by_css_selector(".formInputText#firstName")
    create_user_firstname.send_keys("Anastasiya")
    create_user_midlename = driver.find_element_by_css_selector(".formInputText#middleName")
    create_user_midlename.send_keys("Asiya")
    create_user_lastname = driver.find_element_by_css_selector(".formInputText#lastName")
    create_user_lastname.send_keys("Dmitriewna")
    create_user_save_bnt = driver.find_element_by_id("btnSave")
    create_user_save_bnt.click()

radio = driver.find_element_by_class_name("radio")
examination_radio = radio.get_attribute("radio")
print("value of sheduled checkbox: ", examination_radio)
if examination_radio is None:
        print("выбора нет")
else:
        print("выбор есть")

select = driver.find_element_by_id("personal_cmbNation")
examination_select = select.get_attribute("personal_cmbNation")
print("value of sheduled checkbox: ", examination_radio)
if examination_select is None:
        print("НЕт")
else:
        print("ЕСТЬ")


# driver.quit()
