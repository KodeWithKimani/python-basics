name = input("What is your name: ")

def myfun():

    global mylist
    global digits

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

def sort_fun():

    for i in range(len(mylist) - 1):

        for x in range(len(mylist) - 1):

            if mylist[x] > mylist[x + 1]:

                temp = mylist[x]
                mylist[x] = mylist[x + 1]
                mylist[x + 1] = temp

    print("Your sorted list is:", mylist)
        

sort_fun()