# your code goes here
a,b=map(int,input().split(" "))
i=1
maxi=0
if(a>b):
	m=a
else:
	m=b
for i in range(1,m):
	if(a%i==0 and b%i==0):
		maxi=i
print(maxi)
