# -*- coding: utf-8 -*-
"""python lab cylce 1 Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x0jSEFqC7JvBTjXtN1ualFiz5L1B0I-E
"""

#Develop a program to read the employee's name, code, and basic pay 

#and calculate the gross salary, deduction, and net salary according to

#the following conditions. Define a function to find each of the 

#components

# Finally, generate a payslip.

name = input("Enter name ")
code = int(input("Enter code"))
BS = int(input("Enter code"))

if(BS<10000 ):
  DA=(5/100)*BS
  HRA=(2.5/100)*BS
  MA=500
  PT=20
  PF=(8/100)*BS
  IT=0

elif(BS<30000 ):
   DA=(7.5/100)*BS
   HRA=(5/100)*BS
   MA=2500
   PT=60
   PF=(8/100)*BS
   IT=0
elif(BS<50000 ):
   DA=(25/100)*BS
   HRA=(11/100)*BS
   MA=5000
   PT=11
   PF=(11/100)*BS
   IT=11

else:
    DA=(25/100)*BS
    HRA=(11/100)*BS
    MA=7000
    PT=80
    PF=(12/100)*BS
    IT=20

def Gross_salary ():
  GS=BS+DA+HRA+MA

  return GS

def Deduction():
  D = PT+PF+IT
  
  return D

def Net_salary():
  GS = Gross_salary()
  D = Deduction()
  N = GS-D


  print("name", name)
  print("code", code)
  print("Basicpay", BS)
  print("Net salary", N)
  print("Gross salary", GS)

  return N

Net_salary()