import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--useAutomationExtension=false")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
parent_handel = driver.current_window_handle


def open_browser():
    driver.maximize_window()
    driver.get("https://youthful-shirley-3dacfb.netlify.app/")
    print("Title Name", driver.title)

def home():
    driver.find_element(By.XPATH, "//a[normalize-space()='Home']").is_enabled()
    print("Home button Enable=", home)
    HomeText =driver.find_element(By.XPATH, "//a[normalize-space()='Home']").text
    assert (HomeText == "Home")
    driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()

def Click_Qtalk():
    driver.find_element(By.XPATH, "//a[normalize-space()='QTalk']").click()


def continue_with_Google_button():
    driver.find_element(By.XPATH , "//div[@role='button']").click()
    time.sleep(5)
    all_handels = driver.window_handles
    print(all_handels)
    for handle in all_handels :
       if handle !=parent_handel:
           driver.switch_to.window(handle)
           time.sleep(4)
           driver.find_element(By.CSS_SELECTOR , "#identifierId").send_keys("pushpander@buzz4health.com")
           time.sleep(4)
           driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
           time.sleep(4)
           driver.find_element(By.XPATH, "//input[@name='password']").send_keys("buzzhealth4")
           time.sleep(4)
           driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
           time.sleep(4)
    driver.switch_to.window(parent_handel)


def click_create_quicktalk_button():
    driver.find_element(By.XPATH, "//button[normalize-space()='Create Quicktalk']").click()
    time.sleep(5)



