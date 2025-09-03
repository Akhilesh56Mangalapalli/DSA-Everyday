'''
 * Maximum Subarray Sum - Kadane's Algorithm

 * Given an integer array arr[], find the subarray (containing at least one element) 
 * which has the maximum possible sum, and return that sum.
 * Note: A subarray is a continuous part of an array.
'''

class MaximumSum:

    '''
    Brute force Approach
	 * use 1st loop to start with every element in array
	 * add every other elements on each iteration and track maximum sum
	 * Time Complexity is O(n^2)
	 * Space Complexity is O(1)
    '''
    def maximumSum(self,arr):
        n=len(arr)
        res=arr[0]
        for i in range(n):
            sum=arr[i]
            for j in range(i+1,n):
                sum+=arr[j]
                res=max(res,sum)
        return res
    
    '''
    Kadane's Algorithm
	 * 	Check the element adding to current max giving greater than that element
	 * 	if gives update it as current max, if not take that element as current max
	 * 	simultaneously track the resultant max and return in the end
	 * 	Time Complexity is O(n)
	 * 	Space complexity is O(1)
    '''
    def kadaneAlgorithm(self,arr):
        n=len(arr)
        maxEnd=arr[0]
        res=arr[0]
        for i in range(1,n):
            maxEnd=max(maxEnd+arr[i],arr[i])
            res=max(res,maxEnd)
        return res
    

if __name__=="__main__":
    ms=MaximumSum()
    arr=[2, 3, -8, 7, -1, 2, 3]
    print(ms.maximumSum(arr))
    print(ms.kadaneAlgorithm(arr))