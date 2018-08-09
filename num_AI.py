import random
from itertools import combinations

RANGE=list('123456789')
SEQ=4
posblties=[]
guess_in=[]
guess_pos=[]
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
        return False
def find_same(la,lb):
    same=set()
    subs=[]
    exclude=[]
    for i in la:
        for j in lb:
            if i==j:
                same.add(i)
            elif j in i:
                if j in subs:
                    exclude.append(j)
                    subs.remove(j)
                subs.append(j)
            elif i in j:
                if i in subs:
                    exclude.append(i)
                    subs.remove(i)
                subs.append(j)
    la=la.difference(same)
    lb=lb.difference(same)
    return same,la,lb
def guess(num):
    a,b=judge(num)
    my_posblty=list(combinations(num,a+b))
    for posblty in posblties:
        same,lo,lm=find_same(my_posblty,posblty)

