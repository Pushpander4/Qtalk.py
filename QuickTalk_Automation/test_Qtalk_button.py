from selenium.webdriver.common.by import By
import funtion
import time

funtion.open_browser()
time.sleep(5)


def testQuickTalk():
    Qtalk = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='QTalk']").is_enabled()
    print("Qtalk Enable  Butoton is=", Qtalk)
    QtalkText =funtion.driver.find_element(By.XPATH, "//a[normalize-space()='QTalk']").text
    assert (QtalkText == "QTalk")

    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='QTalk']").click()
    time.sleep(5)


