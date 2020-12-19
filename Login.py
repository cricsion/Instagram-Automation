from Open_Browser import driver
import Open_Browser
from time import sleep 
import getpass #Using getpass to hide username and password 

Open_Browser.OpensURL()
print("Your username and password will not be appearing as your are typing the username and password to prevent anyone from knowing your credentials")
username=getpass.getpass("Enter your instagram username : ") #stores username
password=getpass.getpass("Enter your instagram password : ") #stores password
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username) #Sends input in the username field
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(password) #Send input in the password field  
sleep(1)
driver.find_element_by_xpath('//*[text()="Log In"]').click()
print("Signing In...")
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