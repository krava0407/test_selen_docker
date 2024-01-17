import pytest
from config.data import Data
from pages.contact_details_page import ContactDetailsPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage
from pages.personal_page import PersonalPage


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage
    contact_details_page: ContactDetailsPage
    my_info_page: MyInfoPage

    @pytest.fixture(autouse=True)
    def setup(self, request, chrome_driver):
        request.cls.chrome_driver = chrome_driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(chrome_driver)
        request.cls.dashboard_page = DashboardPage(chrome_driver)
        request.cls.personal_page = PersonalPage(chrome_driver)
        request.cls.contact_details_page = ContactDetailsPage(chrome_driver)
        request.cls.my_info_page = MyInfoPage(chrome_driver)
