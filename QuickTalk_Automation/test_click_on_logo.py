import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()


def test_click_on_logo():
    funtion.driver.find_element(By.XPATH, "//img[@alt='Quick Talk Logo']").click()
