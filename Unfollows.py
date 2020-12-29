import Login
from time import sleep
from Login import driver

driver.get('https://www.instagram.com/{}/'.format(Login.username)) #Opens Profile page
sleep(5)

flag=True
while flag:
    try:
        num_of_unfollows=int(input("Enter the number of people you want to unfollow \n"))
        flag=False
    except ValueError:
        print("Enter the number of unfollows again")

try:
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click() #Opens Following Tab
    print("Opened Following Tab")
    sleep(4)
except:
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        print("Opened Following Tab")
        sleep(4)
    except:
        pass

def Unfollow():
    driver.find_element_by_xpath('//button[text()="Following"]').click()
    sleep(1)
    driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
    sleep(1)

cnt=0

while cnt<=num_of_unfollows:
    Unfollow()
    cnt+=1
    print("Number of people unfollowed : ",cnt)
    
print("Total Number of Accounts Unfollowed : ",cnt)
