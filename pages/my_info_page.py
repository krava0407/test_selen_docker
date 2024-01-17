from selenium.webdriver.support import expected_conditions as EC


import allure

from pages.base_page import BasePage


class MyInfoPage(BasePage):

    BUTTON_SAVE = ("xpath", "//button[@type='submit'][1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    @allure.step("Save changes.")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SAVE)).click()

