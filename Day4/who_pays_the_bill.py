friends = ["alice" , "bob" , "charlis" , "david" , "emanuel" ]
import random
len_friends = len(friends)
print (len_friends)
random_payer = random.randint(0 , 4 )
print (random_payer)
print ( friends[random_payer] + " is the payer of the bill" )
