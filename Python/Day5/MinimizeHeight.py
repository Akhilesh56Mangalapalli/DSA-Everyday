'''
Minimize the Heights II

Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers 
after you have modified each tower.

Note: It is compulsory to increase or decrease the height by k for each tower. 
After the operation, the resultant array should not contain any negative integers.
'''

class MinimizeHeight:

    '''
    Draw and Understand the number line
	 * 	take a random possible position of i and analyze where are chances of maxima and minima
	 * 	Time Complexity is O(nlogn)
	 * 	Space Complexity is O(n)   because we are sorting the array
    '''
    def minimizeHeight(self, arr, k):
        n=len(arr)
        arr.sort()
        res=arr[n-1]-arr[0]
        for i in range(1,n):
            if (arr[i]-k)<0:
                continue
            minH=min(arr[0]+k,arr[i]-k)
            maxH=max(arr[n-1]-k,arr[i-1]+k)
            res=min(res,maxH-minH)
        return res
        
if __name__=="__main__":
    heights=[3, 9, 12, 16, 20]
    k=3
    mht=MinimizeHeight()
    print(mht.minimizeHeight(heights,k))