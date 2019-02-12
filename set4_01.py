# your code goes here
q=input()
c,d=0,0
for i in q:
	if(i=='('):
		c=c+1
	if(i==')'):
		d=d+1
if(c==d):
	print("yes")
else:
	print("no")
