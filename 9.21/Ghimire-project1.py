"""
Created on Tue Apr 12 01:35:39 2022

@author: Anish Ghimire
"""

START_VAL = 3
STOP_VAL = 5001 
STEP_VAL = 2
sum = 0
count = 0
#Declaring the range 
for num in range(START_VAL, STOP_VAL, STEP_VAL):

    i = 1
    #checking if it us a prime number
    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
           #To get out of the loop 
            break;

    #If the number is prime then add it.
    else:
        #counting the integres and adding them up 
        count +=1
        sum += num
#Printing for final output      
print("\nRange of integers being tested:", [START_VAL, STOP_VAL])
print("\nNumbers of prime integers in this range:",count)
print('\nSum of the', count, 'prime integers in this range:', f'{sum:,.0f}')



