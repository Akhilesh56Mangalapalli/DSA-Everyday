
/*	Majority Element - Most Than n/3
 * Given an array arr[] consisting of n integers, 
 * the task is to find all the array elements which occurs more than floor(n/3) times.
 * Note: The returned array of majority elements should be sorted.

Since we are taking >(n/3) we will have only 2 elements has majority
if >(n/2) then only 1 element has majority
if >(n/4) then only 3 elements has majority
'
'
if >(n/k) then (k-1) elements has majority

 * */

package Arrays.Day3;
import java.util.HashMap;
import java.util.ArrayList;
public class MajorityElement {
	public static void main(String[] args) {
		int[] arr= {3,2,4,2,4,2,4};
		System.out.print(majorityElement(arr));
		System.out.print(findingMajority(arr));
	}
	
	/*	Approach - 1
	 * Using HashMap or Dictionary 
	 * make the array as key:value pair where keys are distinct elements and values are frequency
	 * iterate over the keys and check values > floor(n/3 if true add them to list
	 * if list has 2 elements, check for sorting and return
	 * Time Complexity O(n)
	 * Space Complexity O(n) ==> for HashMap in worst case
	 * */
	static ArrayList<Integer> majorityElement(int[] arr) {
		HashMap<Integer,Integer> dict=new HashMap<>();
		ArrayList<Integer> res=new ArrayList<>();
 		for(int i=0;i<arr.length;i++) {
			if(dict.containsKey(arr[i])) {
				dict.put(arr[i],dict.get(arr[i])+1);
			}
			else {
				dict.put(arr[i], 1);
			}
		}
		for(int key:dict.keySet()) {
			if(dict.get(key)>Math.floor(arr.length/3)) {
				res.add(key);
			}
		}
		if (res.size()==2 && res.get(1)<res.get(0)) {
			int temp=res.get(0);
			res.set(0,res.get(1));
			res.set(1,temp);
		}
		return res;
	}
	
	
	/*	Approach - 2
	 * Boyer Moore's Voting Algorithm
	 * take 2 elements as candidates and 2 counters
	 * follow conditions and find 2 candidates/elements which might have majority
	 * check >n//3 condition, if true add to ArrayList to return
	 * if list has 2 elements, check for swapping and return
	 * Time Complexity is O(n)
	 * Space complexity is O(1)
	 * */
	static ArrayList<Integer> findingMajority(int[] arr){
		int element1=-1,element2=-1;
		int count1=0,count2=0;
		for(int element:arr) {
			if(element1==element) {
				count1++;
			}
			else if(element2==element) {
				count2++;
			}
			else if(count1==0) {
				element1=element;
				count1++;
			}
			else if(count2==0) {
				element2=element;
				count2++;
			}
			else {
				count1--;
				count2--;
			}
		}
		ArrayList<Integer> res=new ArrayList<>();
		count1=0;
		count2=0;
		for(int element:arr) {
			if(element1==element) {
				count1++;
			}
			else if(element2==element) {
				count2++;
			}
		}
		if(count1>Math.floor(arr.length/3)) {
			res.add(element1);
		}
		if(count2>Math.floor(arr.length/3) && element1!=element2) {
			res.add(element2);
		}
		if(res.size()==2 && res.get(1)<res.get(0)) {
			int temp=res.get(0);
			res.set(0, res.get(1));
			res.set(1,temp);
		}
		return res;
	}
}
