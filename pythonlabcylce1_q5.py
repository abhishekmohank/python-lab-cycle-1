# -*- coding: utf-8 -*-
"""PythonLabcylce1_Q5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14k-Onollj1EHRXza3ay-NO2bAOJzI_mr
"""

#Develop a program to read a string and perform the following 

#operations:

#• Print all possible substrings.

#• Print all possible substrings of length K.

#• Print all possible substrings of length K with N distinct 

#characters.

#• Print substring(s) of length maximum length with N distinct 

#characters.

#• Print all palindrome substrings.

#Define function for each of the task.


st=str(input("enter any string: "))
def sub_str1():
  for i in range(0,len(st)+1):
    for j in range(i+1,len(st)+1):
      s=st[i:j]
      print(s)

def sub_str2():   
  k= int(input("enter the length type of substring: "))
  for i in range(0,len(st)+1):
    for j in range(i+1,len(st)+1):
      s=st[i:j]
      if(len(s)==k):
       print(s)

def sub_str3():   
  k= int(input("enter the length type of substring: "))
  n= int(input("enter the number of distinct characters: "))
  for i in range(0,len(st)+1):
    for j in range(i+1,len(st)+1):
      s=st[i:j]
    if(len(s)==k and len(set(s))==n):
       print(s)

def sub_str4(): 
  l=[]
  n= int(input("enter the number of distinct characters"))
  for i in range(0,len(st)+1):
    for j in range(i+1,len(st)+1):
      s=st[i:j]
      if(len(set(s))==n):
       l.append(s)
  print(l)
  m=len(max(l,key=len))
  for i in range(len(l)):
    if(len(l[i])==m):
      print(l[i])


def sub_str5():
  for i in range(0,len(st)+1):
    for j in range(i+1,len(st)+1):
      s=st[i:j]
      temp=s[::-1]
      if(s==temp):
        print(s)
  


        
sub_str1()
# sub_str2()
#sub_str3()
#sub_str4()
sub_str5()