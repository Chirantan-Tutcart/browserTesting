from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

def simulate_user_activity(user_id):
    driver.get("https://dev-video.tutcart.com/join?room=tutorId-6694cf2dd069a9c1abe2eba7-classid-6694e367d069a9c1abe2fd8b-uic-f57c1e10c1&roomPassword=false&audio=true&video=true&screen=false&hide=false&notify=true&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXJuYW1lIiwicGFzc3dvcmQiOiJwYXNzd29yZCIsInByZXNlbnRlciI6InRydWUiLCJpYXQiOjE3MjEwMzM1NzUsImV4cCI6MTc1MjU4NzU3NX0._v2Ym_Lv583nG_WnigAiN3mr9RYfp7ZS-CCvQRaGUks&isPresenter=true") 
    time.sleep(2) 
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "login")

    username_field.send_keys(f"user{user_id}")
    password_field.send_keys("password")  
    login_button.click()

    time.sleep(2)
for user_id in range(1, 101):
    simulate_user_activity(user_id)
    time.sleep(5)
driver.quit()
