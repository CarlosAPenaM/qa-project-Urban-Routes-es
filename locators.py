from selenium.webdriver.common.by import By

class Locators:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_rate_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_field = (By.CLASS_NAME, "np_text")
    phone_number_field_popup = (By.ID, "phone")
    phone_number_field_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    siguiente_button = (By.XPATH, "//button[text()='Siguiente']")
    codigo_sms_field = (By.XPATH, "//*[@id='code']")
    confirmar_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By.CSS_SELECTOR, ".pp-button")
    agregar_tarjeta_button = (By.CSS_SELECTOR, ".pp-plus-container")
    card_number_field = (By.ID, "number")
    cvv_field = (By.NAME, "code")
    agregar_button = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")
    close_button_popup = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    message_for_driver_field = (By.ID, "comment")
    requisitos_button = (By.CLASS_NAME, "reqs-head")
    manta_y_panuelos_slider = (
    By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    plus_icecream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
    numero_icecream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    pedir_un_taxi_last_button = (By.CLASS_NAME, "smart-button")