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
from general import plotID,plotMap,plotNodeProb,plotMapStructure


#Load credentials
credentials=pd.read_csv('credentials.csv')
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

#Create tiles, ports and nodes with info from game
lenGrid=0.5
[tiles,ports,nodes]=tileCreation(output,lenGrid)

#Plot ID
plotID(tiles,ports,nodes,lenGrid)
#Plot Map
plotMap(tiles,ports,nodes,lenGrid)

plotMapStructure(tiles,ports,nodes,lenGrid,output)
#Plot Prob Node Prob
plotNodeProb(tiles,ports,nodes,lenGrid)

#Summary of scarcity of resources
probMon=nodes.sum(axis=0)
print(probMon)


        


    

