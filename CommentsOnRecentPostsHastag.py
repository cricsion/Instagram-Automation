import Login
from Open_Browser import driver
from time import sleep

hastags=[]
numHastag=0
while numHastag<=0: # To prevent users from inputting number of hastags as less than 0 or equal to 0
    numHastag=int(input("Enter the number of hastags you want to enter : "))
print("Enter the hastags without space")
for tags in range(numHastag): #Takes input of hastags 
    hastags.append(input("Enter hashtag "+str(tags+1)+" : "))

numComment=0
while numComment<=0: #Same reason as in line 7
    numComment=int(input("Enter the number of comments you want to enter : "))
print("Enter the comments ")
comments=[]
for comment in range(numComment): #Takes input of the comments the user wants to comment on post
    comments.append(input("Enter comment "+str(comment+1)+" : "))

def Opens_First_Recent_Post(): #Opens First Recent Post at the time
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div').click()
    sleep(2)

def NextPost():
    driver.find_element_by_xpath('//*[text()="Next"]').click()
    sleep(1)

com_per_hastag=0
while com_per_hastag<=0: #To take input of the number of comments a user wants to put into an hashtag
    com_per_hastag=int(input("Enter the number of comments you want to post per hastag : "))

for tag in hastags:
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
    Opens_First_Recent_Post()
    NextPost()
    #for com in range(com_per_hastag):

