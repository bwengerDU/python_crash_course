#10-1 created sentences in learning_python.txt file. Import file and read it three times
file_path = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/learning_python.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents*3)

# import file print once by reading in entire file, 
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

# #once by looping over the file object, and 
filename = file_path

with open(filename) as file_object:
    for line in file_object:
        print(line)

# #once by storig the lines in a list and then working with the outside the with block
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    print(len(line))

# 10-2
filename = file_path

with open(filename) as f:
    lines = f.readlines()

for line in lines:
# replace Python with C.
    print(line.replace('Python', 'C++'))

#10-3 prompt for name and writing the response to a new file, guest.txt
user_name = input('\nWhat is your name?')
filename = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(user_name) 

#10-4 while loop to prompt names, print greeting to response, then store response to a guest_book.txt
filename = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    user_name = input('\nWhat is your name?') 
   
    if user_name == 'quit':
        break
    else:
        user_name = (f"\n{user_name}")

        with open(filename, 'a') as file_object:
            file_object.write(f"\n{user_name}") 
        print(f"Welcome, {user_name}! We hope you enjoy your stay.")

# 10-5
filename = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/reasons.txt'

print("When you are finished answering the questions below, please enter 'quit' to exit")

while True:
    reasons = input('Why do you like programming?')

    if reasons == 'quit':
        break
    else:
        reasons = (f"\n{reasons}")

        with open(filename, 'a') as file_object:
            file_object.write(f"\n{reasons}")         
#10-6 prompt for two numbers, add them together. Create a friendly error message if anything other than numbers are entered. 
try:
    x = input("Please provide the first number to be added: ")
    x = int(x)

    y = input("Please provide the second number to be added: ")
    y = int(y)
except ValueError:
    print("Sorry, I can only add numbers.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")

#10-7 wrap previous coding into a while statement to allow users to continually 
print("Please enter 'quit' at any time to quit the program")
while True:
    try:
        x = input("Please provide the first number to be added: ")
        if x == 'quit':
            break
        x = int(x)

        y = input("Please provide the second number to be added: ")
        if y == 'quit':
            break
        y = int(y)
    except ValueError:
        print("Sorry, I can only add numbers.")
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")

#10-8 read in two files, make on file an error and have an error message print that is user friendly 
cats_file = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/cats.txt'
dogs_file = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/dog.txt'
files = [cats_file, dogs_file]

for file in files:
    print(f"\nReading file: {file}")
    try:
        with open(file) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")

#10-9 format the above code to perform a silent pass on the missing file like 
cats_file = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/cats.txt'
dogs_file = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/dog.txt'
files = [cats_file, dogs_file]

for file in files:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {file}")
        print(contents)

#10-10 use large text file and find how many times particular words appear in the famous book
def count_one_word(filename, word):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf8') as f:
            contents = f.read()
    except FileNotFoundError: 
        print(f"Sorry, the file {filename} does not exist.")
    else:
        word_count = contents.lower().count(word)
        print(f"The book contains the word {word} approximately {word_count} times.")

metamorph = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/the_metamorphosis.txt' 
count_one_word(metamorph, 'cold')

bible = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/the_bible.txt' 
count_one_word(bible, 'cold')

crimpun = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/crime_punishment.txt' 
count_one_word(crimpun, 'cold')

# search for the word 'the' with no space given, then once with a space after 'the ' 
the_search = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/crime_punishment.txt' 
count_one_word(the_search, 'the')

the_space_search = '/Users/bryanwenger/Desktop/python_work/python_crash_course/chapter_exercises/Chapter10/crime_punishment.txt' 
count_one_word(the_space_search, 'the ')

#10-11 prompt for favorite number, store in json dump and write a program that remembers the favorite number
