#!/bin/python3

import sys

def solve(grades):
    gr=[]
    for g in grades:
        if g >= 38:
            m=g%5
            if m<3 :
                gr.append(g)
            else:
                g=g+(5-m)
                gr.append(g)
        else:
            gr.append(g)
        
    return gr
    
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
