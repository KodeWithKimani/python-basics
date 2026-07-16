myNum = int(input("Enter Number: "))

# is_prime checks whether the condition is true or not
is_prime = True

# use for loop to divide each number from 2 to the number chose and checker whether modulus is 0
# if it's 0 then it's not prime
# use myNum//2 + 1  to shorten the range since it'll give te same result
for divisor in range(2, myNum//2 + 1):
    if myNum % divisor == 0:
        is_prime = False
        break

if is_prime:
    print(myNum, "is a prime number")
else:
    print(myNum, "is a composite number")