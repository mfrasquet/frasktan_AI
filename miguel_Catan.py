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

credentials=pd.read_csv('../credentials.csv')
username=credentials['username'][0]
pwd=credentials['pwd'][0]

connectNodes=[[9,2],[1,3],[2,4,11],[3,5],[4,6,13],[5,7],[6,15],[18,9],[8,10,1],[9,11,20],[10,12,3],[11,13,22],[12,14,5],[13,15,24],[14,16,7],[15,26],[28,18],[17,19,8],[18,20,30],[19,21,10],[20,22,32],[21,23,12],[22,24,34],[23,25,14],[24,26,36],[25,27,16],[16,27,25],[17,29],[28,30,39],[29,31,19],[30,32,41],[31,33,21],[32,34,43],[33,35,23],[34,36,45],[35,37,25],[36,38,47],[37,27],[29,40],[39,41,48],[40,42,31],[41,43,50],[42,44,33],[43,45,52],[44,46,35],[45,47,54],[46,37],[40,49],[48,50],[49,51,42],[50,52],[51,53,44],[52,54],[53,46]]
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


layers=pd.DataFrame({'node':range(1,55)})
layers.set_index('node', inplace=True)

layers['nodeConnexions']=connectNodes

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


r = requests.post('http://juatan.cosasdejuan.es/juatanApi.php', json=refresh)
r.status_code
output=r.json()

#Player


#Terrain
lenGrid=0.5
h=lenGrid/math.cos(math.radians(30))
    
tile1={'col':'','res':'','num':'','prob':'','id':1,'coord':[1,-2*lenGrid-2*h*math.sin(math.radians(30))],'nodes':[40,41,42,50,49,48],'node_coord':[],'node_name':[11,10,9,1,2,3]}
tile2={'col':'','res':'','num':'','prob':'','id':2,'coord':[2,-2*lenGrid-2*h*math.sin(math.radians(30))],'nodes':[42,43,44,52,51,50],'node_coord':[],'node_name':[13,12,11,3,4,5]}
tile3={'col':'','res':'','num':'','prob':'','id':3,'coord':[3,-2*lenGrid-2*h*math.sin(math.radians(30))],'nodes':[44,45,46,54,53,52],'node_coord':[],'node_name':[15,14,13,5,6,7]}

tile4={'col':'','res':'','num':'','prob':'','id':4,'coord':[.5,-lenGrid-h*math.sin(math.radians(30))],'nodes':[29.30,31,41,40,39],'node_coord':[],'node_name':[20,19,18,8,9,10]}
tile5={'col':'','res':'','num':'','prob':'','id':5,'coord':[1.5,-lenGrid-h*math.sin(math.radians(30))],'nodes':[31,32,33,43,42,41],'node_coord':[],'node_name':[22,21,20,10,11,12]}
tile6={'col':'','res':'','num':'','prob':'','id':6,'coord':[2.5,-lenGrid-h*math.sin(math.radians(30))],'nodes':[33,34,35,45,44,43],'node_coord':[],'node_name':[24,23,22,12,13,14]}
tile7={'col':'','res':'','num':'','prob':'','id':7,'coord':[3.5,-lenGrid-h*math.sin(math.radians(30))],'nodes':[35,36,37,47,46,45],'node_coord':[],'node_name':[26,25,24,14,15,16]}

tile8={'col':'','res':'','num':'','prob':'','id':8,'coord':[0,0],'nodes':[17,18,19,30,29,28],'node_coord':[],'node_name':[30,29,28,17,18,19]}
tile9={'col':'','res':'','num':'','prob':'','id':9,'coord':[1,0],'nodes':[19,20,21,32,31,30],'node_coord':[],'node_name':[32,31,30,19,20,21]}
tile10={'col':'','res':'','num':'','prob':'','id':10,'coord':[2,0],'nodes':[21.22,23,34,33,32],'node_coord':[],'node_name':[34,33,32,21,22,23]}
tile11={'col':'','res':'','num':'','prob':'','id':11,'coord':[3,0],'nodes':[23,24,25,36,35,34],'node_coord':[],'node_name':[36,35,34,23,24,25]}
tile12={'col':'','res':'','num':'','prob':'','id':12,'coord':[4,0],'nodes':[25,26,27,38,37,36],'node_coord':[],'node_name':[38,37,36,25,26,27]}

tile13={'col':'','res':'','num':'','prob':'','id':13,'coord':[.5,lenGrid+h*math.sin(math.radians(30))],'nodes':[29.30,31,41,40,39],'node_coord':[],'node_name':[41,40,39,29,30,31]}
tile14={'col':'','res':'','num':'','prob':'','id':14,'coord':[1.5,lenGrid+h*math.sin(math.radians(30))],'nodes':[31,32,33,43,42,41],'node_coord':[],'node_name':[43,42,41,31,32,33]}
tile15={'col':'','res':'','num':'','prob':'','id':15,'coord':[2.5,lenGrid+h*math.sin(math.radians(30))],'nodes':[33,34,35,45,44,43],'node_coord':[],'node_name':[45,44,43,33,34,35]}
tile16={'col':'','res':'','num':'','prob':'','id':16,'coord':[3.5,lenGrid+h*math.sin(math.radians(30))],'nodes':[35,36,37,47,46,45],'node_coord':[],'node_name':[47,46,45,35,36,37]}
tile17={'col':'','res':'','num':'','prob':'','id':17,'coord':[1,2*lenGrid+2*h*math.sin(math.radians(30))],'nodes':[40,41,42,50,49,48],'node_coord':[],'node_name':[50,49,48,40,41,42]}
tile18={'col':'','res':'','num':'','prob':'','id':18,'coord':[2,2*lenGrid+2*h*math.sin(math.radians(30))],'nodes':[42,43,44,52,51,50],'node_coord':[],'node_name':[52,51,50,42,43,44]}
tile19={'col':'','res':'','num':'','prob':'','id':19,'coord':[3,2*lenGrid+2*h*math.sin(math.radians(30))],'nodes':[44,45,46,54,53,52],'node_coord':[],'node_name':[54,53,52,44,45,46]}

tiles=[tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,tile10,tile11,tile12,tile13,tile14,tile15,tile16,tile17,tile18,tile19]

port1={'col':'k','type':'all','coord':[tile8['coord'][0]-1.8*lenGrid,tile8['coord'][1]],'nodes':[28,17]}
port2={'col':'#267F0B','type':'ti','coord':[tile4['coord'][0]-lenGrid,tile4['coord'][1]-1.5*lenGrid],'nodes':[8,9]}
port3={'col':'#E24907','type':'cl','coord':[tile2['coord'][0]-lenGrid,tile2['coord'][1]-1.5*lenGrid],'nodes':[3,4]}
port4={'col':'k','type':'all','coord':[tile3['coord'][0]+0.8*lenGrid,tile3['coord'][1]-1.5*lenGrid],'nodes':[6,7]}
port5={'col':'k','type':'all','coord':[tile7['coord'][0]+1.8*lenGrid,tile7['coord'][1]],'nodes':[26,16]}
port6={'col':'#55E237','type':'wo','coord':[tile16['coord'][0]+1.8*lenGrid,tile16['coord'][1]],'nodes':[47,37]}
port7={'col':'k','type':'all','coord':[tile19['coord'][0]+0.8*lenGrid,tile19['coord'][1]+1.8*lenGrid],'nodes':[53,54]}
port8={'col':'#807E74','type':'st','coord':[tile18['coord'][0]-0.8*lenGrid,tile18['coord'][1]+1.8*lenGrid],'nodes':[50,51]}
port9={'col':'#C1A70A','type':'gr','coord':[tile13['coord'][0]-0.8*lenGrid,tile13['coord'][1]+1.8*lenGrid],'nodes':[39,40]}

ports=[port1,port2,port3,port4,port5,port6,port7,port8,port9]

for tile in tiles:
    tile['num']=output['data']['terrains'][str(tile['id'])]['diceNumber']
    tile['res']=output['data']['terrains'][str(tile['id'])]['type']
    if tile['res']=='ti': #Timber
        tile['col']='#267F0B'
    elif tile['res']=='wo': #Wool
        tile['col']='#55E237'
    elif tile['res']=='st': #Stone
        tile['col']='#807E74'
    elif tile['res']=='gr': #Grass Wheat
        tile['col']='#C1A70A'
    elif tile['res']=='cl': #Brick
        tile['col']='#E24907'
    else:
        tile['col']='#5D3C18' #desert
    tile['prob']=probDice(output['data']['terrains'][str(tile['id'])]['diceNumber'])

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