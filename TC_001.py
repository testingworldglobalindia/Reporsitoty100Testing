# Import a particular class which we are going to use
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service

path = "D:/Download/chromedriver-win64/chromedriver-win64/chromedriver.exe"

@pytest.fixture()
def start_close_browser():
    global driver
    service = Service(executable_path=path)
    driver = Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.get("https://www.facebook.com")
    driver.back()
    driver.forward()
    driver.refresh()
    yield
    driver.close()

# Create object of Chrome class
def test_login_logout(start_close_browser):
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("HelloWporld")
    driver.find_element(By.NAME,"pass").send_keys("1234567890")
    driver.find_element(By.NAME,"login").click()

#driver.quit()
# print hello  owldr