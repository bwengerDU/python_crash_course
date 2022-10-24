# 3-4 
guests = ['joe sakic', 'peter forsberg', 'milan hejduk', 'adam foote', 'chris drury']
print(f"Hello {guests[0].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[1].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[2].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[3].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[4].title()}, you are invited to attend my birthday party on Halloween Night")

#3-5
guests.insert(2, 'cale makar')
uta = 'milan hejduk'
guests.remove(uta)
print(f"Hello {guests[0].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[1].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[2].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[3].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[4].title()}, you are invited to attend my birthday party on Halloween Night")

#3-6 
guests.insert(0, 'nathan macKinnon')
guests.insert(2, 'mikko rantanen')
guests.append('gabriel landeskog')
print(f"Hello {guests[0].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[1].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[2].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[3].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[4].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[5].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[6].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[7].title()}, you are invited to attend my birthday party on Halloween Night")
print("We were able to find a larger venue and have expanded our guest list. We can't wait to see you all there!")

# 3-7 
print("I do apologize for being the flakiest person ever. The venue has canceled and we are instead left with a much smaller location. Only two guests will be invited and you are one of them")
uta_1 =guests.pop()
print(f"I am sorry to inform you, {uta_1.title()}, that space is no longer available at the party.")
uta_2 =guests.pop()
print(f"I am sorry to inform you, {uta_2.title()}, that space is no longer available at the party.")
uta_3 =guests.pop()
print(f"I am sorry to inform you, {uta_3.title()}, that space is no longer available at the party.")
uta_4 =guests.pop()
print(f"I am sorry to inform you, {uta_4.title()}, that space is no longer available at the party.")
uta_5 =guests.pop()
print(f"I am sorry to inform you, {uta_5.title()}, that space is no longer available at the party.")
uta_6 =guests.pop()
print(f"I am sorry to inform you, {uta_6.title()}, that space is no longer available at the party.")
print(f"Hello {guests[0].title()}, you are invited to attend my birthday party on Halloween Night")
print(f"Hello {guests[1].title()}, you are invited to attend my birthday party on Halloween Night")

del guests[1]
del guests[0]
print(guests)