#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:46:13 2020

@author: miguel
Wining combinations in Catan
"""
import operator
#item =[(id,victory, value)]

longRoad=[2] #Id 0
army=[2] #Id 1
settlement=[1,1,1] #Id 3,4,5 #Only 5 available, 2 already in place
city=[1,1,1,1,1] #Id 5,6,7,8,9 #Additional 1 plus settlement
victoryCard=[1,1,1,1] #Id 10,11,12,13 #Only 4 available

items=[('road',2,0),
       ('army',2,0,),
       ('set',1,0),('set',1,0),('set',1,0),
       ('city',1,0),('city',1,0),('city',1,0),('city',1,0),('city',1,0),
       ('card',1,0),('card',1,0),('card',1,0),('card',1,0)]


def powerSet(items):
    res=[[]]
    for item in items:
        newset=[r+[item] for r in res]
        res.extend(newset)
    return res

sols=powerSet(items)

sols_10=[]
for i in sols:
    count=2
    for element in i:
        count=count+element[1]
    if count==10 or count==11:
        sols_10.append(i)

limit=10
solutions=[]
solutionsFormat=[]
number=0
for i in sols_10:
    count=2
    sett=2
    city=0
    road=0
    army=0
    card=0
    elementsList=[]
    number+=1
    
    for element in i:
        if element[0]=='road':
            road+=1
        if element[0]=='army':
            army+=1
        if element[0]=='card':
            card+=1
        if element[0]=='set':
            sett+=1
        if element[0]=='city':
            city+=1
        if sett>=city:
            count=count+element[1]
            elementsList.append(element)
        else:
            city=city-1
        if count>=10:
            exist=False
            for sol in solutions:
                if ([road,army,sett,city,card]==sol):
                    exist=True
            if exist==False:
                solutions.append([road,army,sett,city,card])
                solutionsFormat.append(elementsList)
            break

#Cost of victories
#Road ->       [5,5,0,0,0] 5 Timb + 5 Brick 
#Army ->       [0,0,5.5,5.5,5.5] 3/(11/20) Wool + 3/(11/20) Ore + 3/(11/20) Wheat
#Settlement -> [3,3,1,1,0] 1 Timber + 1 Brick + 1 Wool + 1 Wheat
#City ->       [0,0,0,2,3]
#Victory ->    [0,0,5,5,5] 1/(4/20) Wool + 1/(4/20) Ore + 1/(4/20) Wheat

cost=[]
for i in solutions:
    costs=[7*i[0]+0*i[1]+4*(i[2]-2)+0*i[3]+0*i[4],
          7*i[0]+0*i[1]+4*(i[2]-2)+0*i[3]+0*i[4],
          0*i[0]+5.5*i[1]+1*(i[2]-2)+0*i[3]+5*i[4],
          0*i[0]+5.5*i[1]+1*(i[2]-2)+2*i[3]+5*i[4],
          0*i[0]+5.5*i[1]+0*(i[2]-2)+3*i[3]+5*i[4]]
    cost.append([i,costs,sum(costs)])