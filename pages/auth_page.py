from .base_page import BasePage
from .locators import AuthLocators

import  time,os


class AuthPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = os.getenv("LOGIN_URL") or "http://petfriends.skillfactory.ru/login"
       driver.get(url)
#создаем нужные элементы
       self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
       self.password = driver.find_element(*AuthLocators.AUTH_PASS)
       self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
       time.sleep(3)

   def enter_email(self, value):
       self.email.send_keys(value)

   def enter_pass(self, value):
       self.password.send_keys(value)

   def btn_click(self):
       self.btn.click()
  time.sleep(3) #ждем реакции