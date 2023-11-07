from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
URL = os.environ["URL"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="s-1837973528"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(2)
facebook_sign_in = driver.find_element(By.XPATH, '//*[@id="s728612692"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_sign_in.click()

time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

time.sleep(1)
email = driver.find_element(By.CSS_SELECTOR, '#email')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD)
fb_login_button = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
fb_login_button.click()

time.sleep(8)
driver.switch_to.window(driver.window_handles[0])
allow_location_button = driver.find_element(By.XPATH, '//*[@id="s728612692"]/main/div[1]/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(1)
no_notifications_button = driver.find_element(By.XPATH, '//*[@id="s728612692"]/main/div[1]/div/div/div[3]/button[2]')
no_notifications_button.click()

accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="s-1837973528"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies_button.click()

time.sleep(3)
reject_button = driver.find_element(By.XPATH, '//*[@id="s-1837973528"]/div/div[1]/div/main/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
reject_button.click()

for i in range(50):
    time.sleep(3)
    reject_button.click()