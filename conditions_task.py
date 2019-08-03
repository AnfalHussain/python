# conditions_task.py

# Anfal Hussain


FirstNum = input("Enter the first number: ")

SecondNum = input("Enter the second number: ")


ChooseOperation = input("Choose the operation (+, -, /, *):")



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





