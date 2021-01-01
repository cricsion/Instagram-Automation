from logging import error
import Login
import PostInteractions as pi
from Open_Browser import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

account_name=input("Enter the username of the account : ")
driver.get("https://www.instagram.com/{}/".format(account_name)) #Opens profile of the user
pi.sleep(5)

try: #finds any follows button on the account page for preventing errors in the later part of the program
    driver.find_element_by_xpath('//button[text()="Follow"]').click()
except:
    pass

try:
    driver.find_element_by_tag_name('a').click()#Opens followers tab
    print("Successfully Opened Followers tab")
    pi.sleep(3)
except:
    print("Unable to open Folllowers Tab \nExiting the program.")
    driver.quit()
    exit()

while True:
    try:
        num_of_follows=int(input("Enter the number of accounts you want to follow : "))
        if num_of_follows<=0:
            print("Number of accounts to be followed should not be less than or equal to 0.\nTry Again.")
        else:
            break
    except ValueError:
        print("You cannot enter a character at this input field. \nTry Again.")
    
cnt=0
timegap=0
while timegap<=0:
    try:
        timegap=float(input("Enter the duration of sleep(in seconds) between each follow(Recommended greater than 30 seconds): "))
        if timegap<=0:
            print("Time duration cannot be less than or equal to 0. \nTry Again.")
    except ValueError:
        print("You cannot enter a letter or a symbol at the input field. \nTry Again.")

driver.find_element_by_css_selector('.isgrP').click() #Clicks on the follows tab
action = ActionChains(driver) #Used for scrolling  
num_of_errors=0 #stores the number of times the program is unable to find follow button or some error occured
while cnt<num_of_follows:
    try:
        follow=driver.find_element_by_xpath('//button[text()="Follow"]').click()
        cnt+=1
        num_of_errors=0 #resets the value of number of errors which occur consecutively to 0
        pi.sleep(timegap)
    except Exception as e:
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform() #scrolls down the followers list
        num_of_errors+=1
        if num_of_errors>50: #Stops the loop whent the number of consecutive errors is greater than 50
            print("Cannot follow any account for consecutively {} times".format(num_of_errors))
            break
        pi.sleep(6)
print("Number of accounts followed: ",cnt)
driver.quit()