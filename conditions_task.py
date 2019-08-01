# conditions_task.py

# Anfal Hussain


FirstNum = raw_input("Enter the first number: ")

SecondNum = raw_input("Enter the second number: ")


ChooseOperation = raw_input("Choose the operation (+, -, /, *):")



# Checking whether the numbers given are actually numbers and not any other string.
if (FirstNum.isalpha() == False and SecondNum.isalpha() == False ):

	#  check operation if valid 
	if (ChooseOperation == "+" or ChooseOperation == "-" or ChooseOperation == "*" or ChooseOperation == "/") :

		if (ChooseOperation == "+" ):
			answer = int (FirstNum)  + int (SecondNum)

		elif (ChooseOperation == "-" ):
			answer = int (FirstNum)  - int (SecondNum)

		elif (ChooseOperation == "*" ):
			answer = int (FirstNum)  * int (SecondNum)

		elif (ChooseOperation == "/" ):
			answer = int (FirstNum)  / int (SecondNum)

		print ("The answer is ", answer)	

	else:
		print ("the operation is not valid") 

	
else:
	print ("the numbers were invalid") 





