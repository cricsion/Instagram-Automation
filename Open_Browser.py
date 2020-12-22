from urllib.parse import urlunparse
from selenium import webdriver
from time import sleep

try:
    driver=webdriver.Firefox(executable_path='geckodriver.exe')
except:
    try:
        driver=webdriver.Edge(executable_path='msedgedriver.exe')
    except:
        try:
            driver=webdriver.Chrome(executable_path="chromedriver.exe")
        except:
            print("You don't have a compatible browser. \n You should Download/Update Firefox(Recommended), Microsoft Edge or Google Chrome.")

def OpensURL(url):
    driver.get(url)
    sleep(5)