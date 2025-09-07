'''
Maximum Circular Subarray Sum

Given a circular array arr[], find the maximum sum of any non-empty subarray. 
A circular array allows wrapping from the end back to the beginning.
Note: A subarray may wrap around the end and continue from the beginning, 
forming a circular segment.
'''

class CircularMaxSum:
    '''
    Brute force Approach
    traverse circularly, when index reached n, make it zero and continue
    or use % operator => j=j%n
    Time complexity is O(n^2)
    Space Complexity is O(1) 
    '''
    def maxSum(self,arr):
        n=len(arr)
        res=arr[0]
        for i in range(n):
            sum=arr[i]
            # iterating n-1 time, using j variable to make circular traverse
            # we can also use modular '% operator to make circular traversal
            j=i+1
            for _ in range(n-1):
                if j==n:
                    j=0
                sum+=arr[j]
                j+=1
                res=max(res,sum)
        return res
    
    '''
    PrefixSum and Suffix Approach
    Here take an array of n+1 size and find suffix from (n-1)th position
    find the prefix sum and parallelly find the maximum sum using kadane's Algorithm
    summation of (i)th prefix value and (i+1)th suffix value gives the circular sum
    keep track of circular max, and normal max using kadane's algorithm
    return max between circular sum and normal sum
    Time Complexity is O(n)
    Space Complexity is O(n)
    '''
    def prefixSum(self,arr):
        n=len(arr)
        suffix_array=[0]*(n+1)
        suffix_array[n-1]=arr[n-1]
        suffix_sum=arr[n-1]
        prefsum=0
        currsum=0
        normal_sum=arr[0]
        circular_sum=arr[0]
        for i in range(n-2,-1,-1):
            suffix_sum+=arr[i]
            sufmax=max(suffix_array[i+1],suffix_sum)
            # suffix array filling max sum values
            suffix_array[i]=sufmax
        for i in range(n):
            prefsum+=arr[i]
            circular_sum=max(circular_sum,suffix_array[i+1]+prefsum)

            #kadane's Alorithm
            currsum=max(arr[i],arr[i]+currsum)
            normal_sum=max(arr[i],currsum)
        return max(circular_sum,normal_sum)
    
    '''
    Kadane's Algorithm | Best Approach
    total_Sum=maximum_Sum+minimum_Sum
    find the minimum_sum and maximum sum using kadane's Algorithm 
    and find total sum of the array
    return totalSum-minimumSum which results maximum circular sum
    if minimum_kadane_sum is equal to total sum then return maximumKadaneSum
    Time complexity is O(n)
    Space Complexity is O(1)
    '''

    def minKadaneAlg(self,arr):
        n=len(arr)
        prefixsum=0
        minsum=0
        maxsum=0
        kadanemin=0
        kadanemax=float('-inf')
        for i in range(n):
            prefixsum+=arr[i]
        for i in range(n):
            minsum=min(arr[i],minsum+arr[i])
            kadanemin=min(kadanemin,minsum)
            # normal kadane max
            maxsum=max(arr[i],maxsum+arr[i])
            kadanemax=max(kadanemax,maxsum)
        if prefixsum==kadanemin:
            return kadanemax
        
        return prefixsum-kadanemin



if __name__=="__main__":
    arr=[8, -8, 9, -9, 10, -11, 12]
    arr2=[10, -3, -4, 7, 6, 5, -4, -1]
    arr3=[5, -2, 3, 4]
    arr4=[-1,-2,-3]
    cms=CircularMaxSum()
    print(cms.maxSum(arr3))
    print(cms.prefixSum(arr))
    print(cms.minKadaneAlg(arr))

     
