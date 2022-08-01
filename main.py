
import sys
import os
import string
import random
import clipboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from colorama import Fore, Back, Style
import undetected_chromedriver as uc

# Setting console color
os.system("color 05")

# Domain ending list
tlds = [".tk", ".cf", ".ga", ".gq", ".ml"]

# Starting message

print("""
    
    
                                 __ _       _                     _             
                                / /(_)_ __ | | ____ _ _ __   __ _| |_ ___  _ __ 
                               / / | | '_ \| |/ / _` | '_ \ / _` | __/ _ \| '__|
                              / /__| | | | |   < (_| | | | | (_| | || (_) | |   
                              \____/_|_| |_|_|\_\__,_|_| |_|\__,_|\__\___/|_|   
     

""")

# Obtaining arguments from the user
freenomEmail = str(input("[40;32m[?] Email Address of Freenom Account? (Ex. himag49147@logodez.com): [40;36m"))
print(" ")
freenomPassword = str(input("[40;32m[?] Password of Freenom Account? (Ex. menlikersunited): [40;36m"))
print(" ")
type = str(input("[40;32m[?] Which type of proxy links do you want to create? (Ex. Lucid / Void): [40;36m "))

# Starting undetected_chromedriver 
driver = uc.Chrome()

# Defining wait 
wait = WebDriverWait(driver, 10)

# Defining actions
actions = ActionChains(driver)


# Logging in to Freenom
driver.get("https://my.freenom.com/clientarea.php")
wait.until(expected_conditions.presence_of_element_located((By.NAME, "username")))
driver.find_element_by_name("username").send_keys(freenomEmail)
wait.until(expected_conditions.presence_of_element_located((By.NAME, "password")))
driver.find_element_by_name("password").send_keys(freenomPassword)
actions.send_keys(Keys.ENTER).perform()

# Opening the link
driver.get("https://www.freenom.com/en/index.html?lang=en")

# Creating a random domain name
domainName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 9))) + random.choice(tlds)

# Waiting until the domainname element is loaded and then typing the domainname that we created
wait.until(expected_conditions.presence_of_element_located((By.NAME, "domainname")))
driver.find_element_by_name("domainname").send_keys(domainName)
actions.send_keys(Keys.ENTER).perform()

# Going to the cart page to checkout with our domain
driver.get("https://my.freenom.com/cart.php?a=confdomains&language=english")

# Continuing to the checkout page
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="configure_submit_button"]')))
driver.find_element_by_xpath('//*[@id="configure_submit_button"]').click()

# Checking out with domain
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="mainfrm"]/div[2]/div/label')))
driver.find_element_by_xpath('//*[@id="mainfrm"]/div[2]/div/label').click()
wait.until(expected_conditions.presence_of_element_located((By.ID, "formSubmit")))
driver.find_element_by_id("formSubmit").click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="home"]/div[1]/section[3]/div/div/div/p/a')))
driver.get("https://my.freenom.com/clientarea.php?action=domains")
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".smallBtn.whiteBtn.pullRight")))
driver.find_elements_by_css_selector("a.smallBtn.whiteBtn.pullRight")[0].click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="tabs"]/ul/li[4]/a')))
driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[4]/a').click()  m
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'smallBtn primaryColor')))
dnsURL = driver.current_url
driver.get("https://replit.com/@pyroooTM/LinkanatorEducation#index.html")
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[2]/div/div/div[2]/div/button[1]')))
driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div/div[2]/div/button[1]').click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="modal1val-input"]')))
driver.find_element_by_xpath('//*[@id="modal1val-input"]').send_keys("Linkanator"+domainName)
driver.find_element_by_xpath('//*[@id="modal2val-input"]').send_keys(freenomEmail)
driver.find_element_by_xpath('//*[@id="modal3val-input"]').send_keys(freenomPassword)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'jsx-1932603684 primary')))
driver.find_element_by_class_name('jsx-1932603684 primary').click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[3]/div/div/div[2]/div/button[1]')))
driver.find_element_by_xpath('//*[@id="main-content"]/div[3]/div/div/div[2]/div/button[1]').click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[2]/header/div[2]/button')))
driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/header/div[2]/button').click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[2]/div[1]/div[2]/div/div[5]/div/div/div[2]/div/div/div[2]/span/div/button')))
driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div[1]/div[2]/div/div[5]/div/div/div[2]/div/div/div[2]/span/div/button').click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'css-1wiz4be')))
driver.find_element_by_class_name('css-1wiz4be').click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="132val-input"]')))
driver.find_element_by_xpath('//*[@id="132val-input"]').send_keys(domainName)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'css-1wiz4be')))
driver.find_element_by_class_name('css-1wiz4be')[0].click()
aRecord = clipboard.paste()
driver.find_element_by_class_name('css-1wiz4be')[1].click()
txtRecord = clipboard.paste()
driver.find_element_by_class_name('css-nk85md').click()


