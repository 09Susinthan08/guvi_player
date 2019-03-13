# your code goes here
q,w=map(int,input().split())
for i in range(w,1000000):
	if(i%q==0 and i%w==0):
		print(i)
		break
	else:
		continue
