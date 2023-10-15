from selenium.webdriver.common.by import By
from time import sleep

# Redeem code fields
codeInputXPATH = "//*[@placeholder='Enter code']"
redeemButtonClass = "mt-3"
popupClass = "text-sm.font-medium.text-red-800"

def TryCodes(browser):

    # Redeem code stats
    codesTried = 0
    codesAlreadyUsed = 0
    codesNotFound = 0
    codesExpired = 0
    codesWorked = 0

    # Redeem code input
    codeInputField = browser.find_element(By.XPATH, codeInputXPATH)
    # Redeem button
    redeemButton = browser.find_element(By.CLASS_NAME, redeemButtonClass)
    redeemButton.click() # Clicking redeem button to show popup
    sleep(2)

    print("Trying out codes:")
    with open("codes.txt", "r") as codes: # Open codes.txt
        for code in codes: # Loop through codes
            code = code.strip()
            
            try:
                # Input code       
                codeInputField.send_keys(code) 

                # Click redeem button
                redeemButton.click()
                sleep(0.5)
                # Popup
                popupText = browser.find_element(By.CLASS_NAME, popupClass).text
                print(code, popupText)
                if popupText == "Not Found":
                    codesNotFound += 1
                elif popupText == "Trial code already used":
                    codesAlreadyUsed += 1
                elif popupText == "Trial code expired":
                    codesExpired += 1
                    
                # Clear codeInputField
                codeInputField.clear()
                codesTried += 1
            except:
                print(f"Unknown error!")

            sleep(0.5)

        codes.close() # Close codes.txt

    return codesTried, codesAlreadyUsed, codesNotFound, codesWorked, codesExpired # Return stats

        
