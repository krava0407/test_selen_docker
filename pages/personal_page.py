import time

from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    BUTTON_SAVE = ("xpath", "//button[@type='submit'][1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name: str):
        with allure.step(f"Change name on {new_name}"):
            first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            # first_name.clear()
            first_name.send_keys(Keys.COMMAND + "A")
            first_name.send_keys(Keys.BACKSPACE)
            first_name.send_keys(new_name)

    @allure.step("Save changes.")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SAVE)).click()

    @allure.step("Changes has been successfully.")
    def is_changes_save(self, new_name):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, new_name))

