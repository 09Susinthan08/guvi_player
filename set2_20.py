# your code goes here
q=input()
li=[]
li1=[]
for i in q:
	li.append(i)
for i in li:
	s=ord(i)+3
	li1.append(chr(s))
print(''.join(li1))
