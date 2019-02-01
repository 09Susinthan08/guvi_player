a,b,c=map(str,input().split(" "))
count=0
c=int(c)
for i in range(len(a) and len(b)):
	if(a[i]!=b[i]):
		count=count+1
	else:
		continue
if(count==c):
	print("yes")
else:
	print("no")
