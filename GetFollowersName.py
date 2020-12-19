import Login
from Open_Browser import driver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

sleep(1)
driver.get('https://www.instagram.com/{}/'.format(Login.username)) #Opens Profile page
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
sleep(2)
try:  #If the file exists the except block will be executed                          
    followers=open('Followers.txt','x')
except FileExistsError:
    followers=open('Followers.txt','w')

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]').click()
sleep(2)
action = ActionChains(driver) 
action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform() 