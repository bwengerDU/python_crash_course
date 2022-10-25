# Ch. 5 
#5-1 write a series of conditional statements. 
origin = 'germany'

print("Is the list of wanted cars manufactured in Japan?")
print( origin == 'japan')

print("Is the list of wanted cars manufactured in Germany?")
print( origin == 'germany')

car = 'porsche'
print("Is car == 'porsche'? I predict True.")
print(car == 'porsche')

print("Is car == 'bmw'? I predict False.")
print(car == 'bmw')

model = 'vintage'
print("Are the desired Porsches vintage or modern? I predict modern == False.")
print(model == 'modern')

model = 'vintage'
print("Are the desired Porsches vintage or modern? I predict modern == True.")
print(model == 'vintage')

#5-3 
alien_color = 'red'

# one version which passes
if alien_color is 'red':
    print("You have lost 2 points")
# one version that fails 
if alien_color is 'green':
    print("You have earned 5 points")

# 5-4
# write an if block 
if alien_color is 'green':
    print("You have earned 5 points")
if alien_color is 'yellow':
    print("You have earned 2 points")
if alien_color is 'orange':
    print("You have lost 2 points")
# write an else block
if alien_color is 'red':
    print("You have been deducted points.")
else: 
    print("You have earned points.")
# if-elif-else block
if alien_color is 'green':
    print("You have earned 5 points")
elif alien_color is 'yellow':
    print("You have earned 2 points")
else:
    print("You have lost 2 points")
#5-6 stages of life extensive elif code
age = 3
if age < 2 :
    print("This person is a baby.")
elif (age >= 2) and (age < 4): 
    print("This person is a toddler.")
elif (age >= 4) and (age < 13): 
    print("This person is a kid.")
elif (age >= 13) and (age < 20): 
    print("This person is a teenager.")
elif (age >= 20) and (age < 65): 
    print("This person is an elder.")
else: 
    print("This person is an elder.")

# 5-7
favorite_fruits = ['orange', 'strawberry', 'kiwi']

if 'kiwi' in favorite_fruits:
    print("Wow, you realy like Kiwis!")
if 'grapes' in favorite_fruits:
    print("Wow, you realy like Grapes!")
if 'orange' in favorite_fruits:
    print("Wow, you realy like Oranges!")
if 'apple' in favorite_fruits:
    print("Wow, you realy like Apples!")
if 'strawberry' in favorite_fruits:
    print("Wow, you realy like Strawberries!")

# 5-8 
usernames = ['admin', 'steve', 'cleclerc', 'csainz', 'pmanning']

# special message for "Admin" and generic message for all other users. 
for username in usernames:
    if username is 'admin':
        print("Hello, Admin. Would you like to see a status report?") 
    else:
        print(f"Hello {username}, welcome back to your account.")
# 5-9 test if list is empty. Then empty list and test again. 
usernames = []
if usernames:
    for username in usernames:
        if username is 'admin':
            print("Hello, Admin. Would you like to see a status report?") 
        else:
            print(f"Hello {username}, welcome back to your account.")
else:
    print("We need to find more users!")
# check usernames
current_users = ['admin', 'steve', 'cleclerc', 'csainz', 'pmanning']
new_users = ['grussel', 'cmakar', 'jsakic', 'steve', 'svettel']
upper_users = [x.upper() for x in current_users]

# Combine lower case and upper case lists, print to ensure correctly merged
all_current_users = current_users + upper_users
print(all_current_users)

for new_user in new_users:
    if new_user in all_current_users:
        print(f"Sorry, {new_user} is in use. Please select another username.")
    else:
        print(f"Congratulations, {new_user} is available.")

#5-11
numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
    if number is '1':
        print(f"{number}st")
    elif number is '2':
        print(f"{number}nd")
    elif number is '3':
        print(f"{number}rd")
    else:
        print(f"{number}th")
