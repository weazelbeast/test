import sys

from termcolor import colored

print (colored("Type a number", "green"))
num = int(input())

if num < 20 :
    print(colored("fizz", "red"))

elif num > 20 and num < 29 :
    print(colored("buzz" , "green"))

elif num > 30 : 
    print(colored("wuzzy" , "blue"))


