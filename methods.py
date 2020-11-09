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
        
# ----------------------------------
# ANALYSE
# ----------------------------------

# convertie le nombre nutriscore en sa lettre correspondante
def convertNutriscore(number, categorie):
    if(categorie == "nutriscore"):
        if(number == 1):
            return "E"
        elif(number == 2):
            return "D"
        elif(number == 3):
            return "C"
        elif(number == 4):
            return "B"
        elif(number == 5):
            return "A"
    else:
        return number
 
# retourne la liste des produits ayant un score donné dans une catégorie donnée
def getListByScore(score, categorie, list_db):
    list_elements = []
    for i in range (len(list_db)):
        if(int(list_db[i][categorie]) == score):
            list_elements.append(list_db[i])
    return list_elements


def getCritereNameByNumber(number):
    if(number == 0):
        return "fat_100g"
    elif(number == 1):
        return "saturated-fat_100g"
    elif(number == 2):
        return "sugars_100g"
    elif(number == 3):
        return "salt_100g"

def getCritereNameNovaYuka(number):
    if(number == 0):
        return "energy_100g"
    elif(number == 1):
        return "saturated-fat_100g"
    elif(number == 2):
        return "sugars_100g"
    elif(number == 3):
        return "sodium_100g"
    elif(number == 4):
        return "proteins_100g"
    elif(number == 5):
        return "fiber_100g"
    
def converYukaInNutriscore(yuka):
    if(yuka <= 20):
        return 1
    elif(yuka <= 40):
        return 2
    elif(yuka <= 60):
        return 3
    elif(yuka <= 80):
        return 4
    elif(yuka <= 100):
        return 5
    
def duelNutriscoreYuka(nutriscore, yuka):
    conversion_yuka = converYukaInNutriscore(yuka)
    if(conversion_yuka == nutriscore):
        return "equals"
    elif(conversion_yuka < nutriscore):
        return "yuka"
    else:
        return "nutriscore"

def getListSeverity(list_db, score_used):
    list_elements = []
    for i in range (len(list_db)):
        nutriscore = list_db[i]["nutriscore"]
        yuka = list_db[i]["score_yuka"]
        result = duelNutriscoreYuka(nutriscore, yuka)
        if(result == score_used):
            list_elements.append(list_db[i])
    return list_elements

# regarde la répartition de la catégorie donnée sur l'ensemble des produits
def getRepartitionCategorie(categorie, list_db):
    if(categorie == "nutriscore"):    
        list_categorie = [0] * 6  
    elif(categorie == "nova"):
        list_categorie = [0] * 5
    list_categorie[0] = len(list_db)
      
    for i in range (len(list_db)):
        value = int(list_db[i][categorie])
        list_categorie[value] = list_categorie[value] + 1
    print("il y a un total de ", list_categorie[0], " produits")
    for i in range (len(list_categorie)-1, 0, -1):
        percent = "{:.2f}".format(list_categorie[i] / list_categorie[0] * 100)
        value = 0
        print("il y a ", list_categorie[i], "(", percent, "%) elements de la catégorie ", convertNutriscore(i, categorie), "(" , categorie, ")")
     
# pour chaque categorie de nutriscore, renvoie la répartition nova des produits
def compareNutriscoreNova(list_db):
    for i in range(5, 0, -1):
        list_nutriscore = getListByScore(i, "nutriscore", list_db)
        list_nova = [0,0,0,0]
        for j in range(len(list_nutriscore)):
            value = int(list_nutriscore[j]["nova"])
            list_nova[value-1] = list_nova[value-1] + 1
        print("")
        print("pour les produits de la catégorie ", convertNutriscore(i, "nutriscore"), "(nutriscore), il y a :")
        for j in range(len(list_nova)):
            percent = "{:.2f}".format(list_nova[j] / len(list_nutriscore) * 100)
            print(list_nova[j], "(", percent, "%) produits de la categorie nova ", j+1)
 
# pour chaque categorie nova, renvoie la répartition du nutriscore des produits
def compareNovaNutriscore(list_db):
    for i in range(1, 5):
        list_nova = getListByScore(i, "nova", list_db)
        list_nutriscore = [0,0,0,0,0]
        for j in range(len(list_nova)):
            value = int(list_nova[j]["nutriscore"])
            list_nutriscore[value-1] = list_nutriscore[value-1] + 1
        print("")
        print("pour les produits de la categorie ", i, "(nova), il y a :")
        for j in range(4, -1, -1):
            percent = 0;
            if(len(list_nova) != 0):
                percent = "{:.2f}".format(list_nutriscore[j] / len(list_nova) * 100)
            print(list_nutriscore[j], "(", percent, "%) produits de la categorie nutriscore ", convertNutriscore(j+1, "nutriscore"))


# pour chaque categorie nutriscore, donne la répartition des feux sur la catégorie
def compareNutriscoreFeux(list_db):
    for i in range(5, 0, -1):   
        list_nutriscore = getListByScore(i, "nutriscore", list_db)
        list_feux = [0,0,0]
        for j in range(len(list_nutriscore)):
            for k in range(4):    
                critere_name = getCritereNameByNumber(k)
                color = feuxTricolore(list_nutriscore[j], critere_name)
                if(color == "green"):
                    list_feux[0] = list_feux[0] + 1
                elif(color == "orange"):
                    list_feux[1] = list_feux[1] + 1
                elif(color == "red"):
                    list_feux[2] = list_feux[2] + 1
        print("pour les produits de la categorie ", convertNutriscore(i, "nutriscore"), "(nutriscore), il y a : ")   
        total = list_feux[0] + list_feux[1] + list_feux[2]
        for j in range(3):
            color = "";
            if(j == 0):
                color = "vert"
            elif(j == 1):
                color = "orange"
            elif(j == 2):
                color = "rouge"
            percent = "{:.2f}".format(list_feux[j] / total * 100)
            print(list_feux[j], " (", percent ,"%) feux ", color)
        print("")

# pour chaque categorie nutriscore, donne le nombre d'aliments ayant au moins 1 feu de la categorie donnée
def nutriscoreByColor(list_db, colorToSearch, numberToReach):
    for i in range(5, 0, -1):
        list_nutriscore = getListByScore(i, "nutriscore", list_db)
        number_of_color = 0
        for j in range(len(list_nutriscore)):
          number_of_color_elements = 0
          for k in range(4):
              critere_name = getCritereNameByNumber(k)
              color = feuxTricolore(list_nutriscore[j], critere_name)
              if(color == colorToSearch):
                  number_of_color_elements = number_of_color_elements + 1
                  if(number_of_color_elements >= numberToReach):
                      number_of_color = number_of_color + 1
                      break
          else:
              continue
        percent = "{:.2f}".format(number_of_color / len(list_nutriscore)  * 100)
        print("pour les ", len(list_nutriscore), " produits de la categorie ", convertNutriscore(i, "nutriscore"), "(nutriscore), il y a : ")  
        print(number_of_color, " (", percent, "%) ayant au moins ", numberToReach, " feu de couleur ", colorToSearch, "\n")
              
                         
def compareNutriscoreYuka(list_db):
    size = len(list_db)
    total_yuka = 0
    total_nutriscore = 0
    total_egalite = 0
    avg_yuka = 0
    avg_nutriscore = 0
    for i in range (size):
        avg_yuka = avg_yuka + list_db[i]['score_yuka']
        avg_nutriscore = avg_nutriscore + list_db[i]['nutriscore']
        result = duelNutriscoreYuka(list_db[i]['nutriscore'], list_db[i]['score_yuka'])
        if(result == "yuka"):
            total_yuka = total_yuka + 1
        elif(result == "nutriscore"):
            total_nutriscore = total_nutriscore + 1
        elif(result == "equals"):
            total_egalite = total_egalite + 1
    percent_yuka = "{:.2f}".format(total_yuka / size * 100)
    percent_nutriscore = "{:.2f}".format(total_nutriscore / size * 100)
    percent_egalite = "{:.2f}".format(total_egalite / size * 100)
    print("il y a un total de ", size, " produits")
    print("la moyenne de note yuka sur les produits est de ", "{:.2f}".format(avg_yuka / size))
    print("la moyenne de note nutriscore sur les produits est de ", "{:.2f}".format(avg_nutriscore / size))
    print("\ndans ", total_yuka, "(", percent_yuka, "%) cas, yuka est plus sévère que nutriscore")
    print("dans ", total_nutriscore, "(", percent_nutriscore, "%) cas, nutriscore est plus sévère que yuka")
    print("dans ", total_egalite,"(", percent_egalite, "%) cas, les deux note sont similaires")
            
def compareYukaNova(list_db):
    for i in range(1, 5):
        score_yuka = 0
        nb_yuka = 0
        list_nova = getListByScore(i, "nova", list_db)
        for j in range(len(list_nova)):
            value = int(list_nova[j]["score_yuka"])
            score_yuka = score_yuka + value
            nb_yuka = nb_yuka + 1
        avg_yuka = 0
        if len(list_nova) > 0:
            avg_yuka = "{:.2f}".format(score_yuka / nb_yuka)
        print("")
        print("pour les ", len(list_nova), " produits de la categorie ", i, "(nova), il y a :")
        print("une moyenne de score des produits yuka de ", avg_yuka)

def getRepartitionBio(list_db):
    nbBio = 0
    size = len(list_db)
    for i in range(size):
        if(list_db[i]['label_bio'] == 'y'):
            nbBio = nbBio + 1
    percent = "{:.2f}".format(nbBio / size * 100)
    notBioPercent = "{:.2f}".format((size - nbBio) / size * 100)
    print("il y a un total de ", size, " produits")
    print(nbBio, "(", percent, "%) produits sont bio")
    print((size-nbBio), "(", notBioPercent, "%) ne sont pas bio")
                 
def compareNutriscoreBio(list_db):
    for i in range(5, 0, -1):
        list_nutriscore = getListByScore(i, "nutriscore", list_db)
        nbBio = 0
        for j in range(len(list_nutriscore)):
            value = list_nutriscore[j]["label_bio"]
            if(value == "y"):
                nbBio = nbBio + 1
        print("")
        print("pour les produits de la catégorie ", convertNutriscore(i, "nutriscore"), "(nutriscore), il y a :")
        percent = "{:.2f}".format(nbBio / len(list_nutriscore) * 100)
        print(nbBio, "(", percent, "%) produits bio")


def compareNovaBio(list_db):
    for i in range(1, 5):
        list_nova = getListByScore(i, "nova", list_db)
        nbBio = 0
        for j in range(len(list_nova)):
            value = list_nova[j]["label_bio"]
            if(value == "y"):
                nbBio = nbBio + 1
        print("")
        print("pour les produits de la categorie ", i, "(nova), il y a :")
        percent = 0
        if(len(list_nova) !=0):
            percent = "{:.2f}".format(nbBio / len(list_nova) * 100)
        print(nbBio, "(", percent, "%) produits bio")
        
def yukaByColor(list_db, colorToSearch, numberToReach):
    total_score = 0
    nb_elements = 0
    for i in range(len(list_db)):
        number_of_color_elements = 0
        for j in range(4):
            critere_name = getCritereNameByNumber(j)
            color = feuxTricolore(list_db[i], critere_name)
            if(color == colorToSearch):
                number_of_color_elements = number_of_color_elements + 1
                if(number_of_color_elements >= numberToReach):
                    total_score = total_score + list_db[i]["score_yuka"]
                    nb_elements = nb_elements + 1
                    break
        else:
            continue
        
    avg_score = "{:.2f}".format(total_score / nb_elements)
    print("la moyenne des produits yuka ayant au moins", numberToReach, "feux de couleur", colorToSearch, "est de", avg_score)

def detailsNutriscoreYuka(list_db, score_used):
    list_score = getListSeverity(list_db, score_used)
    list_criteres = [0, 0, 0, 0, 0, 0]
    for i in range(len(list_score)):
        for j in range(6):
            list_criteres[j] = list_criteres[j] + list_score[i]["criteres"][j]
    print("\npour les produits notés plus sévèrement selon", score_used, "nous avons :")
    for i in range(6):
        avg = "{:.2f}".format(list_criteres[i] / len(list_score))
        print("pour le critère", getCritereNameNovaYuka(i), "la moyenne est de ", avg)