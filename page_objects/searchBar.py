from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchBar:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.origin_btn = "button[data-stid='origin_select-menu-trigger']"
        self.origin_popover = "section[data-testid='popover-sheet']"
        self.origin_input = "input[data-stid='origin_select-menu-input']"
        self.search_result = "ul[data-testid='origin_select-results']"
        self.city_origin = "button[aria-label='Orlando (MCO - Orlando Intl.) Florida, United States']"


    # methods
    def activate_leaving_field(self):
        self.driver.find_element(By.CSS_SELECTOR, self.origin_btn).click()


    def wait_for_popover(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.origin_popover)))


    def type_origin_destination(self, destination: str):
        inpt = self.driver.find_element(By.CSS_SELECTOR, self.origin_input)
        inpt.send_keys(destination)


    def wait_for_search_results(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_result)))


    def choose_origin_city(self, destination: str):
        self.driver.find_element(By.CSS_SELECTOR, self.city_origin).click()
        origin_btn_text = self.driver.find_element(By.CSS_SELECTOR, self.origin_input).text
        assert origin_btn_text == destination

