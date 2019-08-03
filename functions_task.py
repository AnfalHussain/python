# functions_task.py
# Anfal Hussain

import datetime

NowDate = datetime.date.today()
ThisYear = NowDate.year
ThisMonth = NowDate.month
ThisDay = NowDate.day

def check_birthdate(year, month, day):

	if (year >  ThisYear):
		return False

	elif (year ==  ThisYear):

		if (month > ThisMonth): #check month and day
			return False

		elif (month == ThisMonth):

			if (day >= ThisDay):
				return False
			else:
				return True	#if day < ThisDay means past -> true	


		else:
			return True		#if month < Thismonth means past -> true	

	else:
			return True		#if year < ThisYear means past -> true	


# checking the function check_birthdate

# print ("2020/6/1" , check_birthdate(2020,6,1) )	
# print ("2019/6/1" , check_birthdate(2019,6,1) )	
# print ("2019/9/1" , check_birthdate(2019,9,1) )	
# print ("2019/8/1" , check_birthdate(2019,8,1) )	



def calculate_age(year, month, day):

	TodayDate = datetime.date.today()
	CurrentYear = TodayDate.year
	CurrentMonth = TodayDate.month
	CurrentDay = TodayDate.day

	if (day > CurrentDay ):
		CurrentMonth = CurrentMonth - 1 
		CurrentDay = CurrentDay + 30 

	if (month > CurrentMonth):	
		CurrentYear = CurrentYear -1 
		CurrentMonth = CurrentMonth + 12
	 
	years = CurrentYear - year 
	months = CurrentMonth - month
	days = CurrentDay - day
	print ("You are" ,years, "years," , months,  "months, and" , days, "days" )




UserYear = input("Enter year of birth: ")
UserMonth = input("Enter month of birth: ")
UserDay = input("Enter day of birth: ")

if ( check_birthdate( int(UserYear), int(UserMonth), int(UserDay) ) == True ): # if true 
	calculate_age( int(UserYear), int(UserMonth), int(UserDay))

else:
	print ("The birthdate is invalid")	





