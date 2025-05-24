import data
import test
import helper
from locators import Locators
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators


    def set_from(self, from_address):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.locators.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.locators.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.request_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_rate(self):
        return self.driver.find_element(*self.locators.comfort_rate_icon)

    def click_on_comfort_rate(self):
        self.get_comfort_rate().click()
        
    def set_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field)).click()
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field_popup)).send_keys(phone_number)
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field_button)).click()

        phone_code = helper.retrieve_phone_code(self.driver)
        wait.until(EC.element_to_be_clickable(Locators.codigo_sms_field)).send_keys(phone_code)
        wait.until(EC.element_to_be_clickable(Locators.Confirmar_button)).click()
        
    def open_payment_method_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.payment_method_button)).click()
        
    def click_agregar_tarjeta(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.agregar_tarjeta_button)).click()
    
    def get_card_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locators.card_number_field))
    
    def set_card_number(self, card_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.card_number_field)).send_keys(card_number)
    
    def get_cvv_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locators.cvv_field))
    
    def set_cvv_number(self, cvv_number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.cvv_field)).send_keys(cvv_number)
        
    def click_agregar_button(self):
        #self.driver.find_element(cvv_field).send_keys(Keys.TAB)
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.agregar_button)).click()
    
    def close_popup_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.close_button_popup)).click()
        
    def set_mensaje_al_conductor(self, message):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.message_for_driver_field)).send_keys(message)
    
    def get_mensaje_al_conductor(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locators.message_for_driver_field)).get_attribute("value")
        
    def click_requisitos_pedido(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.requisitos_button)).click()
        
    def set_manta_y_panuelos(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.manta_y_panuelos_slider)).click()
        
    def get_manta_y_panuelos(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.manta_y_panuelos_slider))
    
    def set_icecream(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.plus_icecream)).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(Locators.plus_icecream)).click()
    
    def click_pedir_un_taxi_final(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(Locators.pedir_un_taxi_last_button)).click()
    


