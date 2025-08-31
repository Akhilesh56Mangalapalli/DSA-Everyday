"""
Given an array, shift all the zero elements to the end 
with out effecting the order of the non zero elements
in place [dont use extra array]
"""

"""
Approach -1 
Copying  non zero elements to its preceeding zero elements position
Two loops 1 -> copying non zeros
          2 -> assigning remaining with zeros

Time Complexity is Worst case O(2n) ==> O(n)
Space Complexity is O(1)
"""

# def shiftZerostoEnd(arr):
#     n=len(arr)
#     count=0
#     for i in range(n):
#         if arr[i]!=0:
#             arr[count]=arr[i]
#             count+=1
#     while count<n:
#         arr[count]=0
#         count+=1
#     return arr
# if __name__=="__main__":
#     arr=[1,2,0,5,8,0,9,0]
#     print(shiftZerostoEnd(arr))


"""
Approach - 2 
Swapping  non zero elements to its preceeding zero elements position
One loops -> swapping non zeros

Time Complexity is O(n)
Space Complexity is O(1)
"""

def shiftZerostoEnd(arr):
    n=len(arr)
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count],arr[i]=arr[i],arr[count]
            count+=1
  
    return arr
if __name__=="__main__":
    arr=[1,2,0,5,8,0,9,0]
    # arr=[0,0,0,0,0]
    print(shiftZerostoEnd(arr))

