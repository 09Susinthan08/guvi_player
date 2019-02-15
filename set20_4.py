# your code goes here
a,b=map(str,input().split(" "))
flag=0
if(a=='R' and b=='P'):
	print("P")
	flag=1
if(a=='P' and b=='S'):
	print("S")
	flag=1
if(a=='S' and b=='R'):
	print("R")
	flag=1
if(flag==0):
	print("D")
