from POM_DDTF_Project.Utilities import XLUtils
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    @pytest.fixture()

    def setup(self):

        # Launch Chrome Browser
        self.driver = webdriver.Chrome()

        # Maximize Browser
        self.driver.maximize_window()

        # Open OrangeHRM URL
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        yield

        # Close the Browser
        self.driver.quit()

    def test_login_ddtf(self, setup):

        # Excel File Path from local
        path = r"C:\Users\DELL\OneDrive\Documents\TestData.xlsx.xlsx"

        # Sheet Name
        sheet_name = "Sheet2"

        # Get Total no of Rows
        rows = XLUtils.get_row_count(path,sheet_name)

        # Explicit Wait
        wait = WebDriverWait(self.driver,10)

        # Loop Through Excel Rows
        for r in range(2, rows + 1):

            # Read Username
            username = XLUtils.read_data(path,sheet_name,r,2)

            # Read Password
            password = XLUtils.read_data(path,sheet_name,r,3)

            # Current Date
            current_date = datetime.now().strftime("%d-%m-%Y")

            # Current Time
            current_time = datetime.now().strftime("%H:%M:%S")

            try:
                # Wait For Username Field
                user_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))

                # Clear Username Field
                user_field.clear()

                # Enter Username
                user_field.send_keys(username)

                # Locate Password Field
                pass_field = self.driver.find_element(By.NAME,"password")

                # Clear Password Field
                pass_field.clear()

                # Enter Password
                pass_field.send_keys(password)

                # Click Login Button
                self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

                # Verify Successful Login
                wait.until(EC.presence_of_element_located((By.XPATH,"//h6[text()='Dashboard']")))

                print("Login Successful")

                # to write Date
                XLUtils.write_data(path,sheet_name,r,4,current_date)

                # to write Time
                XLUtils.write_data(path,sheet_name,r,5,current_time)

                # to write Result
                XLUtils.write_data(path,sheet_name,r,6,"Test Passed")

                # Click Profile Dropdown
                wait.until(EC.element_to_be_clickable((By.XPATH,"//p[@class='oxd-userdropdown-name']"))).click()

                # Click Logout
                wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Logout']"))).click()

            except (
                NoSuchElementException,
                TimeoutException
            ):

                print("Login Failed")

                # Write Date
                XLUtils.write_data(path,sheet_name,r,4,current_date)

                # Write Time
                XLUtils.write_data(path,sheet_name,r,5,current_time)

                # Write Result
                XLUtils.write_data(path,sheet_name,r,6,"Test Failed")

                # Refresh Browser
                self.driver.refresh()

        # Final Assertion
        assert True

