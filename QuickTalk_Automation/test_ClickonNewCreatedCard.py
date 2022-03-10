import test_enter_name_new_qtalk
import funtion


def testclickon_new_created_card():
    card_elements = funtion.driver.find_elements(By.CLASS_NAME, "home-feed")
    print(card_elements)
    for card_elem in card_elements:
        title_elem = card_elem.find_element(By.CLASS_NAME, "card--title")
        if title_elem.text == "Automate quickTalk Created":
            print(title_elem.text)
            funtion.driver.execute_script("arguments[0].scrollIntoView()",card_elem)
            print(card_elem)
            time.sleep(3)
            card_elem.click()
            time.sleep(10)