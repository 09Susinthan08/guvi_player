# your code goes here
s=int(input())
li=list(map(int,input().split(' ')))
su=0
for i in li:
	if(i<0):
		su=su+i
	else:
		continue
print(su)
