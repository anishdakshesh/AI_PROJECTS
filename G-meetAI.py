import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

# Replace with your Google Meet URL
meet_url = "https://meet.google.com/your-meet-id"

# Replace with your Google account credentials
email = "your-email@gmail.com"
password = "your-password"

# Create a WebDriver instance
driver = webdriver.Chrome()

# Open Google Meet
driver.get(meet_url)

# Sign in to Google
driver.find_element_by_id("identifierId").send_keys(email)
driver.find_element_by_id("identifierNext").click()
time.sleep(2)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("passwordNext").click()
time.sleep(5)  # Allow time for authentication

# Join the meeting
pyautogui.hotkey('ctrl', 'e')  # Mute/unmute microphone
pyautogui.hotkey('ctrl', 'd')  # Turn camera on/off
pyautogui.hotkey('ctrl', 'f')  # Enter/exit full screen

# To exit the meeting (optional)
# pyautogui.hotkey('ctrl', 'w')

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    driver.quit()
