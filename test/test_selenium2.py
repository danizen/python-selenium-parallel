import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium2():

    def test_google(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10, 0.1)
        driver.get("http://google.com")
        wait.until(expected_conditions.visibility_of_element_located((By.NAME, "q")))
        search_field = driver.find_element_by_name("q")
        search_field.send_keys("class 2")
        search_field.submit()
        time.sleep(5)
        wait.until(expected_conditions.title_contains("class 2"))
        driver.quit()
        print("class 2 - SUCCESS!\n")
