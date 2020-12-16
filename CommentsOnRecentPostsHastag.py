import Login
from Open_Browser import driver
from time import sleep

hastags=[]
numHastag=0
while numHastag<=0:
    numHastag=int(input("Enter the number of hastags you want to enter "))
print("Enter the hastags without space")
for tags in range(numHastag):
    hastags.append(input("Enter hashtag "+str(x+1)+" : "))

numComment=0
while numComment<=0:
    numComment=int(input("Enter the number of hastags you want to enter "))
print("Enter the comments ")
comments=[]
for comment in range(numComment):
    comment.append("Enter comment "+str(x+1)+" : ")

com_per_hastag=int(input("Enter the number of comments you want to post per hastag : "))
