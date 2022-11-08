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
#10-6
