# find non divisible subset where sum of any two numbers are non devided by a given number


arr=[1, 3, 4,9, 10,5]
resp=[]
k=5

rem = [0]*k # to store the remianders from 0...k-1 , it will give [0,0,0,0,0]

for x in arr:
    rem[x % k] +=1

# incompatiblle sets are where  arr[x]%k + arr[y]%k is  again divisible by k, like 7%5,8%5 re incompatible
# so we will take max of these incompatible groups and add to final response

resp = 1 if rem[0]!=0 else 0 # for reminder zero we can have only one number from the set
#start from 1 index as 0 is already coounted
i=1
while(i<k-i):
    resp += max(rem[i], rem[k-i]) # max from incompaitble sets
    i+=1
    
if k%2==0:
    resp=resp+1 # if k%2 ==0 we can only take one value from the mid, ex if k =4 , 2+2=4 so we can only take one from that set
    
print(resp)


# sliding window


arr=[1, 3, 4,9, 10, 11, 5, 21, 2]
resp=[]
k=5

for y in range(len(arr)):
    temp=[arr[y]]
    for x in range(y+1,len(arr)):
        lst = list(filter(lambda z : (z+arr[x])%k==0,temp))

        if(len(lst)==0):
            temp.append(arr[x])

    if(len(temp)>len(resp)):
        resp=temp

print(resp)
