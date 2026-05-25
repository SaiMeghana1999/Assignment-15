from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username_xpath = "//input[@name='username']"
        self.password_xpath = "//input[@name='password']"
        self.login_button_xpath = ("//button[normalize-space()='Login']")

        self.dashboard_xpath = ("//p[@class='oxd-userdropdown-name']")

        self.logout_xpath = ("//a[normalize-space()='Logout']")

    # Enter Username
    def enter_username(self, username):

        username_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_xpath)))
        username_field.clear()
        username_field.send_keys(username)

    # Enter Password
    def enter_password(self, password):

        password_field = self.driver.find_element(By.XPATH,self.password_xpath)
        password_field.clear()
        password_field.send_keys(password)

    # Click Login Button
    def click_login_button(self):

        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    # Verify Successful Login
    def verify_login_success(self):

        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.dashboard_xpath)))

    # Logout Method
    def logout(self):

        self.driver.find_element(By.XPATH,self.dashboard_xpath).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logout_xpath))).click()

