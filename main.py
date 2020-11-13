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
from profils import *

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
#writeDB('Datasets/DB1_score_lamdba_'+str(seuil1), list_cereals_labels, list_cereals) 

seuil2 = 0.7
list_items2, label_DB2 = readDB2()
defineElectreScore(list_items2, list_poids, list_profils, seuil2, label_DB2)
#defineFeuxTricolore(list_items2, label_DB2)  
#writeDB('Datasets/DB2_score_lamdba_'+str(seuil2), label_DB2, list_items2) 

seuil3 = 0.7
list_items3, label_DB3 = readDB3()
defineElectreScore(list_items3, list_poids, list_profils, seuil3, label_DB3)
#defineFeuxTricolore(list_items3, label_DB3)  
#writeDB('Datasets/DB3_score_lamdba_'+str(seuil3), label_DB3, list_items3) 


#print("\n\n\n ========= STAT REPARTITION ====== \n")
#getRepartitionCategorie("nutriscore", list_items3)
#print("\n")
#☻getRepartitionCategorie("nova", list_items2)    
#print("\n\n\n ======= NUTRISCORE ======")
#compareNutriscoreNova(list_items3)
#print("\n\n\n====== NOVA =======")
#compareNovaNutriscore(list_items3)
#print("\n\n\n====== FEUX TRICOLORE =======\n")
#compareNutriscoreFeux(list_items3)
#print("\n\n\n====== FEUX TRICOLORE =======\n")
#nutriscoreByColor(list_items2, "green", 4)

#print("\n\n\n ==== NUTRISCORE / YUKA ======\n")
#compareNutriscoreYuka(list_items3)
#detailsNutriscoreYuka(list_items3, "yuka")
#detailsNutriscoreYuka(list_items3, "nutriscore")
#detailsNutriscoreYuka(list_items3, "equals")

#for i in range(len(list_items3)):
 #   print("yuka : ", list_items3[i]['score_yuka'], " |||  nutriscore : ", list_items3[i]['nutriscore'])
  #  print(duelNutriscoreYuka(list_items3[i]['nutriscore'], list_items3[i]['score_yuka']))
   # print("")
   
#print("\n\n\n ==== YUKA / NOVA ======\n")
#compareYukaNova(list_items3)


#print("\n\n\n ==== YUKA / FEU ======\n")
#yukaByColor(list_items3, "red", 3)

#print("\n\n\n ==== BIO ======\n")
#getRepartitionBio(list_items3)
#compareNutriscoreBio(list_items3)
#compareNovaBio(list_items3)


#print("\n\n\n ==== ELECTRE TRI / NUTRISCORE ======\n")
#print("\n -- PESSIMIST --\n")
#compareElectreNutriscore(list_items2, 'pessimist_score')
#analyseElectre(list_items3, "DB3", 'pessimist_score')
#print("\n\n -- OPTIMIST --\n")
#compareElectreNutriscore(list_items2, 'optimist_score')


#db = 1
print("ANALYSE ELECTRE :")     
for db in range(1, 4):
    db_to_use = ""
    seuil = 0.5
    for i in range(3):
        seuil = 0.5 + i*0.1
        list_items, label_DB
        list_profils_to_use = ""
        db_to_use = ""
        if(db == 1):
            list_items, label_DB = readDB1()
            list_profils_to_use = list_profilsDB1
            db_to_use = "DB1"
        elif(db == 2):
            list_items, label_DB == readDB2()
            list_profils_to_use = list_profilsDB2
            db_to_use = "DB2"
        elif(db == 3):
            list_items,label_DB = readDB3()
            list_profils_to_use = list_profilsDB3
            db_to_use = "DB3"
            
        list_profils = defineProfileWithNutriscore(list_items) 
        defineElectreScore(list_items, list_poids, list_profils, seuil, label_DB)
        print("\n\n\nDB", db, ": seuil de ", seuil, ", poids de base, profils nutriscore")
        print("\n\n -- PESSIMIST --")
        analyseElectre(list_items, db_to_use, 'pessimist_score')
        print("\n\n -- OPTIMIST --")
        analyseElectre(list_items, db_to_use, 'optimist_score')
        
        list_items, label_DB = readDB3()
        defineElectreScore(list_items, list_poids, list_profilsAll, seuil, label_DB)
        defineFeuxTricolore(list_items, label_DB)  
        print("\n\n\nDB", db, ": seuil de ", seuil, ", poids de base, profils all")
        print("\n\n -- PESSIMIST --")
        analyseElectre(list_items, db_to_use, 'pessimist_score')
        print("\n\n -- OPTIMIST --")
        analyseElectre(list_items, db_to_use, 'optimist_score')
            
        list_items, label_DB = readDB3()
        defineElectreScore(list_items, list_poids, list_profils_to_use, seuil, label_DB)
        defineFeuxTricolore(list_items, label_DB)  
        print("\n\n\nDB", db, ": seuil de ", seuil, ", poids de base, profils DB", db)
        print("\n\n -- PESSIMIST --")
        analyseElectre(list_items, db_to_use, 'pessimist_score')
        print("\n\n -- OPTIMIST --")
        analyseElectre(list_items, db_to_use, 'optimist_score')
            
        #avec poids favorisant critères négatifs
        list_profils = defineProfileWithNutriscore(list_items) 
        list_items, label_DB = readDB3()
        defineElectreScore(list_items, list_poids1, list_profils, seuil, label_DB)
        defineFeuxTricolore(list_items, label_DB)   
        print("\n\n\nDB", db, ": seuil de ", seuil, ", poids de base, profils nutriscore")
        print("\n\n -- PESSIMIST --")
        analyseElectre(list_items, db_to_use, 'pessimist_score')
        print("\n\n -- OPTIMIST --")
        analyseElectre(list_items, db_to_use, 'optimist_score')
    
        list_items, label_DB = readDB3()
        defineElectreScore(list_items, list_poids1, list_profilsAll, seuil, label_DB)
        defineFeuxTricolore(list_items, label_DB)         
        print("\n\n\nDB", db, ": seuil de ", seuil, ", poids de base, profils all")
        print("\n\n -- PESSIMIST --")
        analyseElectre(list_items, db_to_use, 'pessimist_score')
        print("\n\n -- OPTIMIST --")
        analyseElectre(list_items, db_to_use, 'optimist_score')
        
        list_items, label_DB = readDB3()
        defineElectreScore(list_items, list_poids1, list_profils_to_use, seuil, label_DB)
        defineFeuxTricolore(list_items, label_DB)         
        print("\n\n\nDB", db, ": seuil de ", seuil, ", poids de base, profils nutriscore")
        print("\n\n -- PESSIMIST --")
        analyseElectre(list_items, db_to_use, 'pessimist_score')
        print("\n\n -- OPTIMIST --")
        analyseElectre(list_items, db_to_use, 'optimist_score')
        
        


        