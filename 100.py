# The goal of this exercise is to create a program that asks name + age and tells you the year you would turn 100
from datetime import date

name = input("What is your name? ")
age = int(input("How old are you " + name + "? "))

today = date.today()
cur_year = (today.year)

print ("So that means you will be 100 in the year " + str(100 - age + cur_year))