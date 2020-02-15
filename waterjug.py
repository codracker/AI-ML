# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:06:45 2020

@author: Muskaan Jain
"""

c=0
res=[]
filled=0
waste=0
result=[]
wastelist=[]
def A(x,y):
    count
    x=4
    count+=1
    
    check(x,y)
def B(x,y):
    global count
    y=3
    count+=1
    check(x,y)
def A_B(x,y):
    global count
    if x+y>=3:
        r=x+y
        x=r-3
        y=3
    else:
        y=x
        x=0
    count+=1
    check(x,y)
    check(x,y)
    
def B_A(x,y):
    global count
    if x+y>=4:
        r=x+y
        y=r-4
        x=4
    else:
        x=y
        y=0
    count+=1
    check(x,y)
def pourA(x,y):
    global count
    global waste
    waste+=x
    r=x
    x=0
    count+=1
    check(x,y)
    waste-=r
def pourB(x,y):
    global count
    global waste
    waste+=y
    r=y
    y=0
    count+=1
    checkanddo(x,y)
    waste-=r
def check(x,y):
    global count
    global c
    global states
    global result
    global res
    global waste
    if (x,y) in states:
        states.append((x,y))
        states.pop(-1)
        pass
    elif x==0 and y==0:
        states.append((x,y))
        count+=1
        A(x,y)
        B(x,y)
        states.pop(-1)
    elif x==1 and y==0:
        states.append((x,y))
        A(x,y)
        B(x,y)
        A_B(x,y)
        pourA(x,y)
        states.pop(-1)
    elif x==2 and y==0:
        states.append((x,y))
        result=copy.deepcopy(states)
        res.append(result)
        wastelist.append(waste)
        c+=1
        states.pop(-1)
    elif x==3 and y==0:
        states.append((x,y))
        A(x,y)
        B(x,y)
        A_B(x,y)
        pourA(x,y)
        states.pop(-1)
    elif x==4 and y==0:
        states.append((x,y))
        B(x,y)
        A_B(x,y)
        pourA(x,y)
        states.pop(-1)
    elif x==0 and y==1:
        states.append((x,y))
        A(x,y)
        B(x,y)
        B_A(x,y)
        pourB(x,y)
        states.pop(-1)
    elif x==1 and y==1:
        states.append((x,y))
        A(x,y)
        B(x,y)
        B_A(x,y)
        A_B(x,y)
        pourA(x,y)
        pourB(x,y)
        states.pop(-1)
    elif x==2 and y==1:
        states.append((x,y))
        pourB(x,y)
        states.pop(-1)
    elif x==3 and y==1:
        states.append((x,y))
        A(x,y)
        B(x,y)
        B_A(x,y)
        A_B(x,y)
        pourA(x,y)
        pourB(x,y)
        states.pop(-1)
    elif x==4 and y==1:
        states.append((x,y))
        B(x,y)
        A_B(x,y)
        pourA(x,y)
        pourB(x,y)
        states.pop(-1)
    elif x==0 and y==2:
        states.append((x,y))
        frBA(x,y)
        states.pop(-1)
    elif x==1 and y==2:
        states.append((x,y))
        fillA(x,y)
        fillB(x,y)
        frBA(x,y)
        frAB(x,y)
        porA(x,y)
        porB(x,y)
        states.pop(-1)
    elif x==2 and y==2:
        states.append((x,y))
        porB(x,y)
        states.pop(-1)
    elif x==3 and y==2:
        states.append((x,y))
        fillA(x,y)
        fillB(x,y)
        frBA(x,y)
        frAB(x,y)
        porA(x,y)
        porB(x,y)
        states.pop(-1)
    elif x==4 and y==2:
        states.append((x,y))
        B(x,y)
        A_B(x,y)
        porA(x,y)
        porB(x,y)
        states.pop(-1)
    elif x==0 and y==3:
        states.append((x,y))
        fillA(x,y)
        frBA(x,y)
        porB(x,y)
        states.pop(-1)
    elif x==1 and y==3:
        states.append((x,y))
        A(x,y)
        B_A(x,y)
        pourA(x,y)
        pourB(x,y)
        states.pop(-1)
    elif x==2 and y==3:
        states.append((x,y))
        porB(x,y)
        states.pop(-1)
    elif x==3 and y==3:
        states.append((x,y))
        A(x,y)
        B_A(x,y)
        pourA(x,y)
        pourB(x,y)
        states.pop(-1)
    elif x==4 and y==3:
        states.append((x,y))
        pourA(x,y) 
        pourB(x,y)
        states.pop(-1)
A,B=0,0
states=list()
count=0
checkanddo(A,B)
print(count)
print(c)
for var in  range(len(res)) :
    print("{}\n liters wasted:{} Liters".format(res[var],wastelist[var]))
print("\n\n\n\n\n")
print(res[wastelist.index(min(wastelist))])
print("Least water wasted:{} liters".format(min(wastelist)))