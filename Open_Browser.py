from selenium import webdriver
from time import sleep

driver=webdriver.Firefox(executable_path='geckodriver.exe')
def OpensURL():
    driver.get('https://www.instagram.com/')
    sleep(5)