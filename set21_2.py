# your code goes here
s=input()
li=[]
li1=[]
for i in s:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
		li.append(i)
	else:
		li1.append(i)
for i in range(len(li)):
	print(li[i],end="")
for i in range(len(li1)):
	print(li1[i],end="")
