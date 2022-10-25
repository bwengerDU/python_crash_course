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

print(f"List: \n\t{words['list']}")
print(f"String: \n\t{words['string']}")
print(f"Looping: \n\t{words['looping']}")
print(f"Indentation: \n\t{words['indentation']}")
print(f"Tuple: \n\t{words['tuple']}")