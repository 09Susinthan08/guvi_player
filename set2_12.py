# your code goes here
q,w=map(int,input().split(" "))
li=list(map(int,input().split(' ')))
for i in range(0,w):
	li = [li[-1]] + li[:-1]
print(' '.join(map(str,li)))
