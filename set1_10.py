s1,s2 = map(str,input().split(" "))
li1=[]
li2=[]
c = 0
if len(s1) != len(s2):
	print("no")
else:
	for i in s1:
		li1.append(i)
	for i in s2:
		li2.append(i)
	for i in range(0,len(li1)):
		if li1[i] == li2[i]:
			break
		else:
			c=c+1
	if c>0:
		print("no")
	else:
		print("yes")
