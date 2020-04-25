#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:42:09 2020

@author: miguel
"""

import requests
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
import pandas as pd
import math
from pylab import figure, text

#My libs
from layerStructure import createNodeM,fillProbNodeM
from board import tileCreation


#Load credentials
credentials=pd.read_csv('../credentials.csv')
username=credentials['username'][0]
pwd=credentials['pwd'][0]

#List of actions
createGame={"reqType":"createGame","data":{"0":1,"1":2,"2":3,"3":5},"username":username,"pwd":pwd}
giveResources={"reqType":"giveResources","data":{"res":{"1":{"gr":0,"wo":0,"ti":0,"cl":0,"st":0},"2":{"gr":0,"wo":2,"ti":4,"cl":-2,"st":0},"3":{"gr":0,"wo":0,"ti":0,"cl":-1,"st":4},"5":{"gr":0,"wo":0,"ti":0,"cl":0,"st":0}},"route":4,"army":2},"username":username,"pwd":pwd}
dice={"reqType":"throwDices","username":username,"pwd":pwd}
editMap_road={"reqType":"editMap","data":{"user":3,"type":"ro","node1":12,"node2":13},"username":username,"pwd":pwd}
editMap_town={"reqType":"editMap","data":{"user":2,"type":"tow","node1":34,"node2":""},"username":username,"pwd":pwd}
throwDices={"reqType":"throwDices","username":username,"pwd":pwd}
makeOffer={"reqType":"makeOffer","data":{"usersOffered":[1,0,1,1,1,0,0],"resourcesOffered":[0,0,2,0,0],"resourcesRequested":[1,0,0,2,0]},"username":username,"pwd":pwd}
#"usersOffered":[1,0,1,1,1,0,0] (1=> nada, 0 => jug1,1=>2,
cancelOffer={"reqType":"cancelOffer","username":username,"pwd":pwd}
acceptOffer={"reqType":"acceptOffer","data":2,"username":username,"pwd":pwd}
makePurchase={"reqType":"makePurchase","data":[2,0,0,0],"username":username,"pwd":pwd}
useCard={"reqType":"useCard","data":{"card":"kn_c","resource":""},"username":username,"pwd":pwd}
moveThief={"reqType":"moveThief","data":2,"username":username,"pwd":pwd}
useThief={"reqType":"useThief","data":2,"username":username,"pwd":pwd}
finishTurn={"reqType":"finishTurn","username":username,"pwd":pwd}
pauseGame={"reqType":"pauseGame","username":username,"pwd":pwd}
resumeGame={"reqType":"resumeGame","username":username,"pwd":pwd}
refresh={"reqType":"refresh","username":username,"pwd":pwd}

#API call
r = requests.post('http://juatan.cosasdejuan.es/juatanApi.php', json=refresh)
r.status_code
output=r.json()

#Create tiles and ports with info from game
[tiles,ports,nodes]=tileCreation(output)


             


def colorPlayer(playerID,output):
    color=output['data']['cards'][str(playerID)]['color']
    return color
        
def strucPrint(output,nodeDict):

    for town in output['data']['towns']:
        if output ['data']['towns'][str(town)]['level']==1:
            plt.scatter(nodeDict[int(town)][0]+.03,nodeDict[int(town)][1]+0.05,color=colorPlayer(output ['data']['towns'][str(town)]['ownerId'],output),marker="o",s=80)
        else:
            plt.scatter(nodeDict[int(town)][0]+.03,nodeDict[int(town)][1]+0.05,color=colorPlayer(output ['data']['towns'][str(town)]['ownerId'],output),marker="D",s=80)
    
    for road in output['data']['roads']:
        node1=output['data']['roads'][road]['node1']
        node2=output['data']['roads'][road]['node2']
        plt.plot([nodeDict[node1][0],nodeDict[node2][0]],[nodeDict[node1][1],nodeDict[node2][1]],color=colorPlayer(output ['data']['roads'][str(road)]['ownerId'],output),linewidth=4)


def printHex(tile,lenGrid,h):
    lenGrid=0.5
    h=lenGrid/math.cos(math.radians(30))
    coord1=[tile['coord'][0]+lenGrid,tile['coord'][1]+h*math.sin(math.radians(30))]
    coord2=[tile['coord'][0],tile['coord'][1]+lenGrid]
    coord3=[tile['coord'][0]-lenGrid,tile['coord'][1]+h*math.sin(math.radians(30))]
    coord4=[tile['coord'][0]-lenGrid,tile['coord'][1]-h*math.sin(math.radians(30))]
    coord5=[tile['coord'][0],tile['coord'][1]-lenGrid]
    coord6=[tile['coord'][0]+lenGrid,tile['coord'][1]-h*math.sin(math.radians(30))]
    
    node_coord=[coord1,coord2,coord3,coord4,coord5,coord6]
    
    coordX=[tile['coord'][0]+lenGrid,tile['coord'][0],tile['coord'][0]-lenGrid,tile['coord'][0]-lenGrid,tile['coord'][0],tile['coord'][0]+lenGrid,tile['coord'][0]+lenGrid]
    coordY=[tile['coord'][1]+h*math.sin(math.radians(30)),tile['coord'][1]+lenGrid,tile['coord'][1]+h*math.sin(math.radians(30)),tile['coord'][1]-h*math.sin(math.radians(30)),tile['coord'][1]-lenGrid,tile['coord'][1]-h*math.sin(math.radians(30)),tile['coord'][1]+h*math.sin(math.radians(30))]
    return [coordX,coordY,node_coord]

#Plot maps
    

#ID
nodeDict_key=[]
nodeDict_coord=[]

for tile in tiles:
    text(tile['coord'][0]-0.05,tile['coord'][1]-0.05, tile['id'],size=10, bbox=dict(facecolor='black', alpha=0.2))
    [coordX,coordY,node_coord]=printHex(tile,lenGrid,h)
    tile['node_coord']=node_coord
    plt.plot(coordX,coordY,color='k')
    for i in range(6):
        text(tile['node_coord'][i][0]-0.05,tile['node_coord'][i][1]-0.05, tile['node_name'][i],size=8, bbox=dict(facecolor='white', alpha=1))
        nodeDict_key.append(tile['node_name'][i])
        nodeDict_coord.append([tile['node_coord'][i][0]-0.05,tile['node_coord'][i][1]-0.05])

nodeDict=dict(zip(nodeDict_key, nodeDict_coord))
plt.show()

for port in ports:
    plt.scatter(port['coord'][0],port['coord'][1],color=port['col'],s=100) 
    for i in range(2):
        plt.plot([port['coord'][0],nodeDict[port['nodes'][i]][0]],[port['coord'][1],nodeDict[port['nodes'][i]][1]],color=port['col'])

#RESOURCES
for tile in tiles:
    text_params = {'ha': 'center', 'va': 'center', 'family': 'sans-serif','fontweight': 'bold'}
    text(tile['coord'][0]-0.05,tile['coord'][1]-0.05, tile['num'],color=tile['col'],size=13,**text_params)
    [coordX,coordY,node_coord]=printHex(tile,lenGrid,h)
    plt.plot(coordX,coordY,color='k')


strucPrint(output,nodeDict)
plt.show()


layers['probTI']=np.zeros(54)
layers['probWO']=np.zeros(54)
layers['probST']=np.zeros(54)
layers['probGR']=np.zeros(54)
layers['probCL']=np.zeros(54)

node={}
#Probaility matrix
for tile in tiles:
    prob_res=[]
    for i in tile['node_name']:
        if tile['res']=='ti':
            layers.loc[i,'probTI'] =layers.loc[i,'probTI'] +tile['prob']
        elif tile['res']=='wo':
            layers.loc[i,'probWO']=layers.loc[i,'probWO']+tile['prob']
        elif tile['res']=='st':
            layers.loc[i,'probST']=layers.loc[i,'probST']+tile['prob']
        elif tile['res']=='gr':
            layers.loc[i,'probGR']=layers.loc[i,'probGR']+tile['prob']
        elif tile['res']=='cl':
            layers.loc[i,'probCL']=layers.loc[i,'probCL']+tile['prob']
        else:
            pass

layers['probTot']=layers.sum(axis=1)

for town in output['data']['towns']:
    layers.loc[int(town),'probTot']=0
    for nodeC in layers['nodeConnexions'][int(town)]:
        layers.loc[nodeC,'probTot']=0

#ID
nodeDict_key=[]
nodeDict_coord=[]

plt.figure(figsize=(15,8))

cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=0, vmax=layers['probTot'].max())
probMon=layers.sum(axis=0)
print(probMon)
for tile in tiles:
    text(tile['coord'][0]-0.05,tile['coord'][1]-0.05, tile['num'],color=tile['col'],size=13,**text_params)
    
    [coordX,coordY,node_coord]=printHex(tile,lenGrid,h)
    tile['node_coord']=node_coord
    plt.plot(coordX,coordY,color='k')
for node in nodeDict:
    if layers['probTot'][node]>0:
        try:
            probMon_node=layers.drop(layers['nodeConnexions'][node]).sum(axis=0)
        except:
            probMon_node=layers.drop(layers['nodeConnexions'][node]).sum(axis=0)
    
        textProb=str(node)+'-'+str(round(100*layers['probTot'][node],1))+'\n'
        if layers['probTI'][node]>0:
            textProb=textProb+'TI:'+str(round(100*layers['probTI'][node],1))+' ('+str(round(100*layers['probTI'][node]/probMon_node['probTI'],1))+')' +'\n'
        if layers['probWO'][node]>0:
            textProb=textProb+'WO:'+str(round(100*layers['probWO'][node],1))+' ('+str(round(100*layers['probWO'][node]/probMon_node['probWO'],1))+')' +'\n'
        if layers['probST'][node]>0:
            textProb=textProb+'ST:'+str(round(100*layers['probST'][node],1))+' ('+str(round(100*layers['probST'][node]/probMon_node['probST'],1))+')' +'\n'
        if layers['probGR'][node]>0:
            textProb=textProb+'GR:'+str(round(100*layers['probGR'][node],1))+' ('+str(round(100*layers['probGR'][node]/probMon_node['probGR'],1))+')' +'\n'
        if layers['probCL'][node]>0:
            textProb=textProb+'CL:'+str(round(100*layers['probCL'][node],1))+' ('+str(round(100*layers['probCL'][node]/probMon_node['probCL'],1))+')' +'\n'
        text(nodeDict[node][0],nodeDict[node][1],textProb,size=8, bbox=dict(facecolor=cmap(norm(layers['probTot'][node])), alpha=.9))

strucPrint(output,nodeDict)


plt.show()