#6-1
person = {
    'first_name' : 'daniel', 
    'last_name' : 'banta', 
    'age' : '34', 
    'city' : 'bellevue',
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2
favorite_numbers = {
    'colleen' : '19', 
    'nate': '29', 
    'cale' : '8',
    'gabe' : '92', 
    }
print(favorite_numbers['colleen'])
print(favorite_numbers['nate'])
print(favorite_numbers['cale'])
print(favorite_numbers['gabe'])

#6-3
words = {
    'list' : 'a collection of items in a particular order contained within square brackets',
    'string' : 'series of characters contained within quotes',
    'looping' : 'applying an action or set of actions with every item in a list and designated by the word for',
    'indentation' : 'python formatting used to determine how a line or group of lines is related tot he rest of the program',
    'tuple' : 'a value or series of values that cannot change, or immutable, and designated by being contained in parentheses',
    }

print(f"\nList: \n\t{words['list']}")
print(f"\nString: \n\t{words['string']}")
print(f"\nLooping: \n\t{words['looping']}")
print(f"\nIndentation: \n\t{words['indentation']}")
print(f"\nTuple: \n\t{words['tuple']}")

#6-4 make a loop through print function for the exercise in 6-3 above
for key, value in words.items():
    print(f"\n{key}: {value}")

#6-5 
rivers = {
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'colorado' : 'usa',
    }

#loop through and print message
for key, value in rivers.items():
    print(f"The {key.title()} River is located in {value.title()}.")

# just print the river names
for key in rivers.keys():
    print({key})

# just print the country names
for value in rivers.values():
    print({value})

#favorite languages poll, print message for those that have taken and one for those that have not. 
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
    }
to_take = ['mike', 'barry', 'selena', 'edward', 'erin']

for name in favorite_languages.keys():
    if name in to_take:
        print(f"Hello {name.title()}, thank you for previously taking the poll.")
    else:
        print(f"{name.title()}, please take the poll at your nearest convenience. Thanks!")

#6-7
#6-1
dan = {
    'first_name' : 'daniel', 
    'last_name' : 'banta', 
    'age' : '34', 
    'city' : 'bellevue',
    }
nate = {
    'first_name' : 'nathan', 
    'last_name' : 'mackinnon', 
    'age' : '26', 
    'city' : 'halifax',
    }
cale = {
    'first_name' : 'cale', 
    'last_name' : 'makar', 
    'age' : '23', 
    'city' : 'boston',
    }
peoples = [dan, nate, cale]

for people in peoples:
    print(people)

#6-8 Pets
canoli = {
    'animal' : 'dog',
    'owner' : 'joe'
    }
bruce = {
    'animal' : 'bear',
    'owner' : 'danny'
    }
casper = {
    'animal' : 'cat',
    'owner' : 'bill'
    }
pets = [canoli, bruce, casper]

for pet in pets:
    print(pet)

#6-9 
favorite_places = {
    'allen' : ['paris', 'rome', 'madrid'],
    'aaron' : ['phuket', 'bangkok', 'beijing'],
    'connor' : ['sydney', 'perth', 'auckland'],
    }
for name, place in favorite_places.items():
    print(f"{name}'s favorite destinations are {place}")

#6-10
favorite_numbers = {
    'colleen' : ['19', '21'], 
    'nate': ['29', '18'], 
    'cale' : ['8', '88'],
    'gabe' : ['92', '19'], 
    }
for person, number in favorite_numbers.items():
    print(f"{person}'s favorite numbers are {number}.")

#6-11
cities = {
    'denver' : {
        'state' : 'colorado', 
        'population' : '500,000', 
        'team' : 'home of the rockies',
        },
    'austin' : {
        'state' : 'texas', 
        'population' : '1,000,000', 
        'team' : 'home of the longhorns',
        },
    'miami' : {
    'state' : 'florida', 
    'population' : '3,000,000', 
    'team' : 'home of the dolphins',
        },
    }

print(cities)

