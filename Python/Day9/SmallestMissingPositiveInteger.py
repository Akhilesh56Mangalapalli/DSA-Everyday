'''
Smallest Missing Positive Number

Given an unsorted array arr[] with both positive and negative elements, 
find the smallest positive number missing from the array.
'''


class SmallestMissingPositiveInteger:
    '''
    Basic Idea:
    find max number 
    iterate to maximum number or to length of the array from 1
    check i in array, if not found then return
    Time Complexity is O(n)
    Space Complexity is O(1)
    '''
    def smallestMissingInt(self,arr):
     
        # This is the easier way in python
        # for i in range(1,n+1):
        #     if i not in arr:
        #         return i
        # return n+1

        n=len(arr)
        # maxi=max(arr) also can be used to find max
        maxi=arr[0]
        for i in range(1,n):
            if maxi>arr[i]:
                continue
            else:
                maxi=arr[i]
        if maxi<0:
            return 1
        for i in range(1,maxi):
            if i not in arr:
                return i
        return maxi+1
    
    '''
    CycleSort Approach
    iterate only over valid cases
    i.e., number lies between 1 and n
    swap if number is not in correct position
    ignore if there are duplicate elements already in position
    after applying sort check which first position is not correctly placed
    return position + 1
    if all placed correctly return n+1
    Time Complexity is O(n)
    Space Complexity is O(1)    
    '''
    def UsingCycleSort(self, arr):
        n=len(arr)
        for i in range(n):
            while 1<=arr[i]<=n and arr[i]!=arr[arr[i]-1]:
                temp=arr[i]
                arr[i]=arr[arr[i]-1]
                arr[temp-1]=temp  
        for i in range(1, n + 1):
            if i != arr[i - 1]:
                return i
        return n + 1
    
if __name__=="__main__":
    smp=SmallestMissingPositiveInteger()
    arr1=[2,-3,4,1,1,7]
    arr2=[5,3,2,5,1]
    arr3=[-8,0,-1,-4,-3]
    arr4=[1,2,3,4,5]
    print(smp.smallestMissingInt(arr1))
    print(smp.UsingCycleSort(arr2))