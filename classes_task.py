#classes_task.py

# HR Pro 2019 System Developed by Anfal Hussain

import datetime 
import sys

class Employee(object):

	def __init__(self, name, age, salary, employment_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date

	def get_working_years(self):
		today = datetime.date.today().year
		return str( int(today) - int(self.employment_date))



#class Manager is a subclass of class Employee
class Manager(Employee):
	def __init__(self, name, age, salary, employment_date, bonus_percentage):

		Employee.__init__(self, name, age, salary, employment_date)
		self.bonus_percentage = bonus_percentage
		

	def get_bonus(self):
		return str( '{:0.6f}'.format((self.bonus_percentage * float(self.salary) ) ) )


employees_list = []
managers_list = []




choice = ""

while (choice != "5"):

	print (" Welcome to HR Pro 2019")
	print ("    Choose an action to do:")
	print ("        1. show employees")
	print ("        2. show managers")
	print ("        3. add an employee")
	print ("        4. add a manager")
	print ("        5. exit")
	print()

	choice = input ("what would you like to do? ") 


	if choice == "1":

		print ("-----------------")

		for employee in employees_list:
			print("name:" ,employee.name, ",age:",employee.age ,",salary:", employee.salary, ", working years:", employee.get_working_years() )




	elif choice == "2":

		print ("-----------------")

		for employee in managers_list:
			print("name:" ,employee.name, ",age:",employee.age ,",salary:", employee.salary, ", working years:", employee.get_working_years(), "bonus:", employee.get_bonus() )




	elif choice == "3":

		print ("-----------------")

		name = input("name: ")
		age = input("age: ")
		salary = input("salary: ")
		employment_date = input("employement year: ")

		new_employee = Employee(name, age, salary, int(employment_date))

		employees_list.append(new_employee)
		print ("Employee added succesfully")

	elif choice == "4": 

		print ("-----------------")

		name = input("name: ")
		age = input("age: ")
		salary = input("salary: ")
		employment_date = input("employement year: ")
		bonus_percentage = input("bonus percentage: ")

		new_manager = Manager(name, age, salary, int(employment_date), float(bonus_percentage) )

		managers_list.append(new_manager)
		print ("Employee added succesfully")

	elif choice == "5":
		sys.exit()

