from selenium.webdriver.common.by import By
from time import sleep


# Login fields
emailInputID = "email"
passwordInputID = "password"
singInButton = "bg-blue-600"


def Login(browser, email, password): # Login 
    try:
        # Email
        emailField = browser.find_element(By.ID, emailInputID) # Find email input field
        emailField.send_keys(email)
        # Password
        passwordField = browser.find_element(By.ID, passwordInputID) # Find password input field
        passwordField.send_keys(password)
        # Sign in
        signIn = browser.find_element(By.CLASS_NAME, singInButton) # Find sign in button
        signIn.click() # Click sign in button

        sleep(2)
        # Check if login was successful
        if browser.current_url == "https://play.refrag.gg/redeem":
            print("Login successful")
            return True
        else:
            print("Login failed. Please check your email and password")
            return False

    except:
        print("Error: Password or email is wrong or input fields are not found")
        return False



