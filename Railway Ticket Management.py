red_color = '\033[91m'
green_color = '\033[32m'
no_color = "\033[00m"
n = 10
AC_S = []
SNIGDHA = []
S_CHAIR = []
PASSENGER_SIT_NO=[]
class BANALATA_EXPRESS:
	
	def set_sit(self):  
		#For set sit
		for i in range(0, n):
			flag = 1
			AC_S.append(flag)
			SNIGDHA.append(flag)
			S_CHAIR.append(flag)

	
	def ac_s(self):	
		count = 0
		for i in range(0, n):
			print("    ",i,no_color+"",green_color+"",AC_S[0],no_color+"",end=" ")
			count +=1
			if count == 2:
				print("\n")
				count=0	

	def singdha(self):	
		count = 0
		for i in range(0, n):
			print("    ",i,no_color+"",green_color+"",SNIGDHA[0],no_color+"",end=" ")
			count +=1
			if count == 2:
				print("\n")
				count=0		

	def s_chair(self):	
		count = 0
		for i in range(0, n):
			print("    ",i,no_color+"",green_color+"",S_CHAIR[0],no_color+"",end=" ")
			count +=1
			if count == 2:
				print("\n")
				count=0							

def book_ticket(route):
	if route == "route1":
		objRaj = BANALATA_EXPRESS()
		print("CHOOSE A CLASS\n Enter 1 for : AC_S \n Enter 2 for : SNIGDHA\n Enter 3 for : S_CHAIR")
		user_sit_class = int(input())

		print("Only Green Color sit is available ")
		if user_sit_class == 1:
			objRaj.ac_s()
			print("Enter Passenger number : ")
			passenger_no = int(input("	"))
			count = 0

		  
		    
		    

		elif user_sit_class == 2:
		    objRaj.singdha()
		    print("Enter Passenger number : ")	
		    passenger_no = int(input("	"))
		    count = 0
		    for i in range(0, n):
		    	if SNIGDHA[i] == 1:
		    		count+=1	
		    if count>=passenger_no:
		    	print("Choose your sit no ")
		    	for i in range(0, passenger_no):
		    		sit_no = int(input())
		    		PASSENGER_SIT_NO.append(sit_no)
		    		SNIGDHA[sit_no]=0
		    	print("Thank's Your sit no is : ",PASSENGER_SIT_NO)
		    	
		elif user_sit_class == 3:
			objRaj.s_chair()
			print("Enter Passenger number : ")

		


											
if __name__ == '__main__':
	objRaj = BANALATA_EXPRESS()
	objRaj.set_sit()	
	print("Select your Route ")
	#user_input = input("Enter a string ")
	user_from = input("FROM : ")
	user_to = input("TO : ")

	if user_from == "Dhaka" or user_from == "DHAKA" and user_to == "Rajshahi" or user_to == "RAJ" :
		book_ticket("route1")
	else:
		print("Sorry Route is wrong")
			
	
	
'''
input

Dhaka
Rajshahi
2
2
3
4
'''
