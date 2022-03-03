


# (1 Task) Add the text of the program for calculating the Euclidean distance (hypotenuse) by displacements a and b (formula:).
#Round the result to the nearest hundredths. Display the resulting value on the screen.

# data entry
a, b = map(int, input().split())

# continue the program here
from math import sqrt
print(round(pow(a**2 + b**2, 0.5),2))



# (2 Task) Add a program to find the number of combinations from n to k (values are entered in the program) 
#using the formula ., where . Print the result to the console as an integer using the print function.
#To calculate the factorials, use the corresponding function from the math library.

# data input
n, k = map(int, input().split())

# here continue the
import math
print((math.factorial(n)//(math.factorial(k)*(math.factorial(n-k)))))



# (3 Task) You need to take n children and m counselors to the summer camp with the help of buses. 
#The maximum capacity of each bus is 20 people. 
#Add a program to calculate the minimum number of buses needed to transport children together with counselors.
#Output the result to the console as an integer.

# data input
n, m = map(int, input().split())

# here continue the program
import math
print(math.ceil((n+m)/20))


# (4 Task) A gel pen costs x rubles. Today, the store provides a 10% discount on each purchased pen. 
#What is the largest number of such pens you can buy for 500 rubles?
#Output the result to the console as an integer.

# data input
x = int(input())

# here continue the program
import math
print(math.floor(500/(x/100*90)))



