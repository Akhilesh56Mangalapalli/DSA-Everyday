"""
Given an array , find the second largest element in it and return the element
"""

"""
Approach - 1
Sorting and returning secondLargest
Time complexity is O(nlogn)
Space complexity is O(1)
"""

# def secondLargest(arr):
#     n=len(arr)
#     arr.sort()
#     for i in range(n-2,-1,-1):
#         if arr[i]<arr[n-1]:
#             return arr[i]
#     return -1
# if __name__=="__main__":
#     arr=[2,8,9,5,7,0,5]
#     print(secondLargest(arr))

"""
Approach - 2
2 loops , 1 for largest and another for second largest
Time complexity is O(2n) => O(n)
Space complexity is O(1)
"""

# def secondLargest(arr):
#     n=len(arr)
#     largest=float('-inf')
#     secondLargest=float('-inf')
#     for i in range(n):
#         if arr[i]>largest:
#             largest=arr[i]
#     for i in range(n):
#         if arr[i]>secondLargest and arr[i]<largest:
#             secondLargest=arr[i]
#     if secondLargest==float('-inf'):
#         return -1
#     else:
#         return secondLargest
# if __name__=="__main__":
#     # arr=[2,8,9,5,7,0,5]
#     arr=[10,10,10]
#     print(secondLargest(arr))


"""
Approach - 3
One loop , tracking secondLargest when finding largest
time complexity is O(n)
space Complexity is O(1)
"""

def secondLargest(arr):
    n=len(arr)
    largest=float('-inf')
    secondLargest=float('-inf')
    for i in range(n):
        if arr[i]>largest:
            secondLargest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>secondLargest:
            secondLargest=arr[i]
 
    if secondLargest==float('-inf'):
        return -1
    else:
        return secondLargest
if __name__=="__main__":
    arr=[2,8,9,5,7,0,5]
    # arr=[10,10,10]
    print(secondLargest(arr))