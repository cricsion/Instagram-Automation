import Login
from time import sleep
import HastagsFunctions as hf
import random 
from Open_Browser import driver

hashtags=hf.InputHashtags()

comments=hf.InputComments()

com_per_hashtag=0
while com_per_hashtag<=0: #To take input of the number of comments a user wants to put into an hashtag
    com_per_hashtag=int(input("Enter the number of comments you want to post per hashtag : "))

for tag in hashtags:
    hf.HashtagPage(tag)
    sleep(1)
    hf.Opens_First_Recent_Post()    
    for com in range(com_per_hashtag):
        print("Posted comment ",str(com+1)," on tag ",tag)
        print("Post Link : "+str(driver.current_url))
        hf.CommentsOnPost(random.choice(comments))
        hf.NextPost()
        sleep(1)


