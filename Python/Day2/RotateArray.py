"""Rotate an Array by d - Counterclockwise or Left

Given an array of integers arr[] of size n, 
the task is to rotate the array elements to the left by d positions."""



# Approach - 1
# Rotating one element to left on every iteration
# Time complexity is O(n*m)
# Space Complexity is O(1)

def rotateArray(arr,d):
    
    temp=0
    for i in range(d):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
        
        arr[len(arr)-1]=temp
	
# Approach -2 
#  * Using temporary empty array, copying d to n-1 to starting of array 
#  * and 0 to d to end of array 
#  * Time complexity is O(n)
#  * Space Complexity is O(n)
	 
	
def rotateArrayOptimized(arr,d):
    n=len(arr)
    temp=[0]*n
    d%=n
    for i in range(n-d):
        temp[i]=arr[d+i]
    for i in range(d):
        temp[n-d+i]=arr[i]
    for i in range(n):
        arr[i]=temp[i]
	
	
# Reversal Algorithm
#  * Reverse sub array 0 to d and sub array n-d to n
#  * then reverse entire array
#  * Time complexity is O(n)
#  * Space complexity  is O(1)
	 
	
def reversalAlgorithm(arr,d):
    d%=len(arr)
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,len(arr)-1)
    reverseArray(arr,0,len(arr)-1)
def reverseArray(arr,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
	
	
	
# Juggling Algorithm   -> Individual traversing
#  * find gcd(n,d) to find number of iterations to take
#  * copy the values into respective chunks till you reach the starting point
#  * update every time +d to currentIndex
#  * Time complexity is O(n)
#  * Space complexity  is O(1)
	 
def jugglingAlgorithm(arr,d):
    n=len(arr)
    d%=n
    circles=gcd(n,d)
    for i in range(circles):
        startIndexValue=arr[i]
        currentIndex=i
        while True:
            nextIndex=(currentIndex+d)%n
            if nextIndex==i:
                break
            arr[currentIndex]=arr[nextIndex]
            currentIndex=nextIndex
        arr[currentIndex]=startIndexValue
    
def gcd(n, d):
    if n==0:
        return d
    return gcd(d%n,n)

if __name__=="__main__":
    arr= [1,2,3,4,5,6]
    d=10
    # rotateArray(arr,d)
    # rotateArrayOptimized(arr,d)
    # reversalAlgorithm(arr,d)
    jugglingAlgorithm(arr,d)
    print(arr)