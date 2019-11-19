'''
    Using the dynamic programming for implementing the knapsack problem
    Time complexity of the algorithm is : O(nW) where n is the number of items and W is the capacity of knapsack.
'''

def knapSack(capacity, volume, value, n): 
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]  
    for i in range(n + 1): 
        for w in range(capacity + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif volume[i-1] <= w: 
                K[i][w] = max(value[i-1] + K[i-1][w-volume[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 

    for i in range(n+1):
        for j in range(capacity+1):
            print(K[i][j], end=" ")
        print()
    return K[n][capacity] 
  
# Driver program to test above function 
try_count=0
while(try_count < 5):
    try:
        try_count+=1
        value=list(map(int,input("Enter the list of value :").split(' ')))
        volume=list(map(int,input("Enter the list of volume :").split(' ')))
        capacity=int(input("Enter the total knapsack capacity :"))
        if(len(value)!=len(volume)):
            print("Length of value and volumne parameter doesn't matches")
        else:
            n = len(value) 
            break
    
    except:
        print("Enter valid integer")
        

print(knapSack(capacity, volume, value, n)) 