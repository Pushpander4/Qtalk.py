import time
import funtion
from selenium.webdriver.common.by import By

def testenter_name_for_qtalk():
    funtion.open_browser()
    funtion.continue_with_Google_button()
    funtion.Click_Qtalk()
    funtion.driver.find_element(By.ID, "formBasicEmail").send_keys("jfhdfhsdbfhsdfbghsd")
    time.sleep(10)
    funtion.click_create_quicktalk_button()
    funtion.home()
    time.sleep(6)

def testClick_on_the_created_card():
    card_elements = funtion.driver.find_elements(By.CLASS_NAME, "card-main ")
    for card_elem in card_elements:
        title_elem = card_elem.find_element(By.CLASS_NAME, "talk--title")
        if title_elem.text == "jfhdfhsdbfhsdfbghsd":
            print(title_elem.text)
            funtion.driver.execute_script("arguments[0].scrollIntoView()", card_elem)
            print(card_elem)
            time.sleep(3)
            card_elem.click()
            time.sleep(10)