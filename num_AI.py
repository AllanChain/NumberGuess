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

def find_same(la,lb):
    same=[]
    for i in la:
        if i in lb:
            same.append(i)
    for i in same:
        la.remove(i)
        lb.remove(i)
    return same,la,lb
def guess(num):
    a,b=judge(num)
    my_posblty=list(combinations(num,a+b))
    for posblty in posblties:
        same,lo,lm=find_same(my_posblty,posblty)

