#Odd ID:
#Basically the logic of a strong number is, if the sum of the factorial of the each value from a number is also 
#equal to the orginal number,then we can call a number is a strong number.
#Example: 145 = 1! + 4! + 5! = 1 + (4x3x2x1) + (5x4x3x2x1) = 1 + 24 + 120 = 145


num = int(input(" Enter the Number:"))  
sum = 0  
temp = num  
  
while(temp > 0):  
    fact = 1  
    rem = temp % 10  
  
    for i in range(1, rem + 1):  
        fact = fact * i  

  
    print("Factorial of %d = %d" %(rem, fact))  
    sum = sum + fact  
    temp = temp // 10  
  
print("\n Sum of Factorials of a Given Number %d = %d" %(num, sum))  
      
if (sum == num):  
    print(" The given number is a Strong Number")  
else:  
    print(" The given number is not a Strong Number") 