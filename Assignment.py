import time

import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/Smruti/Documents/DriversSelenium/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/#")

driver.implicitly_wait(5)



driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click() #Switching to child window
New_window = driver.window_handles
driver.switch_to.window(New_window[1])

email = (driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text) # getting the email
print(email)


driver.switch_to.window(New_window[0]) # switching to the parent window
driver.find_element(By.ID,"username").send_keys(email) # passing the emailID in username

driver.find_element(By.ID,"password").send_keys("PASSWORD") # passing password


user_type = driver.find_elements(By.XPATH,".//input[@type='radio']")
user_type[0].click()
assert user_type[0].is_selected()  # selecting the radio button

driver.find_element(By.ID,"signInBtn").click() # signing in

error_message = WebDriverWait(driver, 10) # Waiting for the error message to be displayed
error_message.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert")))

msg = driver.find_element(By.CSS_SELECTOR,".alert").text# printing the error message
print(f"The error message is {msg}.")
assert 'Incorrect' in msg

#wait = WebDriverWait(driver,10)

#wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

#print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)




driver.close()