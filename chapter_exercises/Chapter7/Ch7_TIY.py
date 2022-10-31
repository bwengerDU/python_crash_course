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
prompt = "\nWhich toppings would you like on your pizza? "
prompt += "\nEnter 'finished' when you have provided all desired toppings: "
message = ""
while message != 'finished' : 
    message = input(prompt)
    print(f"I will add {message} to your pizza.")

# 7-5 
prompt = "\nEnter '0' when you are finished."
prompt += "\nPlease enter your age: "

while True:
    age = input(prompt)
    age = int(age)

    if age == 0:
        break
    elif age <= 3:
        print("Your ticket is free")
    elif age <= 10:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
# 7-6
# Use an active variable to exit loop from 7-5
prompt = "\nEnter '0' when you are finished."
prompt += "\nPlease enter your age: "

while True:
    age = input(prompt)
    age = int(age)

    if age == 0:
        break
    elif age <= 3:
        print("Your ticket is free")
    elif age <= 10:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")

# Use a conditional statement to control how long the loop runs
prompt = "\nEnter '0' when you are finished."
prompt += "\nPlease enter your age: "

active = True
while active:
    age = input(prompt)
    age = int(age)

    if age == 0:
        active = False
    elif age <= 3:
        print("Your ticket is free")
    elif age <= 10:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")

# 7-8
# list of sandwiches and empty list of finished sandwiches
sandwiches = ['italian', 'turkey', 'veggie', 'snarf']
finished_sandwiches = []

# loop to 
while sandwiches: 
    current_sandwich = sandwiches.pop()

    print(f"I have finished making your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)
# List all finished sandwiches
print(f"\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches: 
    print(finished_sandwich.title())

#7-9 
#Add pastrami to the list three times
sandwiches = ['pastrami', 'italian', 'turkey', 'pastrami', 'veggie', 'snarf', 'pastrami']
finished_sandwiches = []

#Message and remove Pastrami now that they are out of meat
print("Sorry, we are out of Pastrami and are no longer able to make any more. Please select another sandwich.")

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')
# loop to 
while sandwiches: 
    current_sandwich = sandwiches.pop()

    print(f"I have finished making your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)
# List all finished sandwiches
print(f"\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches: 
    print(finished_sandwich.title())

# 7-10 
responses = {}

# Set a flag to signal poling is active
polling_active = True

while polling_active: 
    response = input("If you could go anywhere in the world, where would you like to go?")
#Store the responses in a list
    responses = response
# Query whether any additional participants will be polled
    repeat = input("Will anyone else be taking the poll? Y/N?")
    if repeat == 'N':
        polling_active = False
#Provide polling results
print("\nThe polling results are as follows:")
for response in responses.list():
    print(f"A desired vacation location is {response}.")    