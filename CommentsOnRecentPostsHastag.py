import Login
import HastagsFunctions as hf
import PostInteractions as pi
import random 

hashtags=hf.InputHashtags()

comments=hf.InputComments()

com_per_hashtag=0 #Stores the number of comment the program has to post on a specific/certain hastag
while com_per_hashtag<=0: #To take input of the number of comments a user wants to put into an hashtag. Also to prevent users from entering 0 or a number less than 0
    try:
        com_per_hashtag=int(input("Enter the number of comments you want to post per hashtag : "))
    except ValueError: #To catch error if the user enters a charater at the given input field
        print("You have to input a number(an integer) not a character")

cnt=0
for tag in hashtags:
    hf.HashtagPage(tag)#Opens Hastag Page
    hf.sleep(3)
    hf.Opens_First_Recent_Post()  #Opens the first recent post on the given tag  
    for com in range(com_per_hashtag):
        if pi.CommentsOnPost(random.choice(comments)): #Sends random comment from the list
            print("Posting comment "+str(cnt+1)+" on tag "+tag)
            print("Post Link : "+str(hf.driver.current_url))
            cnt+=1
        hf.NextPost()
        hf.sleep(1)

print("Number of comments posted : ",cnt)
hf.driver.quit()