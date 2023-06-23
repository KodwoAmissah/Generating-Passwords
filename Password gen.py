alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol=["'","@","$","!","£","&"]
name=input("Enter your name:")
count_number=int(input("how many numbers in your password"))
count_letter=int(input("how many letters in your password:"))
count_symbol=int(input("how many symbols in your password:"))

import random


# random.randint
pass_letter=[] 
pass_symbol=[]
pass_number=[]

for var in range (count_letter):
    ran_letter=random.randint(0,len(alphabets))
    pass_letter.append(alphabets[ran_letter])
   # print(pass_letter)


   
for var in range (count_symbol):
    ran_symbol=random.randint(0,len(symbol)-1)
    pass_symbol.append(symbol[ran_symbol])
   # print(pass_symbol)


   
for var in range (count_number):
    ran_number=random.randint(0,10)
    pass_number.append (str(ran_number))
    #print(pass_number)

    pass_list=pass_number+pass_letter+pass_symbol
   # print(pass_list)

    random.shuffle(pass_list)
    #print(pass_list)
   
    password="".join(pass_list)
    print(password)