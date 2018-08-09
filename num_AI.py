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
class family:
    def __init__(p,c):
        self.p=p
        self.c=c
        aelf.diff=p.difference(c)
    def __eq__(self,x):
        if isinstance(x,set):
            return self.p==p
        #elif isinstance(x,family
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

