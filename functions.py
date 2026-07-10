#function(argument)

name = input("What's your name? ")

#Strip removes unnecessary white spaces
#Title capitalise the first letter of each word
name = name.strip().title()

#concatination forms 

print("Hi " + name)
print("Hi", name)
print(f"Hi {name}") #f strings