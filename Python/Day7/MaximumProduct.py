'''
Maximum Product Subarray

Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a subarray of arr[].
Note: It is guaranteed that the answer fits in a 32-bit integer.
'''

class MaximumProduct:
    '''
    Brute Force Approach
    finding all possible products and keep tracking maximum product
    Time complexity is O(n^2)
    Space Complexity is O(1)
    '''
    def maximumProduct(self,arr):
        n=len(arr)
        res=arr[0]
        for i in range(n):
            mul=arr[i]
            for j in range(i+1,n):
                mul*=arr[j]
                res=max(res,mul)
        return res
    
    '''
    Greedy Min-Max Algorithm
    Keeping track of both minimum product and maximum product
    There are situations where both negative give greater max then current
    and find maximum product using both minimum and maximum then return
    Time complexity is O(n)
    Space Complexity is O(1)
    '''
    def greedyMinMax(self,arr):
        n=len(arr)
        current_minimum=arr[0]
        current_maximum=arr[0]
        res=arr[0]
        for i in range(1,n):
            temp=max(arr[i],current_maximum*arr[i],current_minimum*arr[i])
            current_minimum=min(arr[i],current_maximum*arr[i],current_minimum*arr[i])
            current_maximum=temp
            res=max(res,current_maximum)
        return res
    
    '''
    Traversal Approach | Even or Odd 
    if there are even number of negative elements, then multiply complete array gives max product
    if there are odd  number of negative elements, then we need ignore one negative element
    to make number of negative numbers into even so that we max product
    it may be first negative number or last negative number in the array
    One of them gives maximum product, to find that
    we need traverse in both directions in one loop
    find max products with different variables
    if '0' is found in the traversal, change the subarray
    i.e., current product is updated as 1 (for both left and right traversal)     
    keep track of maximum product and return
    Time complexity is O(n)
    Space Complexity is O(1)
    '''
    def traversalApproach(self,arr):
        n=len(arr)
        res=float('-inf')
        leftToright=arr[0]
        rightToleft=arr[0]
        for i in range(1,n):
            if leftToright==0:
                leftToright=1
            if rightToleft==0:
                rightToleft=1
            leftToright*=arr[i]
            j=n-i-1
            rightToleft*=arr[j]
            res=max(res,leftToright,rightToleft)
        return res


if __name__=="__main__":
    mp=MaximumProduct()
    arr1=[-2, 6, -3, -10, 0, 2]
    arr2=[-1, -3, -10, 0, 6]
    arr3=[2, 3, 4] 
    print(mp.maximumProduct(arr1))
    print(mp.greedyMinMax(arr2))
    print(mp.traversalApproach(arr3))