# your code goes here
q=int(input())
w=list(map(int,input().split()))
e={}
for i in w:
	e[i]=0
for i in w:
	e[i]=e[i]+1
for i,j in e.items():
	if j==1:
		print(i)
