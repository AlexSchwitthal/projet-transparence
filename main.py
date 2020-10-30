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
list_poids = [1,1,1,1,2,2]
#ordonné de profil b6 à profil b1 et de critère 1 à critère 6
list_profils = [[100,0,0,0,100,100],
                [1550,11,0.8,0.3,10,11],
                [1650,14,1,0.4,7,8],
                [1750,17,1.7,0.5,4,5],
                [1850,20,4,0.6,3,2.5],
                [10000,100,100,100,0,0]]

seuil1 = 0.7
list_cereals, list_cereals_labels = readDB1()  
defineElectreScore(list_cereals, list_poids, list_profils, seuil1, list_cereals_labels)  
writeDB('Datasets/DB1_score_lamdba_'+str(seuil1), list_cereals_labels, list_cereals) 

seuil2 = 0.7
list_items2, label_DB2 = readDB2()
defineElectreScore(list_items2, list_poids, list_profils, seuil2, label_DB2)
defineFeuxTricolore(list_items2, label_DB2)  
writeDB('Datasets/DB2_score_lamdba_'+str(seuil2), label_DB2, list_items2) 

seuil3 = 0.7
list_items3, label_DB3 = readDB3()
defineElectreScore(list_items3, list_poids, list_profils, seuil3, label_DB3)
defineFeuxTricolore(list_items3, label_DB3)  
writeDB('Datasets/DB3_score_lamdba_'+str(seuil3), label_DB3, list_items3) 
       
        