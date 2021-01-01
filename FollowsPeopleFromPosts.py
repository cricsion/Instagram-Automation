import Login
import PostInteractions as pi
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from Open_Browser import driver
print("This program will run on posts with only images")
post_url=input("Enter the URL of the post: \n")
driver.get(post_url)
pi.sleep(5)
try: #clicks on the follow button if there exists before opening the likes panel to avoid errors
    driver.find_element_by_xpath('//button[text()="Follow"]').click()
    pi.sleep(2)
except :
    pass

try:#For posts when you directly open it
    num_of_likes=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button/span').text
except:#For posts like in hastags
    try:
        num_of_likes=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button/span').text
    except:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div') #tries to locate the view count
            print("The media content of the post is a video.")
        except:
            print("The URL is incorrect")
        finally:
            print("Sorry the program cannot be successfully executed.")
            driver.quit()
            exit() #To end the program instantly
  
num_of_likes=str(num_of_likes).replace(',','').replace('K','000').replace('.','').replace('M','0000000')

if pi.OpensLikesPanel():
    print("Opened Likes Panel")
else:
    print('Unable to Open Likes Panel')

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]').click() #clicks on the likes panel
timeduration=0
while timeduration<=0:
    try:
        timeduration=float(input("Enter the time duration (Recommended 5 or greater for the safety of your account) between each follow: "))
        if timeduration==0:
            print("Time duration cannot be 0.")
    except ValueError:
        print("You cannot enter a character. You have to enter time in integer or a fractional number \n Try Again")
    
numFollows=0
while numFollows>int(num_of_likes) or numFollows<=0: #to prevent user from entering a number greater than the number of likes or numFollows less than or equal to 0
    try:
        numFollows=int(input("Enter the number of people you want to follow: "))
        if numFollows>int(num_of_likes):
            print("You cannot enter a number greater than the number of likes on this post.")
        else:
            break
    except ValueError:
        print("You cannot enter a fractional number or a character in the input field. \n Try Again.")

action = ActionChains(driver)
cnt=0
for follow in range(numFollows):
    try:
        driver.find_element_by_xpath('//button[text()="Follow"]').click()#clicks on the follow button
        cnt+=1 #increases the counter by 1
        print("Followed {} Account".format(cnt))
        pi.sleep(timeduration) #the program stops for the prescribed time limit
    except:
        action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()#used to scroll down 
        pi.sleep(5)
    if cnt==30:
        pi.sleep(300) #sleeps for 300 seconds after a set of 30 follows
print("Number of accounts followed: ",cnt)
print("Program was successfully executed.")
driver.quit()