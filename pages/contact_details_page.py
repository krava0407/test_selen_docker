import random

from selenium.webdriver import Keys

from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

from pages.my_info_page import MyInfoPage


class ContactDetailsPage(MyInfoPage):

    PAGE_URL = Links.CONTACT_DETAILS_PAGE

    CONTACT_DETAILS_BUTTON = ("xpath", "//a[text()='Contact Details']")
    STREET_1_FIELD = ("xpath", "//label[text()='Street 1']/../following-sibling::div//input")
    STREET_2_FIELD = ("xpath", "//label[text()='Street 2']/../following-sibling::div//input")
    CITY_FIELD = ("xpath", "//label[text()='City']/../following-sibling::div//input")
    STATE_FIELD = ("xpath", "//label[text()='State/Province']/../following-sibling::div//input")
    ZIP_POSTAL_FIELD = ("xpath", "//label[text()='Zip/Postal Code']/../following-sibling::div//input")
    COUNTRY_DROPDOWN = ("xpath", "//label[text()='Country']/../following-sibling::div")
    CUSTOM_COUNTRY = ("xpath", "//div[@role='listbox']//span[text()='{0}']")
    COUNTRY_TABLE = ("xpath", "//div[@role='listbox']//span")

    @allure.step(f"Click on my info page.")
    def click_contact_details_link(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_DETAILS_BUTTON)).click()

    @allure.step(f"Enter street 1.")
    def enter_street_1(self, street_name: str):
        with allure.step(f"Change street 1 on {street_name}"):
            el_street = self.wait.until(EC.element_to_be_clickable(
                self.STREET_1_FIELD))
            el_street.send_keys(Keys.COMMAND + "A")
            el_street.send_keys(Keys.BACKSPACE)
            el_street.send_keys(street_name)

    @allure.step(f"Enter street 2.")
    def enter_street_2(self, street_name: str):
        with allure.step(f"Change street 2 on {street_name}"):
            el_street = self.wait.until(EC.element_to_be_clickable(
                self.STREET_2_FIELD))
            el_street.send_keys(Keys.COMMAND + "A")
            el_street.send_keys(Keys.BACKSPACE)
            el_street.send_keys(street_name)

    @allure.step(f"Enter city.")
    def enter_city(self, city_name: str):
        with allure.step(f"Change city on {city_name}"):
            el_street = self.wait.until(EC.element_to_be_clickable(
                self.CITY_FIELD))
            el_street.send_keys(Keys.COMMAND + "A")
            el_street.send_keys(Keys.BACKSPACE)
            el_street.send_keys(city_name)

    @allure.step(f"Enter country.")
    def enter_country(self, country_name: str = None):
        with allure.step(f"Change country on {country_name}"):
            self.wait.until(EC.element_to_be_clickable(
                self.COUNTRY_DROPDOWN)).click()
            self.wait.until(EC.visibility_of_element_located(
                self.COUNTRY_TABLE))
            if not country_name:
                country_names_el_list = self.driver.find_elements(
                    *self.COUNTRY_TABLE)
                text_names_countres = []
                for el in country_names_el_list:
                    text_names_countres.append(el.text)
                country_name = random.choice(text_names_countres)
            country_el = self.driver.find_element(self.CUSTOM_COUNTRY[0],
                    self.CUSTOM_COUNTRY[1].format(country_name))
            self.action.move_to_element(country_el)
            self.wait.until(EC.element_to_be_clickable(country_el)).click()

    @allure.step("Wait download spinner.")
    def wait_spinner(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))

