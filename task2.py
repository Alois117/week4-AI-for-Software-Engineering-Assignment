# login_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize browser
driver = webdriver.Chrome()

# Go to login page
driver.get("https://example.com/login")  # Replace with your login page URL

# ---- Test 1: Valid Credentials ----
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.ID, "login-button")

username.clear()
password.clear()
username.send_keys("validuser")
password.send_keys("validpass")
login_button.click()

time.sleep(2)  # Wait for page to load

if "dashboard" in driver.current_url:
    print("✅ Valid login test: PASSED")
else:
    print("❌ Valid login test: FAILED")

# ---- Test 2: Invalid Credentials ----
driver.get("https://example.com/login")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.ID, "login-button")

username.clear()
password.clear()
username.send_keys("invaliduser")
password.send_keys("wrongpass")
login_button.click()

time.sleep(2)

error_msg = driver.find_element(By.CLASS_NAME, "error").text
if "Invalid" in error_msg:
    print("✅ Invalid login test: PASSED")
else:
    print("❌ Invalid login test: FAILED")

driver.quit()
