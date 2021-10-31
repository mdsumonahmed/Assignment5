
def multiplicationTable(num):
	print("Multiplication table for ",num)
	for i in range(1,11):
		print(num,"*",i,"=",num*i)

user_input = int(input("Enter an number "))
for i in range(1,user_input+1):
	multiplicationTable(i)
	