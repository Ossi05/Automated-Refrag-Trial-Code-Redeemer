from selenium import webdriver
from time import sleep
from Login import Login
from TryCodes import TryCodes


# Refrag redeem link
link = "https://play.refrag.gg/redeem"

email = "" # Your email here
password = '' # Your password here



def main():

    browser = webdriver.Chrome() # Open Chrome
    browser.get(link) # Go to the link
    sleep(1)

    loginSuccessful = Login(browser, email, password) # Login
    if not loginSuccessful:
        browser.quit()
        return
    # Try codes
    codesTried, codesAlreadyUsed, codesNotFound, codesWorked, codesExpired = TryCodes(browser)

    print("\nDone!")
    
    print(f"\nCodes tried: {codesTried}")
    print(f"Codes not found: {codesNotFound}")
    print(f"Codes expired: {codesExpired}")
    print(f"Codes already used: {codesAlreadyUsed}")
    print(f"Codes worked: {codesWorked}")
    

    browser.quit()
    exit = input("Press enter to Exit...")
    return
    


if __name__ == "__main__":
    main()




