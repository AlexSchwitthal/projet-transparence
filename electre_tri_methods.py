# -*- coding: utf-8 -*-

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
        if aliment_surclasse_profil == 1:
            return size-i       


def optimisticMajoritySorting(aliment, list_profils, list_poids, seuil):
    size = len(list_profils)
    for i in range (size):
        profil = list_profils[size-i-1]
        profil_surclasse_aliment = surclassement(profil, aliment, list_poids, seuil)
        aliment_surclasse_profil = surclassement(aliment, profil, list_poids, seuil)
        if (profil_surclasse_aliment == 1) and (aliment_surclasse_profil == 0):
            return i 
       
def defineElectreScore(list_aliments, list_poids, list_profils, seuil, label):
    label['pessimist_score'] = 'pessimist_score'
    label['optimist_score'] = 'optimist_score'
    
    for aliment in list_aliments:
        aliment['pessimist_score'] = pessimisticMajoritySorting(aliment['criteres'], list_profils, list_poids, seuil)
        aliment['optimist_score'] = optimisticMajoritySorting(aliment['criteres'], list_profils, list_poids, seuil)
