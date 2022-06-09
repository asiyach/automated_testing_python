# from selenium import webdriver
#
# link = "http://selenium1py.pythonanywhere.com/"
# # driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
# # driver.maximize_window()
#
#
# class TestMainPage1:
#
#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..1")
#         # self.driver = webdriver.Chrome()
#         self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
#
#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..2")
#         self.driver.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.setup_class()
#
#         self.driver.get(link)
#         self.driver.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.setup_class()
#
#         self.driver.get(link)
#         self.driver.find_element_by_css_selector(".basket-mini .btn-group > a")
#
# class TestMainPage2:
#
#     def setup_method(self):
#         print("start browser for test..3")
#         self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
#
#     def teardown_method(self):
#         print("quit browser for test..4")
#         self.driver.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.driver.get(link)
#         self.driver.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.driver.get(link)
#         self.driver.find_element_by_css_selector(".basket-mini .btn-group > a")
import pytest
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
