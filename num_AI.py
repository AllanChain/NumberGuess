import random
from itertools import combinations


RANGE=list('123456789')
rest=SEQ=4
posblties=set(tuple())
guess_in=set()
guess_pos=[]
history={}
cnum=random.sample(RANGE,k=SEQ)
#cnum=tuple('5679')

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
    '''merge two swt of possibility under conditionsh'''
    posblty=set()
    for i in la:
        for j in lb:
            p=tuple(set(i)|set(j))
            if not p in subs and len(p)<=rest:
                posblty.add(p)
    return posblty

def clear(l):
    '''除去父集'''
    l=list(l)
    removes=set()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            p,c=contain(l[i],l[j])
            if not p is None:
                removes.add(p)
    return set(l)-removes
def history_clear(l):
    '''根据历史排除'''
    def filt(p):
        for i in guess_in:
            if not i in p:
                return False
        for h,r in history.items():
            if len(set(p)&set(h))!=r[1] or p==h:
                #全对才可
                return False
        return True
    l=set(filter(filt,l))
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
    return clear(same|subs|merge(la,lb,subs))

def guess(num):
    global posblties,rest,guess_in
    a,b=judge(cnum,num)
    history[''.join(num)]=(a,b+a)
    print(''.join(num),b+a)
    if a+b==4:
        guess_in=num
        posblties=history_clear(posblties)
        print('here')
        return False
    elif a+b==rest:
        new_posblties=set()
        for posblty in posblties:
            new_posblties.add(posblty+('9',))
        posblties=new_posblties
        print(posblties)
        rest+=1
        return
    my_posblty=set(combinations(num,a+b))
    posblties=calc_posblty(my_posblty,posblties) if posblties else my_posblty
    posblties=history_clear(posblties)
    if len(posblties)==1:
        posblty=posblties.pop()
        if len(posblties)==4:
            print('only:',posblties)
            #guess(posblties.pop())
            #事实证明唯一可能很靠谱
            return False
    print(posblties,guess_in)
    return b+a

def next_num():
    list_posblyties=list(posblties)
    while True:
        n=random.choice(list_posblyties)
        while len(n)<4:
            n=tuple(set(n)|set(random.choice(list_posblyties)))
        n=history_clear({n[:4]})
        if  n!=set():
            return n.pop()
def analyze_order():
    for h,r in history.items():
        ins=set()
        exs=set()
        pos=set()
        my_pos=set()
        situation=set()
        for n in guess_in:
            if not n in h:continue
            situation.add((n,h.index(n)))
        if len(situation)==r[0]:
            ins|=situation
        elif r[0]==0:
            exs|=situation
        else:
            my_pos=set(combinations(situation,r[0]))
        pos=pos-exs-ins
        pos=calc_posblty(pos,my_pos) if pos else my_pos
    print(ins,exs,pos)

pre=(tuple('1234'),tuple('5678'))
ab=0
flag=True
for p in pre:
    ab+=guess(p)
    print(ab)
    if ab is False:
        flag=False
        break
rest=ab
if rest==3:
    new_posblties=set()
    for posblty in posblties:
        new_posblties.add(posblty+('9',))
    posblties=new_posblties
    print(posblties)
    guess_in.add('9')
    rest+=1
print('rest: ',rest)
print('flag: ',flag)
if flag:
    for i in range(8):
        n=next_num()
        ab=guess(n)
        print('*'*6,ab)
        if ab==False:
            break
print(history,len(history),guess_in)
analyze_order()
