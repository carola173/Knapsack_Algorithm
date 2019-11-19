# Knapsack_Algorithm
NP -Hard - Knapsack algorithm implementatioen using Dynamic Programming in Python Language.

This program accepts the value and volumne matrix from the user of same size and also prompt the user to enter the total wanted capacity on which the Knapsack algorithm is to run.

Testing the algorithm with the following values:
    value=[7 9 5 12 14 6 12]
    Volume=[3 4 2 6 7 3 5]
    Capacity = 15
    
    Output = 34

Need to find out the products of maximum total value such that the sum of their volumes is at most 15

Time complexity of the algorithm is : O(nW) where n is the number of items and W is the capacity of knapsack.

when the numbe of input size increases so is the complexity. Complexity of the current algorithm is more than that of the Google OR-Tools. 
Since in is implemented using dynamic programming, so the space complexity increses as the O(nW). Space complexity can be improved by using only 1D Vector rather than the matrix.

There are som neural network using which we can improve this algorithm, like given in the link:
https://towardsdatascience.com/neural-knapsack-8edd737bdc15

This requires the proper test data to be created and then training the Neural network.
