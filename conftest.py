import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def open_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://youthful-shirley-3dacfb.netlify.app/")
    parent_handel = driver.current_window_handle
    print("Title Name", driver.title)
    return driver


