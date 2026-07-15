name = input("What is your name: ")

def myfun():

    global mylist

    digits = int(input("Hi " + name + ", how many numbers do you want to try sorting? "))
    mylist = []

    while digits != 0:
        myNum = int(input("Enter number: "))
        mylist.append(myNum)
        digits -= 1


confirm = "no"

while confirm != "yes":
    myfun()

    print("Your list is:", mylist)

    confirm = input("Is your list correct? (yes/no): ").lower()

print("We can proceed with the Bubble Sorting Algorithm")