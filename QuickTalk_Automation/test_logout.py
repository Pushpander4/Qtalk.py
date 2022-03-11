import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()


def testlogout_button():
    LogOutText = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").text
    assert (LogOutText == "Log out")

