"""Aditya Anand
CA
SoftDev
K06: Divine your Destiny (dictionary from csv file)
2024-09-19
time spent: """

import random
d = {}
nums = []


def createList():
   List = open("occupations.csv", "r") #opens text file with read permissions
   ind = List.read().split("\n") #splits into list of occupations and their percentages
   for ppl in ind: 
       info = ppl.split(",") #splits into occupation and percent
       d[info[0]] = info[1] #list created
   nums.append(d[0][1])
   for i in range(1, len(d)):
           nums.append(d[i][1] + nums[i-1])
   print (nums)
       
def randomDevo():
   choice = random.randint(0, 1000) #random number in range 0 to length
   for i in range(0, len(d)):
       o = d[0][1] * 10 #choose random occupation
       last = o
createList()