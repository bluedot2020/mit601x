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
L = []
for i in range(10):
    L.append(random.randint(1,30))


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
        