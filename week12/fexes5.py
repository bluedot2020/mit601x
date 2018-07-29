"""
MIT 601x Edx 
Week 6: Algorithmic Complexity   12. Searching and Sorting Algorithms   
Exercise 5 Selection Sort
author: bluedot2020
"""

#Assume L a list of integers
#Selection Sort

def selSort(L):
    for i in range((len(L) - 1)):
        minIndex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndex = j
                minVal = L[j]
            j += 1
        if minIndex != i:
            temp = L[i]
            L[i] = L[minIndex]
            L[minIndex] = temp
            
def newSort(L):
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[j] = temp
                L[i] = L[j]
            j += 1
            
L= [10,2,3,10,9,11]
