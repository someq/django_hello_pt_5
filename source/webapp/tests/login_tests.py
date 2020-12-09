from django.test import TestCase, tag
from selenium.webdriver import Chrome


@tag('selenium')
class LoginTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_log_in_as_admin(self):
        self.driver.get('http://localhost:8000/accounts/login/')
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_id('submit').click()
        assert self.driver.current_url == 'http://localhost:8000/'

    def test_login_error(self):
        self.driver.get('http://localhost:8000/accounts/login/')
        self.driver.find_element_by_name('username').send_keys('a')
        self.driver.find_element_by_name('password').send_keys('b')
        self.driver.find_element_by_id('submit').click()
        assert self.driver.current_url == 'http://localhost:8000/accounts/login/'
        error = self.driver.find_elements_by_class_name('error')[0]
        assert error.text == "Please enter a correct username and password. Note that both fields may be case-sensitive."
