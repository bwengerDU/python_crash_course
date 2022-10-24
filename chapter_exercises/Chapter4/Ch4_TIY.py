# 4-1
# List
pizzas = ['supreme', 'pepperoni', 'veggie']

#for loop to print name of pizza
for pizza in pizzas: 
    print(f"I like {pizza} pizza!")

# Add additional sentence outside of loop
print("If you were made of pizza, would you eat yourself? Heck, I know I would!")

# 4-2
#Animals list
animals = ['dog', 'wolf', 'coyote']

#for loop statement about animals
for animal in animals:
    print(f"A {animal} has four legs and a tail.")

# sentence outside of loop
print("These creatures are excellent runners and balance using their tails.")

#4-3
numbers = list(range(1,21))
print(numbers)

#4-4 I'm not going to actually run this one, but I would instead put in 1 million and 1 instead of 21. 

# 4-5
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6 print odds in range of 1-20
numbers = list(range(1, 21, 2))
print(numbers)

#4-7 print multiples of 3 from 3-30
numbers = [value*3 for value in range(1,11)]
print(numbers)

#4-8 cube numbers in range 1-19
numbers = [value**3 for value in range(1,11)]
print(numbers)

#4-9
numbers = []
for value in range(1,11):
    number = value ** 3
    numbers.append(number)
print(numbers)

# 4-10
# List
pizzas = ['supreme', 'pepperoni', 'veggie', 'pesto', 'hawaiian']
print(f"The first three pizzas are:")
for pizza in pizzas[:3]:
    print(pizza.title())
# middle 3
print(f"The middle three pizzas are:")
for pizza in pizzas[1:4]:
    print(pizza.title())

# last three
print(f"The last three pizzas are:")
for pizza in pizzas[-3:]:
    print(pizza.title())
#4-11
# Make a copy
friend_pizzas = pizzas[:]
print(friend_pizzas)
# add a pizza to original list
pizzas.append('meat lovers')
print(pizzas)
# add a pizza to the friend pizza list
friend_pizzas.append('greek')
print(friend_pizzas)
#prove that you have made two separate lists
print("My favorite pizzas are:")
print(pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

#4-13
buffets = ('curry', 'naan', 'aloogobi', 'masaala', 'chettinad')
for buffet in buffets: 
    print(buffet.title())

# try to manipulate the tuple and get an error
#buffets.sort()
#print(buffets)

# two items are replaced on the menue. Reprint the new list
buffets = ('curry', 'lasagna', 'aloogobi', 'pizza', 'chettinad')
for buffet in buffets: 
    print(buffet.title())