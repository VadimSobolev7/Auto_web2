import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    
class AddPostLocators:
    LOCATOR_ADD_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """/html/body/div/main/div/div/form/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_CHECK_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

class OperationsAddPost(BasePage):
    
    def add_post(self):
        logging.info('Adding post')
        add_post_btn = self.find_element(AddPostLocators.LOCATOR_ADD_POST_BTN)
        add_post_btn.click()

    def fill_post_info(self, title=None, description=None, content=None):
        logging.info(f'Filling post info: {title}, {description}, {content}')
        title_field = self.find_element(AddPostLocators.LOCATOR_TITLE)
        #title_field.clear()
        if title:
            title_field.send_keys(title)
        description_field = self.find_element(AddPostLocators.LOCATOR_DESCRIPTION)
        #description_field.clear()
        if description:
            description_field.send_keys(description)
        content_field = self.find_element(AddPostLocators.LOCATOR_CONTENT)
        #content_field.clear()
        if content:
            content_field.send_keys(content)
        btn_create_post = self.find_element(AddPostLocators.LOCATOR_CREATE_POST_BTN)
        btn_create_post.click()

    def check_post(self):
        logging.info('Checking new post')
        time.sleep(1)
        return self.find_element(AddPostLocators.LOCATOR_CHECK_POST).text