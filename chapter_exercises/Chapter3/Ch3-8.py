# 3-8
# original list out of order
places = ['rio', 'moscow','budapest','paris','istanbul']
print(places)

#temporarily sort the list
print(sorted(places))

#showcase that it is not permanently changed
print(places)

#reverse the order, and then reverse it again to return it back to original
places.reverse()
print(places)

places.reverse()
print(places)

# Print it so it's in alphabetical order permanently
places.sort()
print(places)

# now permanently have in reverse alphabetical order
places.sort(reverse=True)
print(places)

# get a count of locations
len(places)