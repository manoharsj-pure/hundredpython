from soupsieve.util import lower

print("Pizza Bill calculator")
# Small = $15 , Medium = $20 , Large=$25
# Chutney=+3 for small , for Medium or large +3 and large
# extra cheese $1
size=(lower(input("Please enter the size of Pizza you want to buy ( S , M , L )")))
extra_topping=(lower(input("Please Say Y or N if you need extra toppings ( Y or N )")))
extra_cheese=(lower(input("Please say Y or N if you need extra Cheese ( Y or N)")))
price=0

if ( size == "s"):
  price=15
  if (extra_topping == "y"):
      price +=2
  if (extra_cheese == "y"):
      price += 1
elif (size == "m"):
  price=20
  if (extra_topping == "y"):
      price +=3
  if (extra_cheese == "y"):
      price += 1
elif (size == "l"):
  price=25
  if (extra_topping == "y"):
      price +=3
  if (extra_cheese == "y"):
      price += 1



print(f" Total bill for your Pizza is { price }")








