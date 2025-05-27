from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from selenium import webdriver
from selenium.webdriver import Keys
import locators
from UrbanRoute import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_click_pedir_un_taxi(self):
        self.routes_page.set_phone_number(data.phone_number)
        comfort_icon = self.routes_page.get_comfort_rate().text
        assert "comfort" in comfort_icon

    def test_select_comfort_rate(self):
        self.routes_page.get_comfort_rate()
        comfort_text = "comfort"
        comfort_icon = self.routes_page.get_comfort_rate().text
        assert comfort_text in comfort_icon

    def test_set_phone_number(self):
        value = self.routes_page.set_phone_number(data.phone_number)
        assert data.phone_number == value

    def test_set_payment_method(self):
        self.routes_page.open_payment_method_popup()
        self.routes_page.click_agregar_tarjeta()
        self.routes_page.set_card_number(data.card_number)
        assert self.routes_page.set_card_number(data.card_number).get_property('value') == data.card_number
        self.routes_page.set_cvv_number(data.card_code)
        self.routes_page.get_cvv_field().send_keys(keys.TAB)
        self.routes_page.click_agregar_button()
        self.routes_page.close_popup_payment_method()

    def test_set_mensaje_al_conductor(self):
        self.routes_page.set_mensaje_al_conductor(data.message_for_driver)
        assert self.routes_page.get_mensaje_al_conductor() == data.message_for_driver

    def test_order_manta_y_panuelos(self):
        self.routes_page.set_manta_y_panuelos()
        assert self.routes_page.get_manta_y_panuelos().get_property('checked')

    def test_order_dos_helados(self):
        self.routes_page.set_icecream()
        assert locators.Locators.numero_icecream == 2

    def test_click_pedir_taxi_final(self):
        self.routes_page.click_pedir_un_taxi_final()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()