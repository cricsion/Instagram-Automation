import Login
import PostInteractions as pi
from Open_Browser import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

account_name=input("Enter the username of the account : ")
driver.get("https://www.instagram.com/{}/".format(account_name)) #Opens profile of the user
pi.sleep(5)

try:
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()#Opens followers tab
    print("Successfully Opened Followers tab")
    pi.sleep(3)
except:
    print("Unable to open Folllowers Tab")

num_of_follows=int(input("Enter the number of accounts you want to follow : "))
cnt=0
timegap=0
while timegap<=0:
    timegap=float(input("Enter the duration of sleep between each follow : "))

driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]').click() #clicks on the follows tab

action = ActionChains(driver) #Used for scrolling   
while True:
    try:
        follow=driver.find_element_by_xpath('//button[text()="Follow"]').click()
        cnt+=1
        pi.sleep(timegap)
    except Exception as e:
        print("Exception : ",e)
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        pi.sleep(6)
