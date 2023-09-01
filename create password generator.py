import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
print("welcome to my password Generator")
n_letters=int(input("how many letters :"))
n_numbers=int(input("enter the numbers:"))
n_symbols=int(input("enter no of symbols:"))

# password =""                                             #easy
# for char in range(1,n_letters +1):
#     password+= random.choice(letters)
# for char in range(1,n_numbers +1):
#     password+= random.choice(numbers)
# for char in range(1,n_symbols +1):
#     password+= random.choice(symbols)
# print(password)

password_list =[]                                           #hard
for char in range(1,n_letters +1):
    password_list+= random.choice(letters)
for char in range(1,n_numbers +1):
    password_list+= random.choice(numbers)
for char in range(1,n_symbols +1):
    password_list+= random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+= char
print(f"your password is:{password}")

 