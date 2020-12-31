import Login
from Open_Browser import driver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

sleep(1)
account_name=input("Enter username of the account whose followers name you want : ")
driver.get('https://www.instagram.com/{}/'.format(account_name)) #Opens Profile page
sleep(5)
try:
    num_of_followers=str(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text)
except:
    print("The account is either private or not in instagram")
    driver.quite()
    exit()
    
num_of_followers=int(num_of_followers.replace(',','').replace('K','000').replace('.','').replace('M','0000000'))
print("The number of followers of instagram account \'"+account_name+"\' is "+str(num_of_followers))

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()#Opens Followers window
sleep(2)

try:  #If the file exists the except block will be executed. The names of the followers are stored in the Followers.txt file.                        
    followers=open('Followers.txt','x')
except FileExistsError:
    followers=open('Followers.txt','w')

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]').click() #followers tab
sleep(2)
action = ActionChains(driver) 
for scroll in range(int(num_of_followers/10)+1):
    action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
    sleep(1)

followerslist=driver.find_element_by_css_selector('.PZuss')
followers_name=followerslist.find_elements_by_css_selector('.Jv7Aj.mArmR.MqpiF') #Scrapes followers from list
for followee in followers_name:
    followers.write(followee.text)
    print(followee.text)
print("All Followers' name has been written to file named Followers.txt in the Folder From Where This Program Has Been Running")
followers.close()