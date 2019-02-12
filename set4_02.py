# your code goes here
a,b=map(int,input().split(" "))
li=list(map(int,input().split(" ")))
flag=0
for i in li:
	if(i==b):
		flag=1
	else:
		continue
if(flag==1):
	print("Yes")
else:
	print("No")
