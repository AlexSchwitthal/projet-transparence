# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:33:35 2020

@author: boris
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#nutriscore de A à E ie 5 à 1
A = 5
E = 1
from methods import *
from read_write_db import *


#ordonné de critère 1 à critère 6
#list_poids = [3,3,3,3,3,0.5] #93 ; 94
list_poids = [1,1,1,1,2,2] #poids de base
list_poids1 = [2,2,2,2,1,1] #poids favorisants les critères négatifs
#list_poids2 = [1,1,1,1,0.5,0.2] #92 ; 92

#ordonné de profil b6 à profil b1 et de critère 1 à critère 6
#liste des profils de base
list_profils = [[100,0,0,0,100,100],
                [1550,11,0.8,0.3,10,11],
                [1650,14,1,0.4,7,8],
                [1750,17,1.7,0.5,4,5],
                [1850,20,4,0.6,3,2.5],
                [10000,100,100,100,0,0]]

list_profils_base = [[100,0,0,0,100,100],
                [1550,11,0.8,0.3,10,11],
                [1650,14,1,0.4,7,8],
                [1750,17,1.7,0.5,4,5],
                [1850,20,4,0.6,3,2.5],
                [10000,100,100,100,0,0]]


#liste des profils en fonction des quintiles
#Pour les céréales
list_profilsDB1 = [[-1,-1,-1,-1,100,100],
                [1561,0.3,5.2,0.11,9.7,6.5],
                [1603,0.7,15.1,0.25,8.33,4.8],
                [1650,2,21.8,0.35,7.6,3.4],
                [1741,4,28.8,0.56,6,0],
                [10000,100,100,100,-1,-1]]

#Sur toutes les données volailles

list_profilsAll = [[-1,-1,-1,-1,100,100],
                [444,0.45,0,0.312,22,0.7],
                [551,1.025,0.5,0.48,19.72,0],
                [752.5,2.3,0.9,0.577,17,0],
                [927,3.7,1.59,0.75,14,0],
                [10000,100,100,100,-1,-1]]

#Sur DB2
list_profilsDB2 = [[-1 ,-1   ,-1   ,-1   ,100,100],
                [448,0.5 ,0   ,0.29,22 ,1.2],
                [553,1   ,0.5 ,0.47,20 ,0.5],
                [821,2.3 ,0.9 ,0.60,17 ,0],
                [992,4.02,1.4 ,0.76,14 ,0],
                [10000,100 ,100 ,100 ,-1  ,-1]]

#Sur DB3
list_profilsDB3 = [[0 ,0   ,0  ,0   ,100,100],
                [448, 0.4,0.5,0.332,23,1.2],
                [689 ,1.5,0.7,0.48 ,21,0.1],
                [861 ,2.5,1  ,0.6  ,17,0  ],
                [1047,4.5,1.5,0.84 ,13,0  ],
                [10000,100 ,100 ,100 ,0  ,0]]



list_items, list_items_labels = readDB2()  

def defineProfileWithNutriscore(list_items):
    sum = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    count = [0.0,0.0,0.0,0.0,0.0]
    for item in list_items:
        for i in range(6):
            sum[item['nutriscore']-1][i] += item['criteres'][i]
             
        count[item['nutriscore']-1] += 1
    for j in range(5):
        for i in range(6):
            sum[j][i] = (sum[j][i])/count[j]

    prof1 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for i in range (6):
        prof1[0][i] = (sum[0][i]+ sum[1][i])/2
        prof1[1][i] = (sum[1][i]+ sum[2][i])/2
        prof1[2][i] = (sum[2][i]+ sum[3][i])/2
        prof1[3][i] = (sum[3][i]+ sum[4][i])/2

    list_profils3 = []
    list_profils3 = [[-100,-100,-100,-100,10000,10000]]

    list_profils3.append(prof1[3])     
    list_profils3.append(prof1[2]) 
    list_profils3.append(prof1[1]) 
    list_profils3.append(prof1[0]) 
    list_profils3.append([10000,10000,10000,10000,-100,-100]) 
    
    return list_profils3

list_profilsWithNutriscore = defineProfileWithNutriscore(list_items)

def checkError(total):
    print("Compte des erreurs totales ",total)
    for i in range(3):
        errorp = 0
        erroro = 0
        seuil = 0.5 + i*0.1
        print("\nSeuil ", seuil)
        defineElectreScore(list_items, list_poids, list_profilsAll, seuil, list_items_labels) 
        for item in list_items:
            if total :
            
                if (item['nutriscore'] != item['pessimist_score']):
                    errorp += 1
                if item['nutriscore'] != item['optimist_score'] :    
                   erroro += 1  
            else:
                if abs(item['nutriscore'] - item['pessimist_score']) >1:
                    errorp += 1   
                if abs(item['nutriscore'] - item['optimist_score']) >1:
                    erroro += 1 
                
        print("profil All")  
        print(erroro) 
        print(errorp)
        errorp = 0
        erroro = 0
        print("\nSeuil ", seuil)
        defineElectreScore(list_items, list_poids, list_profilsDB2, seuil, list_items_labels) 
        for item in list_items:
            if total :
            
                if (item['nutriscore'] != item['pessimist_score']):
                    errorp += 1
                if item['nutriscore'] != item['optimist_score'] :    
                   erroro += 1  
            else:
                if abs(item['nutriscore'] - item['pessimist_score']) >1:
                    errorp += 1   
                if abs(item['nutriscore'] - item['optimist_score']) >1:
                    erroro += 1 
                
        print("profil DB2")  
        print(erroro) 
        print(errorp)
        errorp = 0
        erroro = 0 
        defineElectreScore(list_items, list_poids, list_profilsWithNutriscore, seuil, list_items_labels) 
        for item in list_items:
            if total :
            
                if (item['nutriscore'] != item['pessimist_score']):
                    errorp += 1
                if item['nutriscore'] != item['optimist_score'] :    
                   erroro += 1  
            else:
                if abs(item['nutriscore'] - item['pessimist_score']) >1:
                    errorp += 1   
                if abs(item['nutriscore'] - item['optimist_score']) >1:
                    erroro += 1 
                
        print("profil 3")  
        print(erroro) 
        print(errorp)


#checkError(False)

seuil = 0.5
for i in range (3):
    seuil = 0.5 + i*0.1
    
    #avec poids de base
    list_items, label_DB = readDB3()
    list_profils = defineProfileWithNutriscore(list_items) 
    defineElectreScore(list_items, list_poids, list_profils, seuil, label_DB)
    defineFeuxTricolore(list_items, label_DB)  
    writeDB('Datasets/DB3_score_lamdba_'+str(seuil)+'_poids_de_base_profils_Nutriscore', label_DB, list_items) 

    list_items, label_DB = readDB3()
    defineElectreScore(list_items, list_poids, list_profilsDB3, seuil, label_DB)
    defineFeuxTricolore(list_items, label_DB)  
    writeDB('Datasets/DB3_score_lamdba_'+str(seuil)+'_poids_de_base_profils_Quintiles_DB3', label_DB, list_items)
    
    list_items, label_DB = readDB3()
    defineElectreScore(list_items, list_poids, list_profilsAll, seuil, label_DB)
    defineFeuxTricolore(list_items, label_DB)  
    writeDB('Datasets/DB3_score_lamdba_'+str(seuil)+'_poids_de_base_profils_Quintiles_All', label_DB, list_items)
    
    #avec poids favorisant critères négatifs
    list_profils = defineProfileWithNutriscore(list_items) 
    list_items, label_DB = readDB3()
    defineElectreScore(list_items, list_poids1, list_profils, seuil, label_DB)
    defineFeuxTricolore(list_items, label_DB)  
    writeDB('Datasets/DB3_score_lamdba_'+str(seuil)+'_poids_fav_criteres_negatifs_profils_Nutriscore', label_DB, list_items) 

    list_items, label_DB = readDB3()
    defineElectreScore(list_items, list_poids1, list_profilsDB3, seuil, label_DB)
    defineFeuxTricolore(list_items, label_DB)  
    writeDB('Datasets/DB3_score_lamdba_'+str(seuil)+'_poids_fav_criteres_negatifs_profils_Quintiles_DB3', label_DB, list_items)
    
    list_items, label_DB = readDB3()
    defineElectreScore(list_items, list_poids1, list_profilsAll, seuil, label_DB)
    defineFeuxTricolore(list_items, label_DB) 
    writeDB('Datasets/DB3_score_lamdba_'+str(seuil)+'_poids_fav_criteres_negatifs_profils_Quintiles_All', label_DB, list_items)

#seuil = 0.5
#for i in range (3):
    #seuil = 0.5 + i*0.1
    
    #avec poids de base
    #list_items, label_DB = readDB1()
    #list_profils = defineProfileWithNutriscore(list_items) 
    #defineElectreScore(list_items, list_poids, list_profils, seuil, label_DB) 
    #writeDB('Datasets/DB1_score_lamdba_'+str(seuil)+'_poids_de_base_profils_Nutriscore', label_DB, list_items) 

    #list_items, label_DB = readDB1()
    #defineElectreScore(list_items, list_poids, list_profilsDB1, seuil, label_DB)  
    #writeDB('Datasets/DB1_score_lamdba_'+str(seuil)+'_poids_de_base_profils_Quintiles_DB1', label_DB, list_items)
    
    #list_items, label_DB = readDB1()
    #defineElectreScore(list_items, list_poids, list_profils_base, seuil, label_DB)
    #writeDB('Datasets/DB1_score_lamdba_'+str(seuil)+'_poids_de_base_profils_base', label_DB, list_items)
    
    #avec poids favorisant critères négatifs
    #list_profils = defineProfileWithNutriscore(list_items) 
    #list_items, label_DB = readDB1()
    #defineElectreScore(list_items, list_poids1, list_profils, seuil, label_DB)
    #writeDB('Datasets/DB1_score_lamdba_'+str(seuil)+'_poids_fav_criteres_negatifs_profils_Nutriscore', label_DB, list_items) 

    #list_items, label_DB = readDB1()
    #defineElectreScore(list_items, list_poids1, list_profilsDB1, seuil, label_DB)
    #writeDB('Datasets/DB1_score_lamdba_'+str(seuil)+'_poids_fav_criteres_negatifs_profils_Quintiles_DB1', label_DB, list_items)
    
    #list_items, label_DB = readDB1()
    #defineElectreScore(list_items, list_poids1, list_profils_base, seuil, label_DB) 
    #writeDB('Datasets/DB1_score_lamdba_'+str(seuil)+'_poids_fav_criteres_negatifs_profils_base', label_DB, list_items)

import pandas
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
X=[]
y = []
for item in list_items:
    X.append(item['criteres'])
    y.append(item['nutriscore'])

model = KNeighborsClassifier(n_neighbors=10)
model.fit(X,y)

#for i in range(4):
#print(model.predict([sum[0]]))
#prediction.append(model.predict([[1550, 11 , 0.8, 0.3, 10, 11]]))
#prediction.append(model.predict([[1525.0, 0.6467812500000001, 7.978125, 0.15216749999999998, 9.956249999999999, 7.434375]]))

#prediction.append(model.predict([[1650, 14 , 1, 0.4, 7, 8]]))
#prediction.append(model.predict([[1750, 17 , 1.7, 0.5, 4, 5]]))
#prediction.append(model.predict([[1850, 20 , 4, 0.6, 3, 2.5]]))
#prediction.append(model.predict([[10000, 100 , 100, 100, 0, 0]]))  
#for i in range(len(prediction)):
    #print(prediction[i])

#list_profils = [[100,0,0,0,100,100]]
#for i in range(5):
#print(max)
#print(min)   

               
      