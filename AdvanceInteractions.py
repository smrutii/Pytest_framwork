import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)
driver.maximize_window()

action =  ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(5)
action.double_click(driver.find_element(By.CSS_SELECTOR,"a[id='opentab']")).perform()
#time.sleep(5)

# Mouse Hover

