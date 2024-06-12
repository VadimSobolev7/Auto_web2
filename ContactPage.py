import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

class ContactFormLocators:
    LOCATOR_CONTACT_BTN = (By.XPATH, "/html/body/div[1]/main/nav/ul/li[2]/a")
    LOCATOR_NAME_FIELD = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[1]/label/input")
    LOCATOR_EMAIL_FIELD = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[2]/label/input")
    LOCATOR_CONTENT_FIELD = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[3]/label/span/textarea")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[4]/button")

class OperationsContactForm(BasePage):

    def contact_form_open(self):
        logging.info('Contact form opening')
        contact_form_open_btn = self.find_element(ContactFormLocators.LOCATOR_CONTACT_BTN)
        contact_form_open_btn.click()

    def fill_contact_form(self, name, email, content):
        logging.info(f'Filling contact form: {name}, {email}')
        name_field = self.find_element(ContactFormLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys(name)
        email_field = self.find_element(ContactFormLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        content_field = self.find_element(ContactFormLocators.LOCATOR_CONTENT_FIELD)
        content_field.send_keys(content)
        btn_contact_us = self.find_element(ContactFormLocators.LOCATOR_CONTACT_US_BTN)
        logging.info('Contact btn click')
        time.sleep(1)
        btn_contact_us.click()

    def check_text_alert(self):
        logging.info('Checking alert text')
        time.sleep(2)
        alert = self.driver.switch_to.alert
        return alert.text