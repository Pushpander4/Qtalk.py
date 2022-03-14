import time

import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()


def testQuickTalk_button():
    funtion.click_qtalk()


def test_placeholder_in_QuickTalk():
    place_holder_on_Room_name_lable = funtion.driver.find_element(By.ID, "formBasicEmail").get_attribute("placeholder")
    assert (place_holder_on_Room_name_lable == "Avoid using Spaces ")


def test_checking_text_on_create_quicktalk_button():
    Create_Quicktalk_button = funtion.driver.find_element(By.XPATH,
                                                          "//button[normalize-space()='Create Quicktalk']").text
    assert (Create_Quicktalk_button == "Create Quicktalk")


def test_room_name_lable_text():
    room_name_lable = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Room Name']").text
    assert (room_name_lable == "Room Name")


def test_click_create_quicktalk_button():
    funtion.click_create_quicktalk_button()
