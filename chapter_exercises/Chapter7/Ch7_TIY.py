#7-1
msg = input("What kind of vehicle would you like to rent? ")
print(f"Let me see if I can find you a {msg}.")

#7-2
table = input("How many people are in your party? ")
table = int(table)

if table >= 8:
    print("We do not have any immediate tables available. The wait will be 20 minutes.")
else: 
    print("We can seat you now.")

#7-3
number = input("Please input a number and hit enter: ")
number = int(number)

if number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The number is not a multiple of 10.")

#7-4
