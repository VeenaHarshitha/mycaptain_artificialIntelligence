# -*- coding: utf-8 -*-
"""
Created on Thu May  7 06:46:51 2020

@author: Veena
"""

#1Assigning elements to different lists
lst1 = [11, 22, 33, 44]
lst2 = [10, 20, 30, 40]
lst1.append(55)
lst2.append(50)
print('List1 after appending element:',lst1)
print('List2 after appending element:',lst2)
lst1.insert(2, 66)
lst2.insert(3, 60)
print('List1 after inserting element:',lst1)
print('List2 after inserting element:',lst2)
lst3 = []
lst3.append(20)
lst3.append(40)
lst3.append(60)
print(lst3)


#Accessing elements from a tuple
tup1 = (2,"c","str",3)
print('Tuple is:',tup1)
print(tup1[0:2])
print('Length of tuple 1 is:',len(tup1))
print(tup1[2])


#Deleting different dictionary elements
d = dict()
d['181'] = 'CSE'
d['182'] = 'ECE'
d['183'] = 'ISE'
d['184'] = 'EEE'
print('The dictionary is:',d)
print('The keys in dictionary are:',d.keys())
print('The values in dictionary are:',d.values())
del d['183']
print('The dictionary after deleting an element is:',d)
d['185'] = 'AI'
print('The dictionary is:',d)
del d['181']
print('The dictionary after deleting an element is:',d)