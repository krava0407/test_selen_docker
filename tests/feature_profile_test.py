import random

import allure
import pytest

from base.base_test import BaseTest


@allure.feature("Profile functionality")
class TestProfileFuture(BaseTest):

    new_name = f"{random.randint(1, 100)}"

    @allure.title("Change profile name.")
    @allure.severity("Critical.")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(login=self.data.LOGIN)
        self.login_page.enter_password(password=self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(self.new_name)
        self.personal_page.click_save_button()
        self.personal_page.is_changes_save(self.new_name)
        self.personal_page.make_screenshot("Final result")
