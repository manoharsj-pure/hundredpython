import random

from sqlalchemy.dialects.mysql import match

word_list = ["aardwork" , "babooon" , "camel"]
# TODO Randomly Choose the word from word_list and assign it to word_chosen

word_chosen=word_list[random.randint(0,2)]

print(word_chosen)

placeholder_length =len(word_chosen)

## TODO create a placeholder string with all underscores same as the number of letter in string
placeholder=""
for num in range(placeholder_length):
    placeholder += "_"

print(placeholder)

placeholder_list=list(placeholder)
word_chosen_list=list(word_chosen)

print (placeholder_list)
print (word_chosen_list)

while placeholder_length > 0:
    print(f"attempts {placeholder_length}")
    print(placeholder_list)
    user_letter = input("Enter your letter").lower()
    for index, val in enumerate(word_chosen_list):
        if val == user_letter:
            print("Letter found in " + word_chosen)
            placeholder_list[index] = user_letter
            placeholder_length -= 1
        elif index == len(word_chosen_list) - 1:
            print("No match found")
            #placeholder_length -= 1
        elif not ("_" in placeholder_list):
            print("you Win")
            exit()
        elif placeholder_length < 0:
            print("All Lifes are used.")
            exit()
    placeholder_length -= 1
