# your code goes here
q,w=map(int,input().split())
a=[]
b=[]
c=[]
for i in range(0,1000):
	s=i*i
	a.append(s)
for i in range(q,w+1):
	b.append(i)
for i in a:
	if i in b:
		c.append(i)
print(len(c))
