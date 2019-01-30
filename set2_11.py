# your code goes here
f=input()
holi={'Sunday',"Saturday"}
flag=0
for i in holi:
	if(f==i):
		flag=1
	else:
		continue
if(flag>0):
	print("yes")
else:
	print("no")
