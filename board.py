#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:52:05 2020

@author: miguel
"""
import math
from general import probDice,printHex
import pandas as pd
import numpy as np

def tileCreation(output,lenGrid):

    #Terrain tiles -------------------------------------------
    h=lenGrid/math.cos(math.radians(30))
        
    tile1={'col':'','res':'','num':'','prob':'','id':1,'coord':[1,-2*lenGrid-2*h*math.sin(math.radians(30))],'node_coord':[],'node_name':[11,10,9,1,2,3]}
    tile2={'col':'','res':'','num':'','prob':'','id':2,'coord':[2,-2*lenGrid-2*h*math.sin(math.radians(30))],'node_coord':[],'node_name':[13,12,11,3,4,5]}
    tile3={'col':'','res':'','num':'','prob':'','id':3,'coord':[3,-2*lenGrid-2*h*math.sin(math.radians(30))],'node_coord':[],'node_name':[15,14,13,5,6,7]}
    
    tile4={'col':'','res':'','num':'','prob':'','id':4,'coord':[.5,-lenGrid-h*math.sin(math.radians(30))],'node_coord':[],'node_name':[20,19,18,8,9,10]}
    tile5={'col':'','res':'','num':'','prob':'','id':5,'coord':[1.5,-lenGrid-h*math.sin(math.radians(30))],'node_coord':[],'node_name':[22,21,20,10,11,12]}
    tile6={'col':'','res':'','num':'','prob':'','id':6,'coord':[2.5,-lenGrid-h*math.sin(math.radians(30))],'node_coord':[],'node_name':[24,23,22,12,13,14]}
    tile7={'col':'','res':'','num':'','prob':'','id':7,'coord':[3.5,-lenGrid-h*math.sin(math.radians(30))],'node_coord':[],'node_name':[26,25,24,14,15,16]}
    
    tile8={'col':'','res':'','num':'','prob':'','id':8,'coord':[0,0],'node_coord':[],'node_name':[30,29,28,17,18,19]}
    tile9={'col':'','res':'','num':'','prob':'','id':9,'coord':[1,0],'node_coord':[],'node_name':[32,31,30,19,20,21]}
    tile10={'col':'','res':'','num':'','prob':'','id':10,'coord':[2,0],'node_coord':[],'node_name':[34,33,32,21,22,23]}
    tile11={'col':'','res':'','num':'','prob':'','id':11,'coord':[3,0],'node_coord':[],'node_name':[36,35,34,23,24,25]}
    tile12={'col':'','res':'','num':'','prob':'','id':12,'coord':[4,0],'node_coord':[],'node_name':[38,37,36,25,26,27]}
    
    tile13={'col':'','res':'','num':'','prob':'','id':13,'coord':[.5,lenGrid+h*math.sin(math.radians(30))],'node_coord':[],'node_name':[41,40,39,29,30,31]}
    tile14={'col':'','res':'','num':'','prob':'','id':14,'coord':[1.5,lenGrid+h*math.sin(math.radians(30))],'node_coord':[],'node_name':[43,42,41,31,32,33]}
    tile15={'col':'','res':'','num':'','prob':'','id':15,'coord':[2.5,lenGrid+h*math.sin(math.radians(30))],'node_coord':[],'node_name':[45,44,43,33,34,35]}
    tile16={'col':'','res':'','num':'','prob':'','id':16,'coord':[3.5,lenGrid+h*math.sin(math.radians(30))],'node_coord':[],'node_name':[47,46,45,35,36,37]}
    tile17={'col':'','res':'','num':'','prob':'','id':17,'coord':[1,2*lenGrid+2*h*math.sin(math.radians(30))],'node_coord':[],'node_name':[50,49,48,40,41,42]}
    tile18={'col':'','res':'','num':'','prob':'','id':18,'coord':[2,2*lenGrid+2*h*math.sin(math.radians(30))],'node_coord':[],'node_name':[52,51,50,42,43,44]}
    tile19={'col':'','res':'','num':'','prob':'','id':19,'coord':[3,2*lenGrid+2*h*math.sin(math.radians(30))],'node_coord':[],'node_name':[54,53,52,44,45,46]}
    
    tiles=[tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,tile10,tile11,tile12,tile13,tile14,tile15,tile16,tile17,tile18,tile19]
    
    tileDF = pd.concat([pd.Series(d) for d in tiles], axis=1).fillna(0).T
    tileDF.index = tileDF['id']
    
    for tile in tileDF.iterrows():
        [coordX,coordY,node_coord]=printHex(tile,lenGrid)
        #Fill the node cordinate
        tileDF.loc[tile[1]['id'],'node_coord'] =node_coord
        #Fill the dice number in the tile
        tileDF.loc[tile[1]['id'],'num'] =output['data']['terrains'][str(tile[1]['id'])]['diceNumber']
        #Fill the resource in the tile
        tileDF.loc[tile[1]['id'],'res'] =output['data']['terrains'][str(tile[1]['id'])]['type']
        #Assign color to tile
        if output['data']['terrains'][str(tile[1]['id'])]['type']=='ti': #Timber
            tileDF.loc[tile[1]['id'],'col'] ='#267F0B'
        elif output['data']['terrains'][str(tile[1]['id'])]['type']=='wo': #Wool
            tileDF.loc[tile[1]['id'],'col'] ='#55E237'
        elif output['data']['terrains'][str(tile[1]['id'])]['type']=='st': #Stone
            tileDF.loc[tile[1]['id'],'col'] ='#807E74'
        elif output['data']['terrains'][str(tile[1]['id'])]['type']=='gr': #Grass Wheat
            tileDF.loc[tile[1]['id'],'col'] ='#C1A70A'
        elif output['data']['terrains'][str(tile[1]['id'])]['type']=='cl': #Brick
            tileDF.loc[tile[1]['id'],'col'] ='#E24907'
        else:
            tileDF.loc[tile[1]['id'],'col'] ='#5D3C18' #desert
        #Assign probability to tile
        tileDF.loc[tile[1]['id'],'prob'] =probDice(output['data']['terrains'][str(tile[1]['id'])]['diceNumber'])
    
    
    #Trading ports -------------------------------------
    
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
    
    portsDF = pd.concat([pd.Series(d) for d in ports], axis=1).fillna(0).T
    portsDF.index = np.arange(1,10)
    
    #Nodes --------------------------------------------------
    connectNodes=[[9,2],[1,3],[2,4,11],[3,5],[4,6,13],[5,7],[6,15],[18,9],[8,10,1],[9,11,20],[10,12,3],[11,13,22],[12,14,5],[13,15,24],[14,16,7],[15,26],[28,18],[17,19,8],[18,20,30],[19,21,10],[20,22,32],[21,23,12],[22,24,34],[23,25,14],[24,26,36],[25,27,16],[16,27,25],[17,29],[28,30,39],[29,31,19],[30,32,41],[31,33,21],[32,34,43],[33,35,23],[34,36,45],[35,37,25],[36,38,47],[37,27],[29,40],[39,41,48],[40,42,31],[41,43,50],[42,44,33],[43,45,52],[44,46,35],[45,47,54],[46,37],[40,49],[48,50],[49,51,42],[50,52],[51,53,44],[52,54],[53,46]]

    nodes=pd.DataFrame({'id':np.arange(1,55)})
    nodes.set_index('id',inplace=True)
    nodes['probTI']=np.zeros(54)
    nodes['probWO']=np.zeros(54)
    nodes['probST']=np.zeros(54)
    nodes['probGR']=np.zeros(54)
    nodes['probCL']=np.zeros(54)
    nodes['coordX']=np.zeros(54)
    nodes['coordY']=np.zeros(54)
    
    for i in range(1,1+len(tileDF)):
        nodeNum=0
        for nn in tileDF['node_name'][i]:
            #Probabilities
            if tileDF['res'][i]=='ti':
                nodes['probTI'][nn]=nodes['probTI'][nn]+tileDF['prob'][i]
            elif tileDF['res'][i]=='wo':
                nodes['probWO'][nn]=nodes['probWO'][nn]+tileDF['prob'][i]
            elif tileDF['res'][i]=='st':
                nodes['probST'][nn]=nodes['probST'][nn]+tileDF['prob'][i]
            elif tileDF['res'][i]=='gr':
                nodes['probGR'][nn]=nodes['probGR'][nn]+tileDF['prob'][i]
            elif tileDF['res'][i]=='cl':
                nodes['probCL'][nn]=nodes['probCL'][nn]+tileDF['prob'][i]
            #Coordinates
            nodes['coordX'][nn]=tileDF['node_coord'][i][nodeNum][0]
            nodes['coordY'][nn]=tileDF['node_coord'][i][nodeNum][1]
            nodeNum+=1

    nodes['conn']=connectNodes
    nodes['probTot']=nodes[['probTI','probWO','probST','probGR','probCL']].sum(axis=1)
    exchangeRate=[[4,4,4,4,4]]*54
    
    exchangeRate[2]=[4,2,4,4,4] #Brick Port
    exchangeRate[3]=[4,2,4,4,4] #Brick Port
    
    exchangeRate[5]=[3,3,3,3,3] #Regular Port
    exchangeRate[6]=[3,3,3,3,3] #Regular Port
    
    exchangeRate[25]=[3,3,3,3,3] #Regular Port
    exchangeRate[15]=[3,3,3,3,3] #Regular Port 
    
    exchangeRate[46]=[4,4,2,4,4] #Wool Port
    exchangeRate[36]=[4,4,2,4,4] #Wool Port
    
    exchangeRate[52]=[3,3,3,3,3] #Regular Port
    exchangeRate[53]=[3,3,3,3,3] #Regular Port
    
    exchangeRate[49]=[4,4,4,2,4] #Ore Port
    exchangeRate[50]=[4,4,4,2,4] #Ore Port
    
    exchangeRate[39]=[4,4,4,4,2] #Wheat Port
    exchangeRate[38]=[4,4,4,4,2] #Wheat Port
    
    exchangeRate[27]=[3,3,3,3,3] #Regular Port
    exchangeRate[16]=[3,3,3,3,3] #Regular Port
    
    
    nodes['exchangeRate']=exchangeRate

    return [tileDF,portsDF,nodes]

