auction_user={}
while( True ):
   name=input("Enter your Name")
   amount=input("Enter the amount")
   auction_user[name] = amount
   new_user=input("Do you want to add new user")

   if ( new_user == "Y" ) or ( new_user == "Yes" ) or (new_user == "y" ):
       continue
   else:
       break

print (auction_user)
max_value = max(auction_user.values())

print (max_value)


for name , value in auction_user.items():
    if value == max_value:
        print(f"Player {name} has won the auction ")

