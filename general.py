#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:58:01 2020

@author: miguel
"""
import math
from pylab import figure, text
import matplotlib.pyplot as plt
import matplotlib.colors

def colorPlayer(playerID,output):
    color=output['data']['cards'][str(playerID)]['color']
    return color

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

def printHex(tile,lenGrid):
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

def plotID(tiles,ports,nodes,lenGrid):
    for tile in tiles.iterrows():
        text(tile[1]['coord'][0]-0.05,tile[1]['coord'][1]-0.05, tile[1]['id'],size=10, bbox=dict(facecolor='black', alpha=0.2))
        [coordX,coordY,node_coord]=printHex(tile,lenGrid)
        plt.plot(coordX,coordY,color='k')
        for i in range(6):
            text(tile[1]['node_coord'][i][0]-0.05,tile[1]['node_coord'][i][1]-0.05, tile[1]['node_name'][i],size=8, bbox=dict(facecolor='white', alpha=1))
    
    for port in ports.iterrows():
        plt.scatter(port[1]['coord'][0],port[1]['coord'][1],color=port[1]['col'],s=100) 
        for i in range(2):
            plt.plot([port[1]['coord'][0],nodes['coordX'][port[1]['nodes'][i]]],[port[1]['coord'][1],nodes['coordY'][port[1]['nodes'][i]]],color=port[1]['col'])
    
    plt.show()
    
def plotMap(tiles,ports,nodes,lenGrid):
    for tile in tiles.iterrows():
        text_params = {'ha': 'center', 'va': 'center', 'family': 'sans-serif','fontweight': 'bold'}
        text(tile[1]['coord'][0]-0.05,tile[1]['coord'][1]-0.05, tile[1]['num'],color=tile[1]['col'],size=13,**text_params)
        [coordX,coordY,node_coord]=printHex(tile,lenGrid)
        plt.plot(coordX,coordY,color='k')
        
    for port in ports.iterrows():
        plt.scatter(port[1]['coord'][0],port[1]['coord'][1],color=port[1]['col'],s=100) 
        for i in range(2):
            plt.plot([port[1]['coord'][0],nodes['coordX'][port[1]['nodes'][i]]],[port[1]['coord'][1],nodes['coordY'][port[1]['nodes'][i]]],color=port[1]['col'])
    plt.show()
    
def plotMapStructure(tiles,ports,nodes,lenGrid,output):
    for tile in tiles.iterrows():
        text_params = {'ha': 'center', 'va': 'center', 'family': 'sans-serif','fontweight': 'bold'}
        text(tile[1]['coord'][0]-0.05,tile[1]['coord'][1]-0.05, tile[1]['num'],color=tile[1]['col'],size=13,**text_params)
        [coordX,coordY,node_coord]=printHex(tile,lenGrid)
        plt.plot(coordX,coordY,color='k')
        
    for port in ports.iterrows():
        plt.scatter(port[1]['coord'][0],port[1]['coord'][1],color=port[1]['col'],s=100) 
        for i in range(2):
            plt.plot([port[1]['coord'][0],nodes['coordX'][port[1]['nodes'][i]]],[port[1]['coord'][1],nodes['coordY'][port[1]['nodes'][i]]],color=port[1]['col'])
    
    for town in output['data']['towns']:
        if output ['data']['towns'][str(town)]['level']==1:
            plt.scatter(nodes['coordX'][int(town)]+.03,nodes['coordY'][int(town)]+0.05,color=colorPlayer(output ['data']['towns'][str(town)]['ownerId'],output),marker="o",s=80)
        else:
            plt.scatter(nodes['coordX'][int(town)]+.03,nodes['coordY'][int(town)]+0.05,color=colorPlayer(output ['data']['towns'][str(town)]['ownerId'],output),marker="D",s=80)

    for road in output['data']['roads']:
        node1=output['data']['roads'][road]['node1']
        node2=output['data']['roads'][road]['node2']
        plt.plot([nodes['coordX'][node1],nodes['coordX'][node2]],[nodes['coordY'][node1],nodes['coordY'][node2]],color=colorPlayer(output ['data']['roads'][str(road)]['ownerId'],output),linewidth=4)

    plt.show()
    
    
def plotNodeProb(tiles,ports,nodes,lenGrid):
    plt.figure(figsize=(15,8))
    
    cmap = plt.cm.rainbow
    norm = matplotlib.colors.Normalize(vmin=0, vmax=nodes['probTot'].max())
    
    for tile in tiles.iterrows():
        text_params = {'ha': 'center', 'va': 'center', 'family': 'sans-serif','fontweight': 'bold'}
        text(tile[1]['coord'][0]-0.05,tile[1]['coord'][1]-0.05, tile[1]['num'],color=tile[1]['col'],size=13,**text_params)
        [coordX,coordY,node_coord]=printHex(tile,lenGrid)
        plt.plot(coordX,coordY,color='k')
        
    for node in nodes.iterrows():
        if nodes['probTot'][node[0]]>0:
            textProb=str(node[0])+'-'+str(round(100*nodes['probTot'][node[0]],1))+'\n'
            if nodes['probTI'][node[0]]>0:
                textProb=textProb+'TI:'+str(round(100*nodes['probTI'][node[0]],1))+'\n'
            if nodes['probWO'][node[0]]>0:
                textProb=textProb+'WO:'+str(round(100*nodes['probWO'][node[0]],1))+'\n'
            if nodes['probST'][node[0]]>0:
                textProb=textProb+'ST:'+str(round(100*nodes['probST'][node[0]],1))+'\n'
            if nodes['probGR'][node[0]]>0:
                textProb=textProb+'GR:'+str(round(100*nodes['probGR'][node[0]],1))+'\n'
            if nodes['probCL'][node[0]]>0:
                textProb=textProb+'CL:'+str(round(100*nodes['probCL'][node[0]],1))+'\n'
            text(nodes['coordX'][node[0]],nodes['coordY'][node[0]],textProb,size=8, bbox=dict(facecolor=cmap(norm(nodes['probTot'][node[0]])), alpha=.9))

    plt.show()