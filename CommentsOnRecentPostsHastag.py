import Login
from Open_Browser import driver
from time import sleep

hastags=[]
numHastag=0
while numHastag<=0:
    numHastag=int(input("Enter the number of hastags you want to enter "))
print("Enter the hastags")
for x in range(numHastag):
    hastags.append(input("Enter hashtag "+str(x+1)+" : "))
