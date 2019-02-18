def ana():
    w = input("")
    e = w.lower()
    if(len(w) != 6):
        return False
    else:
        if(e.count('a') == 2 and e.count('k') == 1 and e.count('b') == 1 and e.count('l') and e.count('i')):
            return True
        else:
            return False

q=int(input(""))
c = 0
for i in range(q):
    if(ana()):
        c+=1
print(c)
