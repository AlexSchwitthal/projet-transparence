# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:05:30 2020

@author: boris
"""

#nutriscore de A à E ie 5 à 1
A = 5
E = 1
import xlrd
import xlwt
from datetime import datetime

def readDB1():
    loc = ("Datasets/OpenFood_Petales.xlsx")
 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    list_cereals_labels = {}
    
    list_cereals_labels['product_name']=sheet.row_values(0)[0]
    list_cereals_labels['nutriscore']=sheet.row_values(0)[2]
    list_cereals_labels['criteres']=[]
    list_cereals_labels['criteres'].append(sheet.row_values(0)[3])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[4])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[5])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[8])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[7])
    list_cereals_labels['criteres'].append(sheet.row_values(0)[6])

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
    #print(list_cereals_labels)    
    return list_cereals, list_cereals_labels

def readDB2():
    loc = ("Datasets/DB2.xlsx")
 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    i = 0
    label_OFD = {}
    label_OFD['product_name']=sheet.row_values(i)[1]
    label_OFD['groupe']=sheet.row_values(i)[5]
    label_OFD['sous-groupe']=sheet.row_values(i)[6]
    label_OFD['nutriscore']=sheet.row_values(i)[3]
    label_OFD['nova']=sheet.row_values(i)[4]
    label_OFD['nb_additifs']=sheet.row_values(i)[2]
    label_OFD['criteres']=[]
    label_OFD['criteres'].append(sheet.row_values(i)[7])
    label_OFD['criteres'].append(sheet.row_values(i)[8])
    label_OFD['criteres'].append(sheet.row_values(i)[9])
    label_OFD['criteres'].append(sheet.row_values(i)[10])
    label_OFD['criteres'].append(sheet.row_values(i)[11])
    label_OFD['criteres'].append(sheet.row_values(i)[12])
    label_OFD['criteres_feux'] = []
    label_OFD['criteres_feux'].append(sheet.row_values(i)[13])
    label_OFD['criteres_feux'].append(sheet.row_values(i)[14])
    label_OFD['criteres_feux'].append(sheet.row_values(i)[15])
    label_OFD['criteres_feux'].append(sheet.row_values(i)[16])
    
    list_items =[]
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0 
    count5 = 0
    for i in range(1, sheet.nrows):
        
        item = {}

        item['product_name']=sheet.row_values(i)[1]
        item['groupe']=sheet.row_values(i)[5]
        item['sous-groupe']=sheet.row_values(i)[6]
        item['nutriscore']=102-ord(sheet.row_values(i)[3])
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
        
        item['nova']=sheet.row_values(i)[4]
        item['nb_additifs']=sheet.row_values(i)[2]
        item['criteres']=[]
        item['criteres'].append(sheet.row_values(i)[7])
        item['criteres'].append(sheet.row_values(i)[8])
        item['criteres'].append(sheet.row_values(i)[9])
        item['criteres'].append(sheet.row_values(i)[10])
        item['criteres'].append(sheet.row_values(i)[11])
        item['criteres'].append(sheet.row_values(i)[12])
        item['criteres_feux'] = []
        item['criteres_feux'].append(sheet.row_values(i)[13])
        item['criteres_feux'].append(sheet.row_values(i)[14])
        item['criteres_feux'].append(sheet.row_values(i)[15])
        item['criteres_feux'].append(sheet.row_values(i)[16])
        list_items.append(item)
        
    print(count1, count2, count3, count4, count5)
    print(label_OFD)
    return list_items, label_OFD

def readDB3():
    loc = ("Datasets/DB3.xlsx")
 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    i = 0
    label_OFD = {}
    label_OFD['product_name']=sheet.row_values(i)[1]
    label_OFD['groupe']=sheet.row_values(i)[5]
    label_OFD['sous-groupe']=sheet.row_values(i)[6]
    label_OFD['nutriscore']=sheet.row_values(i)[3]
    label_OFD['nova']=sheet.row_values(i)[4]
    label_OFD['nb_additifs']=sheet.row_values(i)[2]
    label_OFD['criteres']=[]
    label_OFD['criteres'].append(sheet.row_values(i)[7])
    label_OFD['criteres'].append(sheet.row_values(i)[8])
    label_OFD['criteres'].append(sheet.row_values(i)[9])
    label_OFD['criteres'].append(sheet.row_values(i)[10])
    label_OFD['criteres'].append(sheet.row_values(i)[11])
    label_OFD['criteres'].append(sheet.row_values(i)[12])
    label_OFD['criteres_feux'] = []
    label_OFD['criteres_feux'].append(sheet.row_values(i)[13])
    label_OFD['criteres_feux'].append(sheet.row_values(i)[14])
    label_OFD['criteres_feux'].append(sheet.row_values(i)[15])
    label_OFD['criteres_feux'].append(sheet.row_values(i)[16])
    label_OFD['score_yuka']=sheet.row_values(i)[17]
    label_OFD['label_bio']=sheet.row_values(i)[18]
    list_items =[]
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0 
    count5 = 0
    for i in range(1, sheet.nrows):
        
        item = {}

        item['product_name']=sheet.row_values(i)[1]
        item['groupe']=sheet.row_values(i)[5]
        item['sous-groupe']=sheet.row_values(i)[6]
        item['nutriscore']=102-ord(sheet.row_values(i)[3])
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
        
        item['nova']=sheet.row_values(i)[4]
        item['nb_additifs']=sheet.row_values(i)[2]
        item['criteres']=[]
        item['criteres'].append(sheet.row_values(i)[7])
        item['criteres'].append(sheet.row_values(i)[8])
        item['criteres'].append(sheet.row_values(i)[9])
        item['criteres'].append(sheet.row_values(i)[10])
        item['criteres'].append(sheet.row_values(i)[11])
        item['criteres'].append(sheet.row_values(i)[12])
        item['criteres_feux'] = []
        item['criteres_feux'].append(sheet.row_values(i)[13])
        item['criteres_feux'].append(sheet.row_values(i)[14])
        item['criteres_feux'].append(sheet.row_values(i)[15])
        item['criteres_feux'].append(sheet.row_values(i)[16])
        item['score_yuka']=sheet.row_values(i)[17]
        item['label_bio']=sheet.row_values(i)[18]
        list_items.append(item)
        
    print(count1, count2, count3, count4, count5)
    print(label_OFD)
    return list_items, label_OFD

def writeDB(name, label, list_items):

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('test')
    index = 0
    for key ,value in label.items():
        if key == 'criteres':
            for i in range(len(label['criteres'])):
                sheet.write(0, index, label['criteres'][i])
                index += 1
        elif key == 'criteres_feux':
            for i in range(len(label['criteres_feux'])):
                sheet.write(0, index, label['criteres_feux'][i])
                index += 1        
        else :
            sheet.write(0, index, key)
            index += 1
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
            elif key == 'criteres_feux':
                for i in range(len(item['criteres_feux'])):
                    sheet.write(count, index, item['criteres_feux'][i])
                    index += 1
            else :
                sheet.write(count, index, value)
                index += 1
        count += 1        
    id = datetime.now().strftime("%d_%m_%H_%M")            
    workbook.save(name + '_' + id + '.xls')