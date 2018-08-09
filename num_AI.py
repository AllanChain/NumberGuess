import random
from itertools import combinations

RANGE=list('123456789')
rest=SEQ=4
posblties=set(tuple())
guess_in=set()
guess_pos=[]
history={}
cnum=random.sample(RANGE,k=SEQ)
def judge(c,u):
    a=b=0
    for i in range(SEQ):
        if c[i]==u[i]:
            a+=1
    for i in c:
        if i in u:
            b+=1
    return a,b-a
def contain(a,b):
    '''To test of two tuples contains'''
    a_set=set(a)
    b_set=set(b)
    if a_set in b_set:
        return (a,b)
    elif b_set in a_set:
        return (b,a)
    else:
        return None,None
def merge(la,lb,subs):
    #if not la:return lb
    #if not lb:return la
    posblty=set()
    for i in la:
        for j in lb:
            p=tuple(set(i)|set(j))
            if not p in subs and len(p)<=rest:
                posblty.add(p)
    return posblty
def clear(l):
    l=list(l)
    removes=set()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            p,c=contain(l[i],l[j])
            if not p is None:
                removes.add(p)
    return set(l)-removes
def history_clear(l):
    for posblty in l.copy():
        for h,r in history.items():
            if len(set(posblty)&set(h))>r[1]:
                l.remove(posblty)
    return l
def calc_posblty(la,lb):
    same=set()
    subs=set()
    exclude=set()
    for i in la:
        for j in lb:
            if i==j:
                same.add(i)
            else:
                p,c=contain(j,i)
                if p is None:
                    continue
                if p in subs:
                    exclude.add(i)
                else:
                    subs.add(p)
    la=la-same-subs
    lb=lb-same-subs
    subs-=exclude
    #print(same,subs,la,lb,merge(la,lb,subs))
    return clear(same|subs|merge(la,lb,subs))
def guess(num):
    global posblties
    a,b=judge(cnum,num)
    history[''.join(num)]=(a,b+a)
    if a+b==rest:
        return False
    my_posblty=set(combinations(num,a+b))
    posblties=calc_posblty(my_posblty,posblties) if posblties else my_posblty
    posblties=history_clear(posblties)
    print(posblties)
    list_posblyties=list(posblties)
    n=random.choice(list_posblyties)
    while len(n)<4:
        n=tuple(set(n)|set(random.choice(list_posblyties)))
    return n[:4]
n=guess(list(str(1234)))
n=guess(list(str(5678)))
rest=history['1234'][1]+history['5678'][1]
print(rest)
for i in range(5):
    n=guess(n)
    if n==False:
        break
print(history)
