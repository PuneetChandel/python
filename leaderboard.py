# find the ranking on leader board
import sys


def getboard1(scores,newscores):    
 results=[]
    scores=list(set(scores))
    scores.sort(reverse=True)
    idx=0
    for a in newscores:
        idx=0
        for x in range(0,len(scores)):
            if a < scores[x] :
                idx+=1
        scores.insert(idx,a)
        results.append(idx+1)
    return results


def getboard(scores, newscores):
    board={}
    results=[]
    
    for a in newscores:
        idx=0
        for x in range(0,len(scores)):
            if a < scores[x]:
                idx+=1
        scores.append(0)

        for x in range(len(scores)-1,idx,-1):
            temp=scores[x]
            scores[x]=scores[x-1]
            scores[x-1]=temp
        scores[idx]=a
        
        i=0
        for s in scores:
                try:
                    val= board[s]
                except KeyError as e:
                    i+=1
                    board[s]=i
                                              
        results.append(board[a])
        board={}
    return results



