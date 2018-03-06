#Diagonal diff ina 2d array
#!/bin/python3


def diagonalDifference(a):
    n=len(a)
    sum1=0
    sum2=0
    
    for x in range(0,len(a)):
        sum1+=a[x][x]
        sum2+=a[n-1][x]
        n-=1

    sum = abs(sum1-sum2)
    
    return sum

