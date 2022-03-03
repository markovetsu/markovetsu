#Add the text of the program for calculating the Euclidean distance (hypotenuse) by displacements a and b (formula:).
#Round the result to the nearest hundredths. Display the resulting value on the screen.

# data entry
a, b = map(int, input().split())

# continue the program here
from math import sqrt
print(round(pow(a**2 + b**2, 0.5),2))
