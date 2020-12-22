import Login
from time import sleep
import HastagsFunctions as hf
import PostInteractions as pi
hashtags=hf.InputHashtags()
likes_per_hashtag=0
while likes_per_hashtag<=0: #To take input of the number of comments a user wants to put into an hashtag
    likes_per_hashtag=int(input("Enter the number of likes you want per hashtag : "))
cnt=0
for tag in hashtags:
    hf.driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
    sleep(1)
    hf.Opens_First_Recent_Post()    
    for like in range(likes_per_hashtag):
        if pi.LikesPost():
            print("Liked Post : "+str(hf.driver.current_url))
            cnt+=1
        print("Posted comment ",str(like+1)," on tag ",tag)
        hf.NextPost() #Goes to next Post
        sleep(1)

print("Number of Posts Liked : ",cnt)

