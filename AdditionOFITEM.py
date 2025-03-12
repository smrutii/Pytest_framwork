import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Shop']").click()

phone_Models = driver.find_elements(By.CSS_SELECTOR,".card-title")

for phone_Model in phone_Models:
    Phone = phone_Model.text
    print(Phone)

    if Phone == "Blackberry":
        driver.find_element(By.XPATH,"(//button[@class='btn btn-info'] )[4]").click()
        driver.execute_script("window.scrollTo(0,0);")
        driver.get_screenshot_as_file("Blackberry.png")



driver.find_element(By.CSS_SELECTOR,"a[class ='nav-link btn btn-primary']").click()

wait = WebDriverWait(driver, 10)
Checkout = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[class='btn btn-success']")))
Checkout.click()

driver.get_screenshot_as_file("Address.png")

driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
Countries = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".suggestions")))
print(f"Found {len(Countries)} countries.")
list_countries=[]
time.sleep(3)
# Loop through each country and process them
for country in Countries:
    # Split the text by newline and remove extra spaces
    countries_in_text = country.text.strip().split('\n')
    for c in countries_in_text:
        list_countries.append(c.strip())

# Print the entire list of countries after the loop
print("List of countries:", list_countries)


# Loop again to find and click on India
for country in list_countries:
    if country.lower() == "india":
        # Use dynamic XPath to locate the specific country element
        country_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='India']"))
        )
        country_element.click()  # Click on "India"
        print(f"Selected country: {country}")
        break
    else:
        print("India not found in the suggestions.")

driver.find_element(By.CSS_SELECTOR,"div[class= 'checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[value= 'Purchase']").click()

success_message = driver.find_element(By.CSS_SELECTOR,".alert-success")
print(success_message.text)
assert "Success" in success_message.text
driver.close()



# Optional: Add a delay to observe the result before closing the browser
time.sleep(5)