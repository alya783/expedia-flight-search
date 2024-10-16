import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

import time

driver_path = ChromeDriverManager().install()
print(f"driver path: `{driver_path}`")
driver = webdriver.Chrome(service=ChromeService(driver_path))

stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )

driver.maximize_window()
driver.get('https://www.expedia.com/Flights')
time.sleep(0.8 + random.random() * 2)
origin_btn = driver.find_element(By.CSS_SELECTOR,"button[data-stid='origin_select-menu-trigger']")
time.sleep(0.1 + random.random() * 0.5)
origin_btn.click()
time.sleep(0.1 + random.random() * 0.5)
origin_popover = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "section[data-testid='popover-sheet']")))
inpt = driver.find_element(By.CSS_SELECTOR, "input[data-stid='origin_select-menu-input']")
time.sleep(0.8 + random.random() * 2)
for k in "Orlando, FL (MCO)":
        time.sleep(0.1 + random.random() * 0.2)
        inpt.send_keys(k)
option = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[data-testid='origin_select-results']")))
time.sleep(0.8 + random.random() * 2)
city_origin = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Orlando (MCO - Orlando Intl.) Florida, United States'")
city_origin.click()
time.sleep(0.1 + random.random() * 0.2)
origin_btn_text = driver.find_element(By.CSS_SELECTOR, "button[data-stid='origin_select-menu-input']")
print(origin_btn_text)
#assert origin_btn_text == "Orlando, FL (MCO)"

destination_btn = driver.find_element(By.CSS_SELECTOR, "button[data-stid='destination_select-menu-trigger']")
destination_btn.click()
destination_popover = WebDriverWait(driver, 200).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "section[data-testid='popover-sheet']")))
driver.find_element(By.CSS_SELECTOR, "input[data-stid='destination_select-menu-input']").send_keys("New York, NY (JFK)")
time.sleep(3)














