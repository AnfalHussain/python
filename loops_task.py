#loops_task.py

#Anfal Hussain 

item_number = 1
items_dictionary= {}
user_input = ""


while user_input != "done":
	user_input = input ("item (enter \"done\" when finished): ")

	if (user_input != "done"):
		inital_price = input ("price:")
		quantity = input ("quantity:")
		price = float(quantity) * float(inital_price)

		items_dictionary["item_number" + str(item_number) ] = [quantity, user_input, price ]
		item_number += item_number



print ("-------------------")

print("receipt")

print ("-------------------")


total = 0.0
for item in items_dictionary:
		#[quantity, user_input, price ]
		print (items_dictionary[item][0],items_dictionary[item][1] , str( '{:0.3f}'.format(items_dictionary[item][2]) ) + "KD")

		total = total +  float(items_dictionary[item][2])

print ("-------------------")

print("total: ", str('{:0.3f}'.format(total))  + "KD")

