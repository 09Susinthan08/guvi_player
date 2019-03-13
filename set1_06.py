# your code goes here
q,w=map(str,input().split())
print("yes" if len(set(q))==len(set(w)) else "no")
