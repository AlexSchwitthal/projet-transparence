# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:01:33 2020

@author: boris
"""

#critere à valeurs entre 0 et 5
# 0 à 3 min ; 4 et 5 max
def indice_concordance_partiel(critere, item1, item2):
    score_item1 = item1[critere]
    score_item2 = item2[critere]
    
    if critere <= 3:
        if (score_item2 >= score_item1):
            return 1
        else:
            return 0
    else: 
        if (score_item1 >= score_item2):
            return 1
        else:
            return 0
            
def indice_concordance_global(item1, item2, list_poids):
    score = 0.0
    for critere in range(len(list_poids)):
        score += list_poids[critere] * indice_concordance_partiel(critere, item1, item2)
        
    score = score/(sum(list_poids))  
    return score    
           
def surclassement(item1, item2, list_poids, seuil):
    
    if indice_concordance_global(item1, item2, list_poids) >= seuil :
        return 1
    else:
        return 0

         
def pessimisticMajoritySorting(aliment, list_profils, list_poids, seuil):
    size = len(list_profils)
    for i in range (size):
        profil = list_profils[i]
        aliment_surclasse_profil = surclassement(aliment, profil, list_poids, seuil)
        #print('profil :', size-i)
        #print('aliment_surclasse_profil ', aliment_surclasse_profil)
        if aliment_surclasse_profil == 1:
            #print('aliment_surclasse_profil :', size-i)
            #print("Classe de l'aliment :", size-i)
            return size-i       


def optimisticMajoritySorting(aliment, list_profils, list_poids, seuil):
    size = len(list_profils)
    for i in range (size):
        profil = list_profils[size-i-1]
        profil_surclasse_aliment = surclassement(profil, aliment, list_poids, seuil)
        aliment_surclasse_profil = surclassement(aliment, profil, list_poids, seuil)
        #print('profil :', i+1)
        #print(list_profils[size-i-1])
        #print('profil_surclasse_aliment ', profil_surclasse_aliment)
        #print('aliment_surclasse_profil ', aliment_surclasse_profil)
        if (profil_surclasse_aliment == 1) and (aliment_surclasse_profil == 0):
            #print('profil_surclasse_aliment :', i+1)
            #print("Classe de l'aliment :", i)
            return i 
       
def defineElectreScore(list_aliments, list_poids, list_profils, seuil, label):
    label['pessimist_score'] = 'pessimist_score'
    label['optimist_score'] = 'optimist_score'
    
    for aliment in list_aliments:
        aliment['pessimist_score'] = pessimisticMajoritySorting(aliment['criteres'], list_profils, list_poids, seuil)
        aliment['optimist_score'] = optimisticMajoritySorting(aliment['criteres'], list_profils, list_poids, seuil)
        #if aliment['optimist_score'] != aliment['pessimist_score']:
           # print(aliment['product_name'])
           # print(aliment['nutriscore'])
           # print(aliment['pessimist_score'])
           # print(aliment['optimist_score'])

def feuxTricolore(aliment, critere):

    if critere == "fat_100g":
        if aliment['criteres_feux'][0] <= 3:
            return "green"
        
        elif aliment['criteres_feux'][0] <= 20:
            return "orange"
        else: 
            return "red"  
        
    if critere == "saturated-fat_100g":
        if aliment['criteres_feux'][1] <= 1.5:
            return "green"
        
        elif aliment['criteres_feux'][1] <= 5:
            return "orange"
        else: 
            return "red" 
        
    if critere == "sugars_100g":
        if aliment['criteres_feux'][2] <= 5:
            return "green"
        
        elif aliment['criteres_feux'][2] <= 12.5:
            return "orange"
        else: 
            return "red" 
     
    if critere == "salt_100g":
        if aliment['criteres_feux'][3] <= 0.3:
            return "green"
        elif aliment['criteres_feux'][3] <= 1.5:
            return "orange"
        else: 
            return "red"    

def defineFeuxTricolore(list_aliments, label):
    label['color_fat'] = 'color_fat'
    label['color_saturated-fat'] = 'color_saturated-fat'
    label['color_sugars'] = 'color_sugars'
    label['color_salt'] = 'color_salt'
    for aliment in list_aliments:
        aliment['color_fat'] = feuxTricolore(aliment, "fat_100g")
        aliment['color_saturated-fat'] = feuxTricolore(aliment, "saturated-fat_100g")
        aliment['color_sugars'] = feuxTricolore(aliment, "sugars_100g")
        aliment['color_salt'] = feuxTricolore(aliment, "salt_100g")
        
