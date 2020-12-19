import Login
from Open_Browser import driver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

sleep(1)
account_name=input("Enter username of the account whose followers name you want : ")
driver.get('https://www.instagram.com/{}/'.format(account_name)) #Opens Profile page
sleep(2)
try:
    num_of_followers=int(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text)
except:
    print("The account is either private or not in instagram")
print("The number of followers of instagram account \'"+account_name+"\' is "+str(num_of_followers))

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()#Opens Followers window
sleep(2)

try:  #If the file exists the except block will be executed. The names of the followers are stored in the Followers.txt file.                        
    followers=open('Followers.txt','x')
except FileExistsError:
    followers=open('Followers.txt','w')

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]').click() #selects the follower window
sleep(2)
index=1 
followers.write("Hello")
action = ActionChains(driver) 
while num_of_followers>=index:
    try:
        follower_name=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a'.format(index)).text #Scrapes followers from list
        followers.write(follower_name+"\n")
        index+=1
        print(index)
    except:
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        sleep(2)
print("All Followers' name has been written to file named Followers.txt in the Folder From Where This Program Has Been Running")
followers.close()