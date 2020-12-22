import Login
import HastagsFunctions as hf
import PostInteractions as pi
import random 

hashtags=hf.InputHashtags()

comments=hf.InputComments()

com_per_hashtag=0
while com_per_hashtag<=0: #To take input of the number of comments a user wants to put into an hashtag
    com_per_hashtag=int(input("Enter the number of comments you want to post per hashtag : "))

cnt=0
for tag in hashtags:
    hf.HashtagPage(tag)
    hf.sleep(1)
    hf.Opens_First_Recent_Post()    
    for com in range(com_per_hashtag):
        if pi.CommentsOnPost(random.choice(comments)): #Sends random comment from the list
            print("Posting comment "+str(cnt+1)+" on tag "+tag)
            print("Post Link : "+str(hf.driver.current_url))
            cnt+=1
        hf.NextPost()
        hf.sleep(1)

print("Number of comments posted : ",cnt)