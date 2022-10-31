#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#path and chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#test link as given in the pdf
driver.get("https://todo-list-login.firebaseapp.com/")

#first login
link1 = driver.find_element(By.XPATH, "/html/body/ng-view/div/a[4]")
link1.click()

#try and exception sequence as user logs in, if user doesnt log in program will end
try:
    login = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input"))
    )
except:
    driver.quit()
    print("user didnt enter account")
    exit()

#textfield
typein = driver.find_element(By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input")

#for loop to key in from 1-10 list
for x in range(1,11):
    typein.send_keys(x)
    enter = driver.find_element(By.XPATH, "/html/body/ng-view/div/div[2]/div[2]/button")
    enter.click()

#first logout as stated by instructions
logout = driver.find_element(By.XPATH, "/html/body/ng-view/div/nav/div/ul/li/div/button")
logout.click()

#login sequence 2
link2 = driver.find_element(By.XPATH, "/html/body/ng-view/div/a[4]")
link2.click()

#while waiting for pop to finish loading
try:
    login = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input"))
    )
except:
    driver.quit()
    print("user didnt enter account")
    exit()

#for loop to remove from list 5-10
for x in range(6):
    deletebutton5 = driver.find_element(By.XPATH, "/html/body/ng-view/div/div[3]/div/ul/li[5]/div/div[2]/button")
    deletebutton5.click()
    time.sleep(1)

#pause
time.sleep(10)

#final logout
logout = driver.find_element(By.XPATH, "/html/body/ng-view/div/nav/div/ul/li/div/button")
logout.click()