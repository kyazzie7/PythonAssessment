#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# <h1>Assessment given by <i>Ritesh Lohiya</i></h1>
#         <h2>Assigment 2</h2>
#         <ol>
#             <li>Add / modify code ONLY between the marked areas (i.e. "Place code below")
#             </li>
#             <li>Run the associated test harness for a basic check on completeness. A successful run of the test cases does not
#                 guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
#             </li>
#             <li>To run unit tests simply use the below command after filling in all of the code:
#                 python 07_assignment.py
#             </li>
#             <li>Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
#             </li>
#             <li>Submissions must be a Python file and not a notebook file (i.e *.ipynb)
#             </li>
#             <li>Do not use global variables unless stated to do so
#             </li>
#             <li>Make sure your work is committed to your master branch in Github
#             </li>
#         </ol>
#     
# 

# 

# 

# In[3]:


#Install numpy:
#Already installed
pip install numpy


# In[4]:



import math
import unittest
import numpy as np
import requests as r


# In[49]:


#def exercise01():
# Create a list called animals containing the following animals: cat, dog, crouching tiger, hidden dragon, manta ray

# ------ Place code below here \/ \/ \/ ------
def exercise01() :
    animals = ['cat', 'dog', 'crouching tiger', 'hidden dragon', 'manta ray']
    return animals
# ------ Place code above here /\ /\ /\ ------


# In[61]:


#def exercise02():
# Repeat exercise 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set the variable len_animals to the length of the animal list.

# ------ Place code below here \/ \/ \/ ------
def exercise02() :
    #I'm using the same list I used in exercise one and making a new variable
    len_animals = animals
    for a in range(0,5):
        print(animals[a])
        #This will print list from left to right versus top to bottom in the print function
        return animals, len_animals
        
# ------ Place code above here /\ /\ /\ ------


# In[62]:


exercise02()


# In[80]:


#def exercise03():
    # Programmatically reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list.
    # The 5th element will be stored in the variable the_fifth_element, which currently below has a dummy value of -999.
    # Remember, the index number of the 5th element is not 5

    # ------ Place code below here \/ \/ \/ ------
def exercise03() :
    countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
    the_fifth_element = countdown[4]
    countdown.reverse()
    return countdown, the_fifth_element
    # ------ Place code above here /\ /\ /\ ------


# In[81]:


exercise03()


# In[90]:


#def exercise04(more_temperatures, iot_sensor_points, a, b, c, d, e):
    # This exercise function receives a list of temperatures and a dictionary of temperature data
    #..where the key is an arbitrary sequential number and the value is the temperature and a,b,c,d and e are each 
    #..a single temperature reading
    # To Do:
    # 1. Add all of the items in more_temperatures to the temperatures list
    # 2. Add all of the temperature values in iot_sensor_points to the temperatures list
    # 3. Add a,b,c,d and e to the temperature list
    # 4. Organize the temperatures in descending order
    # 5. The samples list will contain every 5th reading from the final temperatures list i.e in list [1,2,3,4,5,6,7,8,9,10] samples would be [5,10]
    # 6. Do a shallow copy of samples into copy_of_samples
    # 7. Organize samples in ascending order

    # ------ Place code below here \/ \/ \/ ------
def exercise04(more_temperatures, iot_sensor_points, a, b, c, d, e):
    #This represents the temp of the lowest temp of -25 to +25; The size is how many temps it outputs in the random set
    temperatures = list(np.random.randint(-25, 25, size=10))
    samples = []
    copy_of_samples = []
    more_temperatures = []
    iot_sensor_points = {}
    
    #1.
    for m in temperatures :
        temperatures.append(more_temperatures)
    #2.
    temperatures.append(iot_sensor_points)
    #3.
    temperatures.extend([a, b, c, d, e])
    #4.
    temperatures.reverse()
    #5.
    for s in range(0, len(temperatures), 5) :
        samples.append(temperatures[s])
    #6.
    copy_of_samples = samples
    #7.
    samples.sort()    
    
    return samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples
    # ------ Place code above here /\ /\ /\ ------


# In[96]:





# In[138]:


#def exercise05(n):
    # This function will find n factorial using recursion (calling itself) and return the solution. For example exercise05(5) will return 120. No Python functions are to be used.

    # ------ Place code below here \/ \/ \/ ------
def exercise05(n):
    if (n == 0 or n == 1) :
        return 1
    else:
        return n * exercise05(n-1)
    # ------ Place code above here /\ /\ /\ ------


# In[139]:





# In[149]:


def exercise06(n):
    # This function will receive an arbitrary list of numbers of arbitrary size and find the average of those numbers.
    #The size of the list may vary. Find the method that requires the  least amount of code. Return back the length,
    #...sum of list and average of list

    # ------ Place code below here \/ \/ \/ ------
    length_n=len(n)
    sum_n=sum(n)
    average_n=sum_n/length_n
    # ------ Place code above here /\ /\ /\ ------
    return length_n, sum_n, average_n


# In[150]:





# In[ ]:


def exercise07(n):
    # This function looks for duplicates in list n.
    #..If there is a duplicate False is returned. If there are no duplicates True is returned.

    # ------ Place code below here \/ \/ \/ ------
        list1=[1,2,3,4,6,3,5,6]
        if n in list1:
            print('true')
        else:
            print('false')
        

    # ------ Place code above here /\ /\ /\ ------


# In[ ]:


# Exercise 8
# Create a function called display_menu that receives an argument called menu. The function should do the following:
# 1. Verify that menu is in fact a tuple. If it isnt, return back -1. Remember that a function can return more than one value and -1 is just one of those values. Not all return values need to be meaningful in all cases.
# 2. Determine the number of elements in the menu tuple
# 3. Loops through menu & enumerate through the a menu to the screen. The test case will describe what the menu items are. The enumeration should be generate by code and not hardcoded.
# 4. Using input(), asks the user to select a menu item by entering a number and hitting Enter 
# 5. Validates if the number entered is a valid menu option and asks user to retry if number is not valid or is not a number / int
# 6. An EXIT menu option should be added at the end of the displayed list of menu options allowing the user to exit selecting a menu causing the display_menu() function to return back the number of the last menu option chosen prior to exit and also return the length of menu (the display_menu() function returns two values)
# 7. The menu options should repeatedly display after each selection until user selects EXIT

# ------ Place code below here \/ \/ \/ ------
menu=(1,3,4,5,6)
def display_menu(menu):
    #1. Checking if menu is a type tuple or not
    if type(menu) is tuple:
        print('This is a tuple.')
    else:
        return -1        
    options = input("Select a menu item by a number(1-6) and hit enter then done: ")
    if options in menu:
# ------ Place code above here /\ /\ /\ ------


# In[ ]:




