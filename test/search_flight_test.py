from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = set_up_driver()
    driver.get('https://www.expedia.com/Flights')
    search_test(driver)


def set_up_driver():
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=ChromeService(driver_path))
    driver.maximize_window()
    return driver


def search_test(driver):
    origin_btn = driver.find_element(By.CSS_SELECTOR, "button[data-stid='origin_select-menu-trigger']")
    origin_btn.click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "section[data-testid='popover-sheet']")))
    inpt = driver.find_element(By.CSS_SELECTOR, "input[data-stid='origin_select-menu-input']")
    inpt.send_keys("Orlando, FL (MCO)")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[data-testid='origin_select-results']")))
    # test fails here, because options list infinity loadings due to selenium detection on the original site.
    city_origin = driver.find_element(By.CSS_SELECTOR,
                                      "button[aria-label='Orlando (MCO - Orlando Intl.) Florida, United States'")
    city_origin.click()
    origin_btn_text = driver.find_element(By.CSS_SELECTOR, "button[data-stid='origin_select-menu-input']").text
    assert origin_btn_text == "Orlando, FL (MCO)"
    # I stopped to create the test here, because the website detected and blocked Selenium actions.


if __name__ == "__main__":
    main()
