'''
Majority Element - Most Than n/3
 * Given an array arr[] consisting of n integers, 
 * the task is to find all the array elements which occurs more than floor(n/3) times.
 * Note: The returned array of majority elements should be sorted.

Since we are taking >(n/3) we will have only 2 elements has majority
if >(n/2) then only 1 element has majority
if >(n/4) then 3 elements has majority
'
'
if >(n/k) then (k-1) elements has majority
'''

class MajorityElement:

    '''
    Approach - 1
	 * Using HashMap or Dictionary 
	 * make the array as key:value pair where keys are distinct elements and values are frequency
	 * iterate over the keys and check values > floor(n/3 if true add them to list
	 * if list has 2 elements, check for sorting and return
	 * Time Complexity O(n)
	 * Space Complexity O(n) ==> for HashMap in worst case
	 
    '''
    def majorityElement(self, arr):
        # code here
        dict={}
        res=[]
        for element in arr:
            dict[element]=dict.get(element,0)+1          
        for key,value in dict.items():
            if value>len(arr)//3:
                res.append(key)
        if len(res)==2 and res[1]<res[0]:
            res[0],res[1]=res[1],res[0]
        return res
    
    '''
    Approach - 2
	 * Boyer Moore's Voting Algorithm
	 * take 2 elements as candidates and 2 counters
	 * follow conditions and find 2 candidates/elements which might have majority
	 * check >n//3 condition, if true add to ArrayList to return
	 * if list has 2 elements, check for swapping and return
	 * Time Complexity is O(n)
	 * Space complexity is O(1)
    '''
    def findMajority(self,arr):
        n = len(arr)
        ele1, ele2 = -1, -1
        cnt1, cnt2 = 0, 0

        for ele in arr:
            if ele1 == ele:
                cnt1 += 1
            elif ele2 == ele:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = ele
                cnt1 += 1
            elif cnt2 == 0:
                ele2 = ele
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        res = []
        cnt1, cnt2 = 0, 0

        for ele in arr:
            if ele1 == ele:
                cnt1 += 1
            if ele2 == ele:
                cnt2 += 1

        if cnt1 > n / 3:
            res.append(ele1)
        if cnt2 > n / 3 and ele1 != ele2:
            res.append(ele2)

        if len(res) == 2 and res[1] < res[0]:
            res[0], res[1] = res[1], res[0]

        return res

if __name__=="__main__":
    arr=[2, 2, 3, 1, 3, 2, 1, 1]
    m=MajorityElement()
    print(m.majorityElement(arr))
    print(m.findMajority(arr))