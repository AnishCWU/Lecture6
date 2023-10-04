# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:45:45 2022

@author: Anish
"""

import numpy as np 
import time 
#import matplotlib.pyplot to enable plotting histogram 
import matplotlib.pyplot as plt

#setting up global variable for number of recursive calls
numRecCalls = 0 

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
    itGcdList = [] 
    numIterations = []

    
    #get start time 
    startTime = time. time() 
    #iterate through the lists and determine gcd of each pair 
    for i in range(len(listA)):
        curGcd, numIt = gcdIterative(listA[i], listB[i]) 
        #append this gcd to gcdList 
        itGcdList.append(curGcd) 
        #append this numIterations to the numIterations list 
        numIterations.append(numIt)
        endTime = time.time() 
        itExeTime = endTime - startTime 
        #return exe time, gcdList and numIterations list 
    return itExeTime, itGcdList, numIterations

def gcdRecursive(a, b): 
    """Assumes a and b are positive integers 
       Implements recursion to determine gcd 
       Returns the gcd
    """
    global numRecCalls 
    numRecCalls += 1
    
    if b==0:
        return a
    else:
        return gcdRecursive(b, a%b)
    
    
    
def getGcdRecursiveList(listA, listB):
    """Assumes listA and listB are equivalently sized python lists of ints 
        Calls the recursive function to determine gcd of each
       Returns the following:
           execution time required 
           list of gcd values 
           list of num recursive calls required 
    """
    global numRecCalls
    #initialize list of gcd vals 
    recGcdList = [] 
    numRecursive = []

    
    #get start time 
    startTime = time. time() 
    #recurve through the lists and determine gcd of each pair 
    for i in range(len(listA)):
        numRecCalls = 0
        curGcd = gcdRecursive(listA[i], listB[i]) 
        #append this gcd to gcdList 
        recGcdList.append(curGcd) 
        #append this numIterations to the numIterations list 
        numRecursive.append(numRecCalls)
    endTime = time.time() 
    itExecTime = endTime - startTime 
    #return exec time, recGcdList and numRecursive list 
    return itExecTime, recGcdList, numRecursive
    
    
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
itExeTime , itGcdList , itNumIt = getGcdIterativeList(listA,listB)  

itExecTime, recGcdList, numRecCalls = getGcdRecursiveList(listA, listB)

#print number of random integers pairs
print('The number of random integer pairs:', "{:,}".format(NUM_INTS))
print('\n')

#call the displayListSubset() function to display first ten elements of listA
print('First', NUM_DISPLAY, 'elements of listA:') 
displayListSubset(listA,NUM_DISPLAY)
print('\n')

#call the displaylistsubset() function to display first ten elements of listB 
print('First', NUM_DISPLAY, 'elements of listB:') 
displayListSubset(listB,NUM_DISPLAY)
print('\n')

#call the displayListSubset() function to display first ten elements of the godlist 
print('First', NUM_DISPLAY, 'elements of the itGcdList:') 
displayListSubset(itGcdList,NUM_DISPLAY)
print('\n')

print('First', NUM_DISPLAY, 'elements of the recGcdList:') 
displayListSubset(recGcdList,NUM_DISPLAY)
print('\n')

#call the displayListSubset() function to display first ten elements of itNumIt list 
print('First', NUM_DISPLAY, 'elements of itNumit:') 
displayListSubset(itNumIt,NUM_DISPLAY)
print('\n')

print('First', NUM_DISPLAY, 'elements of numRecCalls:') 
displayListSubset(numRecCalls,NUM_DISPLAY)
print('\n')

#use f' string formattng tool to display itExeTime 
print('Iterative function execution time: ', f'{itExeTime: .4f}')
print('\n')
print('Recursive function execution time: ', f'{itExecTime: .4f}')
print('\n')

if itExeTime < itExecTime:
    print("Iterative function requires less execution time")
else:
    print("Recursive function requires less execution time")

plt.figure()
bins = 10
nr = 10
plt.hist(numRecCalls, nr , facecolor = "blue", label = 'recursive')
plt.hist(itNumIt,bins,facecolor = 'green' ,label =' iterative')

plt.legend(loc = 'best')
plt.title("Ietrative vs Recursive gcd for 500,000 ints")
plt.xlabel("Number of iterations/ functions calls required")
plt.ylabel("Num of occurences of each iteration value/function call value")
plt.show()



    
    
    






