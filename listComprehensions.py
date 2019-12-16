#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:36:11 2019

@author: scottmarsden
"""

import re 

def main():
    
    #part 1
   firstSentence = ['I', 'am', 'playing', 'xbox', 'and', 'trying', 'hard']
   secondSentence = ['I', 'am', 'trying', 'hard', 'for', 'a', 'win']
   
   #1
   print([x for x in firstSentence if len(x) > 2 ] + [x for x in secondSentence if len(x) > 2 ])
   print([x[:-3] for x in firstSentence])
   #2
   print( [x for x in firstSentence if x[:1] == "a"])
   #3
   print( [x[-2:] for x in firstSentence ])
   #4
   print([x for x in firstSentence if len(x) % 2 == 0] + [x for x in secondSentence if len(x) % 2 == 0])
   #5 
   print([firstSentence.index(x) for x in firstSentence if len(x) % 2 == 0])
   #6 
   print([x for x in firstSentence if len(x) >= 6] + [x for x in secondSentence if len(x) >= 6] )
   #7 
   print([x for x in firstSentence for y in secondSentence if x == y and len(x) < 3])
   #8 
   print([x for x in firstSentence for y in secondSentence if x == y])
   #9
   print([x.capitalize() for x in firstSentence])
   #10 
   print([x.replace("a", "ee") for x in firstSentence])
   #11
   print([(x,y) for x in firstSentence for y in secondSentence if firstSentence.index(x) == secondSentence.index(y) and x != y])
   #12 
   print([(x,y) for x in firstSentence for y in secondSentence if x == y])
   #13
   print( [(x+y) for x in firstSentence for y in firstSentence if x != y and len(x) < len(y)])
   #14
   print([firstSentence.index(x) for x in firstSentence for y in secondSentence if x == y])
   #15
   print( [(x[:1] ,y[:1] ) for x in firstSentence for y in secondSentence])
   
   
   #Part 2
   
       
   #Read in file of words 
   file = open("/Users/scottmarsden/Desktop/Lowerwords.txt" ,"r")
   wordList = []
   for line in file:
       line = line.strip()
       wordList.append(line)
       
   #1
   print("Question 1: " + str(len(filterList(r'^.*a$', wordList))))
   #2
   print("Question 2: " + str(len(filterList(r'^\w{4}d$', wordList))))
           
   #3
   print("Question 3: " + str(len(filterList(r'^.*[aeiou]$', wordList))))
   #4
   print("Question 4: " + str(len(filterList(r'^[aeiou].*[aeiou]$', wordList))))
   #5 
   print("Question 5: " + str(len(filterList(r'^([aeiou])\w*\1$', wordList)))) 

   #6 
   print("Question 6: " + str(len(filterList(r'^.*[aeiou]{4}$', wordList))))
   
   #7
   print("Question 7: " + str(len(filterList(r'^.*in.*in.*in.*$', wordList))))
   #8 
   print("Question 8: " + str(len(filterList(r'.*(..).*\1.*\1.*$', wordList))))
   #9 
   print("Question 9: " + str(len(filterList(r'^.*(.)(.).*\2\1.*\1\2.*$', wordList))))
   #10 
   print("Question 10: " + str(len(filterList(r'^.*(.)\1.*(.)\2.*(.)\3.*$', wordList))))
   #11
   print("Question 11: " + str(len(filterList(r'^.*((.).\2).*\1.*$', wordList))))
   #12
   print("Question 12: " + str(len(filterList(r'^.*(.).\1(.).\2(.).\3.*$', wordList))))


#filter list function
def filterList(regex, myList):
   return [x for x in myList if re.search(regex,x)]

main()