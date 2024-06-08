import time
import unittest
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoBlazeTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def test_user_signup_positive(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        signup_button = self.driver.find_element(By.XPATH,"//a[@id='signin2']")
        signup_button.click()
        username_input = self.driver.find_element(By.XPATH,"//input[@id='sign-username']")
        password_input = self.driver.find_element(By.XPATH,"//input[@id='sign-password']")

        username_input.send_keys("12345")
        password_input.send_keys("12345")
        signup_submit_button = self.driver.find_element(By.XPATH,"//button[normalize-space()='Sign up']")
        signup_submit_button.click()
        time.sleep(2)
        print("Signup successful")
    def tearDown(self):
              self.driver.quit()

    def test_user_login_positive(self):
        self.driver.get("https://www.demoblaze.com/")
        login_button = self.driver.find_element(By.XPATH,"//a[@id='login2']")
        login_button.click()

        # Fill out the login form with valid credentials
        username_input = self.driver.find_element(By.XPATH,"//input[@id='loginusername']")
        password_input = self.driver.find_element(By.XPATH,"//input[@id='loginpassword']")

        username_input.send_keys("12345")
        password_input.send_keys("12345")

        login_submit_button = self.driver.find_element(By.XPATH,"//button[text()='Log in']")
        login_submit_button.click()
        time.sleep(2)
        print("Welcome 12345")

    def test_product_browsing(self):
        self.driver.get("https://www.demoblaze.com/index.html#")
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card-block']"))
        )
        self.assertGreater(len(products), 0, "No products are displayed on the homepage")
        print(f"Products on homepage: {len(products)}")
        categories = ["Phones", "Laptops", "Monitors"]
        for category in categories:
            category_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, category))
            )
            category_link.click()
            category_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card-block']"))
            )
            self.assertGreater(len(category_products), 0, f"No products in {category} category")
            print(f"Products in {category} category: {len(category_products)}")
            home_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Home"))
            )
            home_link.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card-block']"))
                    )
    def tearDown(self):
                self.driver.quit()



    def test_add_to_cart(self):
        self.driver.get("https://www.demoblaze.com/")
        product_link = self.driver.find_element(By.XPATH,"//button[@id='next2']")
        product_link.click()

        add_to_cart_button = self.driver.find_element(By.XPATH,"//div[@class='card-block']//a")
        add_to_cart_button.click()
        success_alert = self.driver.find_element(By.XPATH,"//div[@id='tbodyid']")
        self.assertTrue(success_alert.is_displayed())
    

    def test_checkout_process(self):
        self.driver.get("https://www.demoblaze.com/cart.html")
        checkout_button = self.driver.find_element(By.XPATH, "//button[text()='Place Order']")
        checkout_button.click()
        name_input = self.driver.find_element(By.XPATH, "//input[@id='name']")
        name_input.send_keys("Test User")

        country_input = self.driver.find_element(By.XPATH, "//input[@id='country']")
        country_input.send_keys("Test Country")

        city_input = self.driver.find_element(By.XPATH, "//input[@id='city']")
        city_input.send_keys("Test City")

        card_input = self.driver.find_element(By.XPATH, "//input[@id='card']")
        card_input.send_keys("1234567890123456")

        month_input = self.driver.find_element(By.XPATH, "//input[@id='month']")
        month_input.send_keys("12")

        year_input = self.driver.find_element(By.XPATH, "//input[@id='year']")
        year_input.send_keys("24")

        purchase_button = self.driver.find_element(By.XPATH, "//button[@onclick='purchaseOrder()']")
        purchase_button.click()
        success_alert = self.driver.find_element(By.XPATH, "//div[@class='sweet-alert  showSweetAlert visible']")
        self.assertTrue(success_alert.is_displayed())

    def test_logout_process(self):
        self.driver.get("https://www.demoblaze.com/")
        success_message = self.driver.find_element(By.XPATH,"//a[@id='login2']")
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
