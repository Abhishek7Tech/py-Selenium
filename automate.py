from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
element = browser.find_element(By.CLASS_NAME, "form-control")

element.send_keys("HEY THERE COMES THE DAWN!")
# button_1 = browser.find_element(By.CLASS_NAME,"btn-default")
# button.click()

output = browser.find_element(By.ID, "display")

num1 = browser.find_element(By.ID, "sum1")
num1.send_keys("23")

num2 = browser.find_element(By.ID, "sum2")
num2.send_keys("27")

button = browser.find_elements(By.CLASS_NAME, "btn-default")

for i in range(len(button)):
    button[i].click()

total = browser.find_element(By.ID, "displayvalue")
print(output.get_attribute("innerHTML"))
print(total.get_attribute("innerHTML"))    
time.sleep(10)