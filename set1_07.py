# your code goes here
a=input()
res=""
for i in range(0,len(a)-1,2):
	res=res+a[i+1]
	res=res+a[i]
print(res)
