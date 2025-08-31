def pattern1(n):  				 		#  * * * * *
    for i in range(n):           		#  * * * * *
        for j in range(n):       		#  * * * * *
            print("* ", end="")  		#  * * * * *
        print()                 		#  * * * * *

def pattern2(n):  						#  *
    for i in range(1, n+1):       		#  * *
        for j in range(1, i+1):   		#  * * *
            print("* ", end="")   		#  * * * *
        print()                   		#  * * * * *

def pattern3(n): 				  		#  * * * * *
    for i in range(1, n+1):      	 	#  * * * *
        for j in range(n, i-1, -1):   	#  * * *
            print("* ", end="")   		#  * *
        print()                   		#  *

def pattern4(n):  						#  *
    for i in range(1, n+1):         	#  * *
        for j in range(1, i+1):    	 	#  * * *
            print("* ", end="")     	#  * * * *
        print()                     	#  * * * * *
    for i in range(1, n+1):         	#  * * * *
        for j in range(n-1, i-1, -1):   #  * * *
            print("* ", end="")     	#  * *
        print()							#  *

def pattern5(n):  						#  1
    for i in range(1, n+1):         	#  1 2
        for j in range(1, i+1):     	#  1 2 3
            print(j, end=" ")      		#  1 2 3 4
        print()                     	#  1 2 3 4 5

def pattern6(n):  						#      *
    for i in range(1, n+1):         	#     **
        for j in range(n-1, i-1, -1):   #    ***
            print(" ", end="")      	#   ****
        for j in range(i):          	#  *****
            print("*", end="")
        print()

def pattern7(n):  						#  *****
    for i in range(n):             		#   ****
        for j in range(i):          	#    ***
            print(" ", end="")      	#     **
        for j in range(n, i, -1):   	#      *
            print("*", end="")
        print()

def pattern8(n):
    for i in range(1, n+1):         	#      *
        for j in range(n-1, i-1, -1):   #     * *
            print(" ", end="")      	#    * * *
        for j in range(i):          	#   * * * *
            print("* ", end="")     	#  * * * * *
        print()

def pattern9(n):  						#  * * * * *
    for i in range(n):             	 	#   * * * *
        for j in range(i):          	#    * * *
            print(" ", end="")      	#     * *
        for j in range(n, i, -1):   	#      *
            print("* ", end="")
        print()

def pattern10(n):
    for i in range(n):
        for j in range(n-1, i, -1):     #      *
            print(" ", end="")          #     ***
        for j in range(i+1):            #    *****
            print("*", end="")          #   *******
        for j in range(i):              #  *********
            print("*", end="")
        print()

def pattern11(n): 		 				#  *********
    for i in range(n):              	#   *******
        for j in range(i):          	#    *****
            print(" ", end="")      	#     ***
        for j in range(n, i, -1):   	#      *
            print("*", end="")
        for j in range(n-1, i, -1):
            print("*", end="")
        print()

def pattern12(n): 	 					#  * * * * *
    for i in range(n):              	#   * * * *
        for j in range(i):          	#    * * *
            print(" ", end="")      	#     * *
        for j in range(n, i, -1):   	#      *
            print("* ", end="")			#      *
        print()							#     * *
    for i in range(n):					#    * * *
        for j in range(n-1, i, -1):		#   * * * *
            print(" ", end="")			#  * * * * *
        for j in range(i+1):
            print("* ", end="")
        print()

def pattern13(n):  						#  * * * * *
    for i in range(n):              	#   * * * *
        for j in range(i):          	#    * * *
            print(" ", end="")      	#     * *
        for j in range(n, i, -1):   	#      *
            print("* ", end="")			#     * *
        print()							#    * * *
    for i in range(1, n):				#   * * * *
        for j in range(n-1, i, -1):		#  * * * * *
            print(" ", end="")
        for j in range(i+1):
            print("* ", end="")
        print()

def pattern14(n):  								#      *
    for i in range(1, n+1):         			#     **
        for j in range(n, i, -1):   			#    * *
            print(" ", end="")     	 			#   *  *
        for j in range(1, i+1):					#  *****
            if j == 1 or j == i or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def pattern15(n):  						#      *
    for i in range(1, n+1):         	#     * *
        for j in range(n-i):        	#    *   *
            print(" ", end="")      	#   *     *
        if i == 1:						#  *********
            print("*")
        elif i < n:
            print("*", end="")
            for j in range(2*i-3):
                print(" ", end="")
            print("*")
        else:
            for j in range(2*n - 1):
                print("*", end="")
            print()

# Usage example
if __name__ == "__main__":
    # n = int(input("enter a number:  "))
    n=5
    # pattern1(n)
    # pattern2(n)
    # pattern3(n)
    # pattern4(n)
    # pattern5(n)
    # pattern6(n)
    # pattern7(n)
    # pattern8(n)
    # pattern9(n)
    # pattern10(n)
    # pattern11(n)
    # pattern12(n)
    # pattern13(n)
    # pattern14(n)
    pattern15(n)
