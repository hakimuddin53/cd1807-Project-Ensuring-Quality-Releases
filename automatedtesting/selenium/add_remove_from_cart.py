#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime
  

def log_timestamp(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {text}")

def login(driver, user, password):
    log_timestamp('Go to login page.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element("id", "user-name").send_keys(user)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "login-button").click()
    log_timestamp(f"Login with username {user} and password {password} successful")


def add_items_to_cart(driver):
    cart = []

    log_timestamp('Add all items to the cart')

    items = driver.find_elements(By.CLASS_NAME,"inventory_item")
    for item in items:
        item_name = item.find_element(By.CLASS_NAME,"inventory_item_name").text
        cart.append(item_name)
        item.find_element(By.CLASS_NAME,"btn_inventory").click()
        log_timestamp(f'Added {item_name}')
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    log_timestamp("All Items were added to shopping cart.")

def remove_items_to_cart(driver):
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click() 
    cart_items = len(driver.find_elements(By.CLASS_NAME,"cart_item"))

    log_timestamp(f"Number of items in the cart = {cart_items}")

    for item in driver.find_elements(By.CLASS_NAME,"cart_item"):
        item_name = item.find_element(By.CLASS_NAME,"inventory_item_name").text
        item.find_element(By.CLASS_NAME,"cart_button").click()
        log_timestamp(f'Removed {item_name}')

    log_timestamp(f"{cart_items} Items are all removed from shopping cart.")
    

def run_tests():
    """Run the test"""
    log_timestamp("Starting the browser...")
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    log_timestamp('Starting the browser...')
    log_timestamp('Login')
    login(driver, "standard_user", "secret_sauce")
    log_timestamp('Add items')
    add_items_to_cart(driver)
    log_timestamp('Remove items')
    remove_items_to_cart(driver)
    log_timestamp("Tests Completed")

if __name__ == "__main__":
    run_tests()
