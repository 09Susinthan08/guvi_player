# your code goes here
q,w=map(int,input().split(" "))
li=list(map(int,input().split(" ")))
li1=list(map(int,input().split(" ")))
for i in range(0,len(li1)):
	li.append(li1[i])
	if(i==len(li1)-1):
		print(max(li))
	else:
		print(max(li),end=" ")
