from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pytest import fixture
from page_objects.searchBar import SearchBar
import time


@fixture
def driver():
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=ChromeService(driver_path))
    driver.maximize_window()
    return driver


def test_search(driver):
    driver.get('https://www.expedia.com/Flights')
    search_bar = SearchBar(driver)
    search_bar.activate_leaving_field()
    search_bar.wait_for_popover()
    search_bar.type_origin_destination("Orlando, FL (MCO)")
    #search_bar.wait_for_search_results()
    time.sleep(5)
    # test fails here, because options list infinity loadings due to selenium detection on the original site.
    search_bar.choose_origin_city("Orlando, FL, United States of America (MCO-Orlando Intl.)")
    # I stopped to create the test here, because the website detected and blocked Selenium actions.
