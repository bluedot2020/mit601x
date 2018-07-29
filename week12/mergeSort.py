"""
MIT 601x Edx 
Week 6: Algorithmic Complexity   12. Searching and Sorting Algorithms   
Merge Sort
author: bluedot2020
"""

def merge(left, right, compare):
    """
    Assumes left and right are ordered lists, and compare
    define ordering the elements. 
    Returns a new sorted (by compare) list containing the
    same elements(left+right)
    """
    
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #now we append the rest of the left list if any left 
    while (i < len(left)):
        result.append(left[i])
        i += 1
        
    #same as above for right list
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L, compare = lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering on 
    elements of L
    Returns a new sorted list with the same elements as L"""
    
    if len(L) < 2:
        return L[:]
    else:
        middle = L//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
    
    
    
    
    
    
    