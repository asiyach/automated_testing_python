import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# CHROME_DRIVER_PATH = 'C:\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


class Test__(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
        self.driver.maximize_window()

    def test_1(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys("puzach")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("asiya")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys("asiya3877@gmail.com")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your phone:']").send_keys("+48632569856")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your address:']").send_keys("Poland")
        self.driver.find_element_by_xpath("/html/body/div/form/button").click()
        variable = self.driver.find_element_by_xpath("/html/body/div/h1").text
        self.assertEqual('Congratulations! You have successfully registered!', variable)




    def test_2(self):
        self.driver.execute_script("window.open('about:blank', 'tab2');")
        self.driver.switch_to.window("tab2")
        self.driver.get("http://suninjuly.github.io/registration2.html")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys("puzach")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("asiya")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys("asiya3877@gmail.com")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your phone:']").send_keys("+48632569856")
        self.driver.find_element_by_xpath("//input[@placeholder='Input your address:']").send_keys("Poland")
        self.driver.find_element_by_xpath("/html/body/div/form/button").click()
        variable = self.driver.find_element_by_xpath("/html/body/div/h1").text
        # self.driver.find_element_by_xpath("//input[@placeholder='Input your name']").send_keys("puzach")
        # self.driver.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys("asiya3877@gmail.com")
        # self.driver.find_element_by_xpath("//input[@placeholder='Input your phone']").send_keys("+48632569856")
        # self.driver.find_element_by_xpath("//input[@placeholder='Input your address']").send_keys("Poland")
        # self.driver.find_element_by_xpath("/html/body/div/form/button").click()
        # variable2 = self.driver.find_element_by_xpath("/html/body/div/h1").text
        self.assertEqual('Congratulations! You have successfully registered!', variable)


if __name__ == "__main__":
    unittest.main()
