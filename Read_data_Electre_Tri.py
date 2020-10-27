# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#nutriscore de A à E ie 5 à 1
A = 5
E = 1
import xlrd
import xlwt
from datetime import datetime

list_cereals_labels = {}
def readDB1():
    loc = ("Datasets/OpenFood_Petales.xlsx")
 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    
    list_cereals_labels['product_name']=sheet.row_values(0)[0]
    list_cereals_labels['nutriscore']=sheet.row_values(0)[2]
    list_cereals_labels['criteres']=[]
    list_cereals_labels['criteres'].append(sheet.row_values(0)[3])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[4])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[5])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[8])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[7])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[6])


    #print(list_cereals_labels)
    list_cereals =[]
    for i in range(1, sheet.nrows):
        cereal = {}
        cereal['product_name']=sheet.row_values(i)[0]
        cereal['nutriscore']=102-ord(sheet.row_values(i)[2])
        cereal['criteres']=[]
        cereal['criteres'].append(sheet.row_values(i)[3])
        cereal['criteres'].append(sheet.row_values(i)[4])
        cereal['criteres'].append(sheet.row_values(i)[5])
        cereal['criteres'].append(sheet.row_values(i)[8])
        cereal['criteres'].append(sheet.row_values(i)[7])
        cereal['criteres'].append(sheet.row_values(i)[6]) 
        list_cereals.append(cereal)
    return list_cereals

label = {}
def readOFD_SD():
    loc = ("Datasets/openfoodfacts_simplified_database.xlsx")
 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    i = 0
    
    label['product_name']=sheet.row_values(i)[0]
    label['nutriscore']=sheet.row_values(i)[8]
    label['nova']=sheet.row_values(i)[9]
    label['nb_additifs']=sheet.row_values(i)[6]
    label['criteres']=[]
    label['criteres'].append(sheet.row_values(i)[12])
    label['criteres'].append(sheet.row_values(i)[13])
    label['criteres'].append(sheet.row_values(i)[14])
    label['criteres'].append(sheet.row_values(i)[17])
    label['criteres'].append(sheet.row_values(i)[16])
    label['criteres'].append(sheet.row_values(i)[15]) 
    
    list_items =[]
    list_false=[]
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0 
    count5 = 0
    for i in range(1, sheet.nrows):
        valid = True
        item = {}
        if len(str(sheet.row_values(i)[0])) == 0:
            sheet.row_values(i)[0]
            valid = False
            
        if len(str(sheet.row_values(i)[8])) == 0:
            sheet.row_values(i)[8]
            valid = False
        if len(str(sheet.row_values(i)[9])) == 0:
            sheet.row_values(i)[9]
            valid = False
        if len(str(sheet.row_values(i)[6])) == 0:
            sheet.row_values(i)[6]
            valid = False
        if len(str(sheet.row_values(i)[12])) == 0:
            sheet.row_values(i)[12]
            valid = False
        if len(str(sheet.row_values(i)[13])) == 0:
            sheet.row_values(i)[13]
            valid = False
        if len(str(sheet.row_values(i)[14])) == 0:
            sheet.row_values(i)[14]
            valid = False
        if len(str(sheet.row_values(i)[17])) == 0:
            sheet.row_values(i)[17]
            valid = False
        if len(str(sheet.row_values(i)[16])) == 0:
            sheet.row_values(i)[16]
            valid = False
        if len(str(sheet.row_values(i)[15])) == 0:
            sheet.row_values(i)[15]
            valid = False
        if not valid:
            list_false.append(item)
            
        if valid :
            item['product_name']=sheet.row_values(i)[0]
            item['nutriscore']=102-ord(sheet.row_values(i)[8])
            if item['nutriscore'] == 1:
                count1 += 1
            if item['nutriscore'] == 2:
                count2 += 1 
            if item['nutriscore'] == 3:
                count3 += 1
            if item['nutriscore'] == 4:
                count4 += 1
            if item['nutriscore'] == 5:
                count5 += 1
            item['nova']=sheet.row_values(i)[9]
            item['nb_additifs']=sheet.row_values(i)[6]
            item['criteres']=[]
            item['criteres'].append(sheet.row_values(i)[12])
            item['criteres'].append(sheet.row_values(i)[13])
            item['criteres'].append(sheet.row_values(i)[14])
            item['criteres'].append(sheet.row_values(i)[17])
            item['criteres'].append(sheet.row_values(i)[16])
            item['criteres'].append(sheet.row_values(i)[15])
            list_items.append(item)
    #print(count1, count2, count3, count4, count5)
    #print(len(list_false))
    return list_items


def writeDB(name, label, list_items):

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('test')
    index = 0
    for key ,value in label.items():
        if key == 'criteres':
            for i in range(len(label['criteres'])):
                sheet.write(0, index, label['criteres'][i])
                index += 1
        else :
            sheet.write(0, index, key)
            index += 1
    sheet.write(0, index, 'pessimist_score')
    sheet.write(0, index+1, 'optimist_score')
    count = 1
    for item in list_items:
        index = 0
        for key ,value in item.items():
            if key == 'nutriscore' or key == 'pessimist_score' or key == 'optimist_score':
                sheet.write(count, index, chr(102-value))
                index += 1
            elif key == 'criteres':
                for i in range(len(item['criteres'])):
                    sheet.write(count, index, item['criteres'][i])
                    index += 1
            else :
                sheet.write(count, index, value)
                index += 1
        count += 1        
    id = datetime.now().strftime("%d_%m_%H_%M")            
    workbook.save(name + '_' + id + '.xls')
      

#print(list_cereals_labels) 
#ordonné de critère 1 à critère 6
#aliment = [7,5,7,5,2,2]
#ordonné de critère 1 à critère 6
list_poids = [1,1,1,1,2,2]
#ordonné de profil b6 à profil b1 et de critère 1 à critère 6
list_profils = [[100,0,0,0,100,100],
                [1550,11,0.8,0.3,10,11],
                [1650,14,1,0.4,7,8],
                [1750,17,1.7,0.5,4,5],
                [1850,20,4,0.6,3,2.5],
                [10000,100,100,100,0,0]]

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
       
def defineElectreScore(list_aliments, list_poids, list_profils, seuil):
    for aliment in list_aliments:
        aliment['pessimist_score'] = pessimisticMajoritySorting(aliment['criteres'], list_profils, list_poids, seuil)
        aliment['optimist_score'] = optimisticMajoritySorting(aliment['criteres'], list_profils, list_poids, seuil)
        #if aliment['optimist_score'] != aliment['pessimist_score']:
           # print(aliment['product_name'])
           # print(aliment['nutriscore'])
           # print(aliment['pessimist_score'])
           # print(aliment['optimist_score'])
 
list_items = readOFD_SD() 
defineElectreScore(list_items, list_poids, list_profils, 0.51)  
#writeDB('Datasets/DB2', label, list_items) 

list_cereals = readDB1()  
defineElectreScore(list_cereals, list_poids, list_profils, 0.51)  
#writeDB('Datasets/DB1', list_cereals_labels, list_cereals) 

#print("pessimistic")
#print(pessimisticMajoritySorting(aliment, list_profils, list_poids, 0.5)) 
#print("optimistic")
#print(optimisticMajoritySorting(aliment, list_profils, list_poids, 0.5))        
        