from os import system, name 

#win 
if name == 'nt': 
    _ = system('cls') 
  
#GNU Linux,Unix and etc.
else: 
    _ = system('clear')