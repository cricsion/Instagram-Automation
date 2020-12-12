from Open_Browser import driver
import Open_Browser
from time import sleep 

Open_Browser.OpensURL()
username=input("Enter your instagram username : ") #stores username
password=input("Enter you instagram password : ") #stores password
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username) #Sends input in the username field
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(password) #Send input in the password field  
sleep(1)
driver.find_element_by_xpath('//*[text()="Log In"]').click()
sleep(5)
try:
    driver.find_element_by_xpath('//*[text()="Not Now"]').click()
    sleep(2)
except:
    pass

try:
    driver.find_element_by_xpath('//*[text()="Not Now"]').click() #Clicks on Not Now button for notifications
    sleep(2)
except:
    pass