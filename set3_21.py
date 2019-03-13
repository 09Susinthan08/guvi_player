# your code goes here
q,w=map(int,input().split())
a,s=map(int,input().split())
z,x=map(int,input().split())
if(q==a==z):
	print("yes")
elif(w==s==x):
	print("yes")
elif(q==w and a==s and z==x):
	print("yes")
else:
	print("no")
