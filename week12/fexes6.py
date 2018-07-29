"""
MIT 601x Edx 
Week 6: Algorithmic Complexity   12. Searching and Sorting Algorithms   
Exercise 6 Selection Sort
author: bluedot2020
"""

#Assume L a list of integers
#Selection Sort

import random

#set up L

def genList():
    L = []
    for i in range(10):
        L.append(random.randint(1,30))
    return L

def unique(L):
    result = []
    for i in range(len(L)):
        if L[i] not in result:
            result.append(L[i])
    return result

def mySort(L):
    """L a list of unique elements"""
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1]=temp
        
def newSort(L):
    """L a list with unique elements"""
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
        j += 1