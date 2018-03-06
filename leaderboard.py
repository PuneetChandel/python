# find the ranking on leader board
import sys

def Leaderboard(scores, alice):
    board={}
    results=[]
    
    for a in alice:
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
