package Patterns;
import java.util.Scanner;
public class Patterns {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		System.out.print("enter a number:  ");
		int n=sc.nextInt();
//		pattern1(n);
//		pattern2(n);
//		pattern3(n);
//		pattern4(n);
//		pattern5(n);
//		pattern6(n);
//		pattern7(n);
//		pattern8(n); 
//		pattern9(n);
//		pattern10(n);
//		pattern11(n);
//		pattern12(n);
//		pattern13(n);
//		pattern14(n);
		pattern15(n);
//		pattern16(n);
		sc.close();

	}
	static void pattern1(int n) {				//	* * * * *
		for(int i=0;i<n;i++) {					//	* * * * *
			for(int j=0;j<n;j++) {				//	* * * * *
				System.out.print("* ");			//	* * * * *
			}									//	* * * * *
			System.out.println();
		}
	}
	static void pattern2(int n) {				//	*
		for(int i=1;i<=n;i++) {					//	* *
			for(int j=1;j<=i;j++) {				//	* * *
				System.out.print("* ");			//	* * * *
			}									//	* * * * *
			System.out.println();
		}
	}
	static void pattern3(int n) {				//	* * * * *
		for(int i=1;i<=n;i++) {					//	* * * *
			for(int j=n;j>=i;j--) {				//	* * *
				System.out.print("* ");			//	* *
			}									//	*
			System.out.println();
			
		}
	}
	static void pattern4(int n) {				//	*
		for(int i=1;i<=n;i++) {					//	* *
			for(int j=1;j<=i;j++) {				//	* * *
				System.out.print("* ");			// 	* * * *
			}									//	* * * * *
			System.out.println();				//	* * * *
		}										//	* * *
		for(int i=1;i<=n;i++) {					//	* *
			for(int j=n-1;j>=i;j--) {			//	*
				System.out.print("* ");
			}
			System.out.println();
		}
	}
	
	static void pattern5(int n) {				//	1
		for(int i=1;i<=n;i++) {					//	1 2
			for(int j=1;j<=i;j++) {				//	1 2 3
				System.out.print(j+" ");		//	1 2 3 4
			}									// 	1 2 3 4 5
			System.out.println();
		}
	}
	
	static void pattern6(int n) {				//	    *
		for(int i=1;i<=n;i++) {					//	   **
			for(int j=n-1;j>=i;j--) {			//	  ***
				System.out.print(" ");			//	 ****
			}									//	*****
			for(int j=1;j<=i;j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
	
	static void pattern7(int n) {				//	*****
		for(int i=0;i<n;i++) {					//	 ****
			for(int j=0;j<i;j++) {				//	  ***
				System.out.print(" ");			//	   **
			}									//	    *
			for(int j=n;j>i;j--) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
	
	
	static void pattern8(int n) {
		for(int i=1;i<=n;i++) {					//	    *
			for(int j=n-1;j>=i;j--) {			//	   * *
				System.out.print(" ");			//	  * * *
			}									//	 * * * *
			for(int j=1;j<=i;j++) {				//	* * * * *
				System.out.print("* ");
			}
			System.out.println();
		}
	}
	
	static void pattern9(int n) {				//	* * * * * 
		for(int i=0;i<n;i++) {					//	 * * * * 
			for(int j=0;j<i;j++) {				//	  * * * 
				System.out.print(" ");			//	   * *
			}									//	    *
			for(int j=n;j>i;j--) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}
	
	static void pattern10(int n) {
		for(int i=0;i<n;i++) {
			for(int j=n-1;j>i;j--) {			//	    *
				System.out.print(" ");			//	   ***
			}									//	  *****
			for(int j=0;j<=i;j++) {				//	 *******
				System.out.print("*");			//	*********
			}
			for(int j=0;j<i;j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
	
	static void pattern11(int n) {				//	*********
		for(int i=0;i<n;i++) {					//	 *******
			for(int j=0;j<i;j++) {				//	  *****
				System.out.print(" ");			//	   ***
			}									//	    *
			for(int j=n;j>i;j--) {	
				System.out.print("*");
			}
			for(int j=n-1;j>i;j--) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
	
	
	static void pattern12(int n) {				//	* * * * *
		for(int i=0;i<n;i++) {					//	 * * * *
			for(int j=0;j<i;j++) {				//	  * * *
				System.out.print(" ");			//	   * * 
			}									//		*
			for(int j=n;j>i;j--) {				//	    *	
				System.out.print("* ");			//	   * *
			}									//	  * * *
			System.out.println();				//	 * * * *
		}										//	* * * * *
		for(int i=0;i<n;i++) {
			for(int j=n-1;j>i;j--) {
				System.out.print(" ");
			}
			for(int j=0;j<=i;j++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}
	
	static void pattern13(int n) {				//	* * * * *
		for(int i=0;i<n;i++) {					//	 * * * *
			for(int j=0;j<i;j++) {				//	  * * *
				System.out.print(" ");			//	   * * 
			}									//		*
			for(int j=n;j>i;j--) {				//	   * *
				System.out.print("* ");			//	  * * *
			}									//	 * * * *
			System.out.println();				//	* * * * *
		}										
		for(int i=1;i<n;i++) {
			for(int j=n-1;j>i;j--) {
				System.out.print(" ");
			}
			for(int j=0;j<=i;j++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}
	
	static void pattern14(int n) {				//	    *
		for(int i=1;i<=n;i++) {					//	   **
			for(int j=n;j>i;j--) {				//	  * *
				System.out.print(" ");			//	 *  *
			}									//	*****     
			for(int j=1;j<=i;j++) {
				if(j==1||j==i||i==n) {
					System.out.print("*");
				}
				else {
					System.out.print(" ");
				}
			}
			
			System.out.println();
			
		}
	}
	
	
	static void pattern15(int n) {				//	    *
		for(int i=1;i<=n;i++) {					//	   * *
			for(int j=1;j<=n-i;j++) {			//	  *   *
				System.out.print(" ");			//	 *     *
			}									//	*********
			if(i==1) {
				System.out.println("*");
			}
			else if(i<n) {
				System.out.print("*");
				for(int j=1;j<=2*i-3;j++) {
					System.out.print(" ");
				}
				System.out.println("*");
			}
			else {
				for(int j=1;j<=2*n-1;j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			
			
		}
	}
	
	
}
