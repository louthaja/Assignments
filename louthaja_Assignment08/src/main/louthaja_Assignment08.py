'''
Created on Jul 21, 2021

Name: Jacob Louthan
email: louthaja@mail.uc.edu
Assignment: Assignment 08
Course: IS 1040
Semester/Year: Summer 2021
Brief Description: This project demonstrates that I can use Eclipse to create an Eclipse PyDev project
Citations: https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html, numpy slides on canvas, https://www.w3resource.com/numpy/manipulation/ndarray-flatten.php, https://www.w3resource.com/python-exercises/numpy/python-numpy-string-exercise-3.php
Anything else that's relevant:
'''
from numpy.matlib import rand
from numpy.random.mtrand import randint

if __name__ == '__main__':
    
    import numpy as np
    # Problem #1: Here is a numPy array of Fahrenheit temperatures.
    #Convert them to Centigrade temperatures and print the result
    f = [-100, 0, 32, 100, 212]
    c = []
    Fahrenheit = np.array(f)
    for i in f:
       d = (i -32) * 5/9
       c.append(d)
    Centigrade = np.array(c)
    print(Centigrade)
       
    #print(Fahrenheit)
    
    # Problem #2: Given two arrays, find the common values between them.
    # function came from https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html 
    a1 = np.array([1,2,3,4,5,6,7,8,9,10])
    a2 = np.array([2,4,6,8,10,12,14,16,18,20])
    print(np.intersect1d(a1,a2))
    
    # Problem #3: Given an array, a1, create a new array, a2, with all the values divisible by 3 in a1
    #assumed you meant p3 so thats what i based my code on
    # almost entirely donor code from the numpy slides
    p3 = np.array([3,6,9,10,11,12,13,14,15,16,17,18])
    divis = p3 % 3 == 0
    a = p3[divis]
    print(a)   
    
    # Problem #4: Create a 2-dimensional (2-axis) array with 5 rows and 6 columns. Initialize the elements to random integer values between 1 and 100
    p4 = np.random.randint(0,101,30).reshape(5,6)
    p4.shape
    print(p4)
    
    # Problem #5: Given an array, a, compute the average of all the elements. Use a for loop and a flatten function.
    # learned what flatten was through https://www.w3resource.com/numpy/manipulation/ndarray-flatten.php
    a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
    x = 0
    c = 0
    for i in a:
        x = x + i
        c = c + 1
    avg = x / c
    avg = np.array(avg).flatten()
    print(avg)
    
    # Problem #6: Given an array of strings containing first/last names, convert them to title case.
    # title case context came from https://www.w3resource.com/python-exercises/numpy/python-numpy-string-exercise-3.php
    names = np.array(['calbert cheaney', 'lyndon jones', 'pat graham', 'chris reynolds', 'matt nover', 'greg graham', 'todd leary'], dtype=str)
    titlenames = np.char.title(names)
    print(titlenames)
       
       
   