# Given an array of integers, find and print the maximum number of integers you can select from the array such that 
# the absolute difference between any two of the chosen integers is <=1

import sys

def chooseNumbers(a):
    arr1=[]
    result=[]
    a.sort()    
    for x in range(0,len(a)):
        for y in range(x,len(a)):
            if abs(a[x]-a[y])<=1:
                if len(arr1)>0:
                    if abs(min(arr1)-a[y])<=1:
                         arr1.append(a[y])
                else:
                    arr1.append(a[y])    
        
        if len(arr1)>len(result) or x==0:
            result=arr1
        arr1=[]
    return len(result)    
