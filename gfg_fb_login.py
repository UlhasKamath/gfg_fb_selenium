#import required modules
from selenium import webdriver 
from selenium.webdriver.common.by import By
from getpass import getpass
from time import sleep

#take user input for fb credentials
email = input('Enter the email: ')
pwd = getpass('Enter the password: ')

#initiate driver object
driver = webdriver.Chrome()
driver.get('https://www.geeksforgeeks.org/')
driver.maximize_window()

#access sign in button
login_button = driver.find_element(By.XPATH, '//*[@id="userProfileId"]/a')
login_button.click()
sleep(2)

#choose fb as the method to login
login_fb = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div/div[2]/div[1]/div/div[3]')
login_fb.click()
sleep(2)

#control moves to different window so we need to switch
handles = driver.window_handles
for i in handles:
    driver.switch_to.window(i)

#send user email as input
fb_login_email = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_login_email.send_keys(email)

#send user pass as input
fb_login_pwd = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_login_pwd.send_keys(pwd)

#login
fb_login_click = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
fb_login_click.click()

#move to python page
python_page = driver.find_element(By.LINK_TEXT, 'Python')
python_page.click()