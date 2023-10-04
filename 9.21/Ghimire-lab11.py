# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:45:45 2022

@author: Anish
"""

import numpy as np 
import time 
#import matplotlib.pyplot to enable plotting histogram 
import matplotlib.pyplot as plt

def getRandomInts(min, maxPlusOne, numInts):
    """Assumes the following:
        min is an int which specifies the smallest random int to generate 
        maxPlusOne is an int which specifies one more than largest random int to generate 
        numInts is an int that specifies how many random ints to generate 
        Returns the list of random ints
    """
    #start with empty list of random ints 
    randInts = []
    
    #use for loop to iterate to get required number of random ints 
    for i in range(numInts): 
        newInt = np.random.randint(min, maxPlusOne) 
        #append newInt to randInts list 
        randInts.append(newInt) 
    return randInts

def gcdIterative(a, b):
    """Assumbes a and b are ints 
       Implements loop to determine gcd of a and b
       Returns the gcd and numIterations required to determine this
    """
    #keep track of numIterations required
    numIterations = 0
    #initialize remainder to zero 
    remainder = 0
    #implement loop to compute gcd 
    while (b != 0):
        remainder = a % b 
        a = b 
        b = remainder 
        numIterations += 1
        #after exiting loop return a and numIterations 
    return a, numIterations

def displayListSubset(oneList, subsetSize): 
    """ Assumes onelist is a python list
        subsetSize is a positive int that specifies how many elements of the list to display 
    """
    #set up a list to contain the subset 
    listSubset = [] 
    for i in range(subsetSize + 1):
        listSubset.append((oneList[i])) 
    
    print(listSubset)

def getGcdIterativeList(listA, listB):
    """Assumes listA and listB are equivalently sized python lists of ints in 
       Implements iterative gcd method to determine gcd of each pair 
       Returns the following:
           execution time required 
           list of gcd values 
           list of num iterations required 
    """
    #initialize list of gcd vals 
    gcdList = [] 
    numIterations = []

    
    #get start time 
    startTime = time. time() 
    #iterate through the lists and determine gcd of each pair 
    for i in range(len(listA)):
        curGcd, numIt = gcdIterative(listA[i], listB[i]) 
        #append this gcd to gcdList 
        gcdList.append(curGcd) 
        #append this numIterations to the numIterations list 
        numIterations.append(numIt)
        endTime = time.time() 
        itExeTime = endTime - startTime 
        #return exe time, gcdList and numIterations list 
    return itExeTime, gcdList, numIterations
    
MIN = 2
MAX_PLUS_ONE = 51
NUM_INTS = 500000
NUM_DISPLAY = 10

#call the getRandom Ints() function to get listA 
listA = getRandomInts(MIN,MAX_PLUS_ONE,NUM_INTS)
#call the getRandom Ints( ) function to get listB
listB = getRandomInts(MIN,MAX_PLUS_ONE,NUM_INTS)

#call the getGcdIterativeList(listA, listB) to get the following:
    #itExtTime, godlist, itNumIt
itExeTime , gcdList , itNumIt = getGcdIterativeList(listA,listB)  


#call the displayListSubset() function to display first ten elements of listA
print('The first', NUM_DISPLAY, 'elements of listA:') 
displayListSubset(listA,NUM_DISPLAY)
#call the displaylistsubset() function to display first ten elements of listB 
print('The first', NUM_DISPLAY, 'elements of listB:') 
displayListSubset(listB,NUM_DISPLAY)
#call the displayListSubset() function to display first ten elements of the godlist 
print('The first', NUM_DISPLAY, 'elements of the gcdList:') 
displayListSubset(gcdList,NUM_DISPLAY)
#call the displayListSubset() function to display first ten elements of itNumIt list 
print('The first', NUM_DISPLAY, 'elements of itNumit:') 
displayListSubset(itNumIt,NUM_DISPLAY)
#use f' string formattng tool to display itExeTime 
print('Iterative method execution time: ', f'{itExeTime: .4f}')



plt.figure()
bins = 10
plt.hist(itNumIt,bins,facecolor = 'green' ,label =' iterative')
plt.legend(loc = 'best')
plt.title("Number of iterations for iterative gcd function")
plt.xlabel("Number of iterations required")
plt.ylabel("Num of occurences of each iteration value")
plt.show()



    
    
    






