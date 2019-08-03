#loops_task.py

#Anfal Hussain 

items_list= []
user_input = ""


while user_input != "done":
	user_input = input ("item (enter \"done\" when finished): ")

	if (user_input != "done"):
		inital_price = input ("price:")
		quantity = input ("quantity:")
		price = float(quantity) * float(inital_price)

		items_list.append({ "name": user_input,"price": str(price), "quantity": quantity})



print ("-------------------")

print("receipt")

print ("-------------------")


total = 0.0
for item in items_list:
		#[quantity, user_input, price ]
	print (item["quantity"],item["name"], str('{:0.3f}'.format( float(item["price"]) ) ) + "KD" )	
	total = total +  float(item["price"])

print ("-------------------")

print("total: ", str('{:0.3f}'.format(total))  + "KD")

