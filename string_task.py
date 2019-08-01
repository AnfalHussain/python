# string_task.py
# Anfal Hussain


print ("Mad libs where libs get Mad")

print (" Start Below:")

print("\n")

time = raw_input("Number: ")

items = raw_input("Noun(plural): ")

name = raw_input("Name: ")

scream = raw_input("Any sentence: ")

action = raw_input("Verb: ")

print("    It was",  str(time) ,"o'clock when I heard a knock at the door.")

print("    I opened the door and there was a box full of", items, "with a note saying \"From Mr." , name.title() , ".\" ")

print("    Just as I closed the door I heard a scream \" " , scream.upper(), ".\"  ")

print("    I froze in place and all I could do was", action , "." )