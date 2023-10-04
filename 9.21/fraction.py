# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:09:39 2022

@author: Anish
"""

class Fraction(object):
    """
        A fraction object is defined by its numerator and denominator
        If the denominator is zero, it raises a ZeroDivisionError
    """   
    def __init__(self, n, d):
        """
            Create a fraction object which has two instance variables: 
                n for the numerator 
                d for the denominator 
                if d == 0, raise ZeroDivisionError
        """ 
        self.n = n 
        if d != 0: 
            self.d = d 
        else: 
            raise ZeroDivisionError( 'Denominator cannot be zero')
            
    def getFloat(self, numDecPlaces = 4): 
        """Returns float representation of this fraction, rounded to 
            numDecPlaces; if no value for numDecPlaces is passed, uses default of 4
        """ 
        return round((self.n / self.d), numDecPlaces)

    def multiply(self, f2):
        """Method to return self fraction object times parameter fraction object""" 
        #the n of the product of the two fractions is the product of their
        #numerators
        n = self.n * f2.n 
        #the d of the product of the two fractions is the product of their 
        #denominators 
        d = self.d * f2.d 
        #instantiate fraction object, with numerator n and denominator d 
        f3 = Fraction(n, d) 
        #return the new fraction object 
        return f3

    def __str__(self): 
        """Method to display a fraction as n/d, 
           If d == 1 display as whole number 
           If n == d display as the integer one 
        """
        #format info to display
        #if d == 1 the fraction is a whole number
        if self.d == 1: 
             return str(self.n)  
        elif self.n == self.d: 
             #this fraction is the integer one
             return str(1) 
        else: 
            return str(self.n) + '/' + str(self.d)
        
        