'''
NextPermutation
 * 
 * Given an array of integers arr[] representing a permutation (i.e., all elements are unique and 
 * arranged in some order), find the next lexicographically greater permutation by rearranging the elements of the array.
 * If such a permutation does not exist (i.e., the array is the last possible permutation), 
 * rearrange the elements to form the lowest possible order (i.e., sorted in ascending order).
 
'''


'''	NextPermution Algorithm
 * Find the pivot element, (element which is less than right element from the end.
 * Traverse from end to pivot position, find the first greatest number than pivot.
 * swap pivot element with that greatest element.
 * reverse sub array pivot+1 to n
 * if there is no pivot element found reverse the given array and return.
 * Time Complexity is O(n)
 * Space Complexity is O(n)
 '''
class NextPermutation:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        pivot=-1
        for i in range(n-2,-1,-1):
            if  arr[i]<arr[i+1]:
                pivot=i;
                break
        if pivot==-1:
            arr.reverse()
            return
        for i in range(n-1,pivot,-1):
            if arr[i]>arr[pivot]:
                arr[i],arr[pivot]=arr[pivot],arr[i]
                break
        self.reversal(arr,pivot+1,n-1)
    def reversal(self,arr,l,r):
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
            
if  __name__=="__main__":
    arr=[2,4,1,7,5,0]
    n=NextPermutation()
    n.nextPermutation(arr)
    print(arr)