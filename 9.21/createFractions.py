# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:25:01 2022

@author: Anish
"""

"""Driver class to create fractions from class Fraction""" 
#import the fraction class 
import fraction 
#import numpy to permit generating random integer values
import numpy as np 
#import utilitiesModule to permit getting lists of integer values 
import utilitiesModule as um

#empty list to store list of fraction objects 
f = []
#set how many fraction objects will be instantieated 
NUM_FRACTIONS = 10
#set the min val for numerator values; keep fractions pos to simplify formatting mixed fr.
NUM_MIN_VAL = 2
#set min value for denominator values; permit zero to verify that 
#ZeroDivisionErroris raised correctly
DEN_MIN_VAL = 0
#set max plus one of numerator values 
NUM_MAX_VAL = 21 
#set max plus one of denominator values 
DEN_MAX_VAL = 41

#populate the list of numerator values by calling getRandom Ints in utilitiesModule 

print('List of numerators: ')
nums= um.getRandomInts(NUM_MIN_VAL, NUM_MAX_VAL, NUM_FRACTIONS)
#populate list of_denominator values 
print (nums)  
dens = um.getRandomInts(NUM_MIN_VAL, NUM_MAX_VAL, NUM_FRACTIONS)
print('List of denominators: ')


print('\nFractions generated: \n') 
#instantiate fraction objects by pairing up the nums and dens vals 
for i in range(len(nums)): 
    try:
        fr = fraction. Fraction(nums[i], dens[i])
    #if denominator is zero, catch the ZeroDivisionError that is raised 
    except ZeroDivisionError:
        #replace the zero with 1 
        fr = fraction.Fraction(nums[i], 1)
        #inform user that zero denominator was changed to 1
        print('Zero denominator changed to i, at index', i) 
    #append this fraction object to the list 
    f.append(fr)
print() #add line of white space in console 
#display all fractions, as both n / d and as its equivalent float representation 
for i in range(len(f)): 
    print('i:', i, '; f[', i,']: ', f[i], ', equivalent to', f[i].getFloat())

indexF1 = np.random.randint(0, NUM_FRACTIONS)
indexF2 = np.random.randint(0, NUM_FRACTIONS)
    
#Randomly choose the two fractions for the operations, by randomly generating integer values 
#that represent the index values of an element in the list of fraction objects 
print('\nRandomly select two of the Fraction objects on which to perform the multiply operation: ')
### write the code to randomly get indexF1 in correct range 
print('\nf1: The fraction at index', indexF1, 'is', f[indexF1])
#### write the code to randomly get indexF2 in correct range 
print('\nf2: The fraction at index', indexF2, 'is', f[indexF2], '\n')
#perform multiplication on the two fractions 
f3 = f[indexF1].multiply(f[indexF2]) 
print(f[indexF1], 'times', f[indexF2], '==', f3, ', equivalent to', f3.getFloat())