#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:06:11 2020

@author: miguel
"""
import pandas as pd
import numpy as np

def createNodeM():
    connectNodes=[[9,2],[1,3],[2,4,11],[3,5],[4,6,13],[5,7],[6,15],[18,9],[8,10,1],[9,11,20],[10,12,3],[11,13,22],[12,14,5],[13,15,24],[14,16,7],[15,26],[28,18],[17,19,8],[18,20,30],[19,21,10],[20,22,32],[21,23,12],[22,24,34],[23,25,14],[24,26,36],[25,27,16],[16,27,25],[17,29],[28,30,39],[29,31,19],[30,32,41],[31,33,21],[32,34,43],[33,35,23],[34,36,45],[35,37,25],[36,38,47],[37,27],[29,40],[39,41,48],[40,42,31],[41,43,50],[42,44,33],[43,45,52],[44,46,35],[45,47,54],[46,37],[40,49],[48,50],[49,51,42],[50,52],[51,53,44],[52,54],[53,46]]
    
    node=pd.DataFrame({'index':np.arange(1,55),'connexions':connectNodes})
    node.set_index('index',inplace=True)
    return node

def fillProbNodeM(node,tile):
    node['probTI']=np.zeros(54)
    node['probWO']=np.zeros(54)
    node['probST']=np.zeros(54)
    node['probGR']=np.zeros(54)
    node['probCL']=np.zeros(54)
    
    #Fill probabilities
    for tile in tiles:
        for i in tile['node_name']:
            if tile['res']=='ti':
                node.loc[i,'probTI'] =node.loc[i,'probTI'] +tile['prob']
            elif tile['res']=='wo':
                node.loc[i,'probWO']=node.loc[i,'probWO']+tile['prob']
            elif tile['res']=='st':
                node.loc[i,'probST']=node.loc[i,'probST']+tile['prob']
            elif tile['res']=='gr':
                node.loc[i,'probGR']=node.loc[i,'probGR']+tile['prob']
            elif tile['res']=='cl':
                node.loc[i,'probCL']=node.loc[i,'probCL']+tile['prob']
            else:
                pass
    return node

