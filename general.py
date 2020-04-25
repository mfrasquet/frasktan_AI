#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:58:01 2020

@author: miguel
"""
import math

def probDice(number):
    if number==2:
        prob=0.0278
    elif number==3:
        prob=0.0556
    elif number==4:
        prob=0.0833
    elif number==5:
        prob=0.1111
    elif number==6:
        prob=0.1389
    elif number==7:
        prob=0.1667
    elif number==8:
        prob=0.1389
    elif number==9:
        prob=0.1111
    elif number==10:
        prob=0.0833
    elif number==11:
        prob=0.0556
    elif number==12:
        prob=.0278
    else:
        prob=0
    return prob

def printHex(tile,lenGrid,h):
    lenGrid=0.5
    h=lenGrid/math.cos(math.radians(30))
    coord1=[tile[1]['coord'][0]+lenGrid,tile[1]['coord'][1]+h*math.sin(math.radians(30))]
    coord2=[tile[1]['coord'][0],tile[1]['coord'][1]+lenGrid]
    coord3=[tile[1]['coord'][0]-lenGrid,tile[1]['coord'][1]+h*math.sin(math.radians(30))]
    coord4=[tile[1]['coord'][0]-lenGrid,tile[1]['coord'][1]-h*math.sin(math.radians(30))]
    coord5=[tile[1]['coord'][0],tile[1]['coord'][1]-lenGrid]
    coord6=[tile[1]['coord'][0]+lenGrid,tile[1]['coord'][1]-h*math.sin(math.radians(30))]
    
    node_coord=[coord1,coord2,coord3,coord4,coord5,coord6]
    
    coordX=[tile[1]['coord'][0]+lenGrid,tile[1]['coord'][0],tile[1]['coord'][0]-lenGrid,tile[1]['coord'][0]-lenGrid,tile[1]['coord'][0],tile[1]['coord'][0]+lenGrid,tile[1]['coord'][0]+lenGrid]
    coordY=[tile[1]['coord'][1]+h*math.sin(math.radians(30)),tile[1]['coord'][1]+lenGrid,tile[1]['coord'][1]+h*math.sin(math.radians(30)),tile[1]['coord'][1]-h*math.sin(math.radians(30)),tile[1]['coord'][1]-lenGrid,tile[1]['coord'][1]-h*math.sin(math.radians(30)),tile[1]['coord'][1]+h*math.sin(math.radians(30))]
    return [coordX,coordY,node_coord]