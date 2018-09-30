# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:17:20 2018

@author: aditya
"""


'''
Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

'''

people = [3,5,3,4]
limit =5

people = [1,2]
limit =8

people = [3,2,2,1]
limit = 3
print("#####")
people = [3,8,7,1,4]
limit = 9

cache = []
counter =0 
i=0
for i in range(0,len(people)):
    diff=limit
    
    if i in cache:
        continue
    j=i
    while(diff > 0 and j <len(people)):
        print("j = %d , Counter = %d, Diff = %d"%(j,counter,diff))
        print(cache)
     
        if j not in cache:
            check = True
            diff = diff - people[j]
            if diff < 0 :
                diff = diff + people[j]
                check = False
            if check :
                cache.append(j)
        j=j+1
    print("Came out of while loop")
    print("cache : ",cache)
    counter = counter +1
    
people = [3,5,3,4] 
people = [3,2,2,1]
limit = 3


people= sorted(people) 
light=0
heavy= len(people)-1  
  del i,j 
limit = 5
counter =0
while(light<=heavy):
    counter = counter +1
    if (people[light]+people[heavy])<=limit:
        light = light +1
    heavy = heavy - 1
    