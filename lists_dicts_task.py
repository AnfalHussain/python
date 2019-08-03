
#Recruitment System

#Anfal Hussain




print("Welcome to the special recruitment program, please answer the following questions:")


cv = {} # empty list

cv["name"] = input("name: ")

cv["age"] = input("age: ")

cv["experience"] = input("how many years of experience do you have? ")

#key skills to the cv dictionary and give it an empty list as a value
cv["skills"] = [] 

skills = ["Python", "Java", "Swift", "UX", "UI", "CSS" ]

print("skills:")

#Printing skills
index = 1 
for skill in skills:
	print ( str(index) + "-",skill )
	index+=1

skill1 = input("choose a skill from above: ")
skill2 = input("choose another skill from above: ")


skill1Name = skills[ int(skill1) -1]
skill2Name = skills[ int(skill2) -1]

cv["skills"] = [skill1Name,skill2Name]

print (cv)

hasSwiftSkill = False
#checking skills:
for item in cv["skills"]:
	if(item == "Swift"):
		hasSwiftSkill = True




if int(cv["age"]) >= 21 and int(cv["experience"]) >=1  and hasSwiftSkill == True :
		print ("you have been accepted,", cv["name"])

else:
	print ("you have been rejected,", cv["name"])	

