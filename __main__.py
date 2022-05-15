from distutils.command.upload import upload
from msilib.schema import Error
import undetected_chromedriver as uc
import requests
import asyncio
import glob, os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
# you dont need all of these, I just like to copy them from previous codes to make my life easier

path = "C:/Program Files (x86)/chromedriver.exe"
list1 = []
path1 = "C:/Users/etomo/OneDrive/Desktop/tiktok-askreddit-main/render/"

def bot():
    options = uc.ChromeOptions()

    options.add_argument("--log-level=3")
    prefs = {"credentials_enable_service": False,
    "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(options=options, executable_path= path)
    driver.get("https://github.com/ErinTomorri")
    driver.set_page_load_timeout(25)
  

    return driver

async def main():

    driver = bot()
    driver.set_window_size(1920, 1080)
    driver.get("https://github.com/ErinTomorri")
    for num in range(10000):
        time.sleep(1) #change this number to increase or decrease wait time before a refresh (in seconds)
        driver.refresh()
    
if __name__ == '__main__':
    asyncio.run(main())
