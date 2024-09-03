from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


def home_input(driver, input_field, input_value):
    input_field = driver.find_element(By.XPATH, input_field)
    print('Element XPATH found')
    input_field.send_keys(input_value)
    print(f'Send input value: {input_value}')
    time.sleep(3)
    input_field.send_keys(Keys.ENTER)


def press_button(driver, input_field):
    press_enter = driver.find_element(By.XPATH, input_field)
    press_enter.send_keys(Keys.ENTER)
