from docutils.io import Input
import random
letters_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char_list=['@','#','$','%','^','&','*','(',')']
print ("=== Welcome to Password Generator ===")
total_numbers=int(input("Please enter the number of characters you want in Password"))
print(f"Total Number of letters are {total_numbers}")

total_alphabets=int(input("Please enter how many alphabets you want"))
total_numbers=int(input("Please enter how many numbers you want"))
total_chars=int(input("Please enter how many special characters you want"))
password_list= []
for letter in range(0 , total_alphabets):
    password_list.append(random.choice(letters_list))

for letter in range(0 , total_numbers):
    password_list.append(random.choice(numbers_list))

for letter in range(0 , total_chars):
    password_list.append(random.choice(special_char_list))


print(password_list)

random.shuffle(password_list)

print(password_list)

password=""
for char in password_list:
    password+= char

print(f"your generated password is {password}")




