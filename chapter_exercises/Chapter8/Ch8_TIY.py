# 8-1
def display_message():
    """Display Message Describing Lessons in this chapter"""
    print("In this chapter I am learning about functions.")

display_message()

#8-2
def favorite_book(title):
    """Favorite Book Message"""
    print(f"My favorite book is {title.title()}.")

favorite_book('The Outsiders')

#8-3
def make_shirt(size, text):
    """Size and Text of Message Program"""
    print(f"You have successfully ordered a shirt in size {size} with the message '{text}' written on the back.")

make_shirt('Medium', 'Hello Moto!')

# Now call with keyword arguments
make_shirt(text='Hallo Moto', size='Large')

#8-4
def large_shirt(size='Large', text='I love Python!'):
    """Setting one the elements as a constant"""
    print(f"You have ordered a Large shirt with the message, 'I love Python' on the back.")

large_shirt()

#Medium version
def medium_shirt(size='Medium', text='I love Python!'):
    """Setting one the elements as a constant"""
    print(f"You have ordered a {size} shirt with the message, '{text}' on the back.")

medium_shirt()

#Standard message shirt with leaving the size adjustable. 
def any_shirt(size, text='All Hail, Cale!'):
    """Any size shirt, standard message"""
    print(f"You have ordered a size {size} shirt with the message {text} written on the back")

any_shirt('Small')

#8-5 Cities
def describe_city(city, country='Germany'):
    """Name of City and Country it is in."""
    print(f"{city.title()} is located in {country.title()}.")
describe_city('Munich')
describe_city('Berlin')
describe_city('Paris')

#8-6
def city_country(city, country):
    """City Names Function"""
    print(f"{city.title()}, {country.title()}")

city_country('santiago', 'chile')
city_country('berlin', 'germany')
city_country('paris', 'france')

#8-7
def make_album(artist_name, album_name):
    """Function values into list"""
    disc = {'artist' : artist_name, 'album' : album_name}
    return disc

discography_1 = make_album('metallica', 'master of puppets')
discography_2 = make_album('the doors', 'soft parade')
discography_3 = make_album('steve miller band', 'greatest hits')
print(discography_1)
print(discography_2)
print(discography_3)

#add a 'none' option for storing the number of songs on each album if known
def make_album(artist_name, album_name, number_songs=None):
    """Function values into list"""
    disc = {'artist' : artist_name, 'album' : album_name, 'number of songs' : number_songs}
    if number_songs:
        disc[number_songs] = number_songs
    return disc

discography_1 = make_album('metallica', 'master of puppets')
discography_2 = make_album('the doors', 'soft parade', number_songs=12)
discography_3 = make_album('steve miller band', 'greatest hits', '14')
print(discography_1)
print(discography_2)
print(discography_3)

#8-8 While loop that allows user input 
def make_album(artist_name, album_name):
    """User input to allow for discography to be stored"""
    disc = {f"One of my favorite albums is {album_name.title()} by {artist_name.title()}."}
    return disc
while True:
    print("\nWho is your favorite artist? If complete please enter 'quit'")
    print("\nWhat is your favorite album of theirs?")
    
    a_name = input('artist_name : ') 
    if a_name == 'quit':
        break
    al_name = input('album_name : ')
    if al_name == 'quit':
        break
    formatted_message = make_album(a_name, al_name)
    print(f"My favorite album is {al_name} by {a_name}.")

#8-9
def short_messages(sms):
    """Print short messages from list"""
    for sm in sms:
        msg = f"{sm}"
        print(msg) 

smsg = ['Is this still available?', 'Are you willing to negotiate on the price?', 'When are you available to meet and show the vehicle?', 'Does it have a clean, Colorado title?']
short_messages(smsg)

#8-10
smsg = ['Is this still available?', 'Are you willing to negotiate on the price?', 'When are you available to meet and show the vehicle?', 'Does it have a clean, Colorado title?']
sent_msgs = []

while smsg:
    current_msg = smsg.pop() 
    print(f"{current_msg}")
    sent_msgs.append(current_msg)
print("\nThe following messages have been sent: ")
for sent_msg in sent_msgs:
    print(sent_msg)

print(smsg)

#8-11
def send_messages(unsent_msgs, sent_msgs):
    """Print each unsent message and store in sent messages"""
    while unsent_msgs:
        current_msg = unsent_msgs.pop() 
        print(f"{current_msg}")
        sent_msgs.append(current_msg)    
def sent_messages(sent_msgs):
    """Show which models were printed"""
    print("\nThe followning messages have been sent: ")
    for sent_msg in sent_msgs:
        print(sent_msg)
unsent_msgs = ['Is this still available?', 'Are you willing to negotiate on the price?', 'When are you available to meet and show the vehicle?', 'Does it have a clean, Colorado title?']
sent_msgs = []

send_messages(unsent_msgs [:], sent_msgs)
sent_messages(sent_msgs)

print(unsent_msgs)

#8-12
def make_sandwich(*toppings):
    """Summarize the sandwich ordered"""
    print("\nWe are making a sandwich with the following ingredients:")
    for topping in toppings:
        print(f"- {topping.title()}")
make_sandwich('avocado', 'bacon', 'tomatoes')
make_sandwich('mustard', 'spinach', 'olives')
make_sandwich('lettuce')

#8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing information about myself"""
    user_info['first _name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('cale', 'makar', team='colorado avalanche', position='defenseman', number='8')
print(user_profile)

#8-14
def car(manufacturer, model, **car_info):
    """Build car profile and additional info input"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car_profile = car('porsche', '928', engine='v8', color='blue', manual_transmission=True)
print(car_profile)


