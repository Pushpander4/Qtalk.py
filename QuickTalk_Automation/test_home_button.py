import time

from selenium.webdriver.common.by import By

import funtion

funtion.open_browser()


def test_home_button():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Home']").is_enabled()
    print("Home button Enable=", funtion.home)
    HomeText = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Home']").text
    assert (HomeText == "Home")
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()
