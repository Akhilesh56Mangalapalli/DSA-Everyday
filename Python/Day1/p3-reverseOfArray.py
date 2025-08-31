"""
Given an Integer array, Reverse the array in place[not using extra array]
"""

"""
Approach - 1
Two pointers left and right
Swapping first and last elements and updating left and right
Time complexity is O(n/2) => O(n)
Space complexity is O(1)
"""
# def reverseArray(arr):
#     n=len(arr)
#     left=0
#     right=n-1
#     while left<right:
#         arr[left],arr[right]=arr[right],arr[left]
#         left+=1
#         right-=1
#     return arr
# if __name__=="__main__":
#     arr=[1,2,3,4,5]
#     print(reverseArray(arr))


"""
Approach - 2
Swapping with temp Variable
Time complexity is O(n/2) => O(n)
Space complexity is O(1)
"""
# def reverseArray(arr):
#     n=len(arr)
#     temp=0
#     for i in range(n//2):
#         temp=arr[i]
#         arr[i]=arr[n-i-1]
#         arr[n-i-1]=temp
#     return arr
# if __name__=="__main__":
#     arr=[1,2,3,4,5]
#     print(reverseArray(arr))

"""
Approach - 3
Using built-in function
Time complexity is O(n)
Space complexity is O(1)
"""

def reverseArray(arr):
    arr.reverse()
    return arr
if __name__=="__main__":
    arr=[1,2,3,4,5]
    print(reverseArray(arr))