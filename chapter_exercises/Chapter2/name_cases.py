name = "Bryan"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

message = f"Hello {name.upper()}, would you like to learn some Python today?"
print(message)

message = f"Hello {name.lower()}, would you like to learn some Python today?"
print(message)

message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

quote = "\"An analogy is a thought with another thought's hat on.\""
print(f"Britta Perry once said, {quote}")

quote = "\"An analogy is a thought with another thought's hat on.\""
famous_person = "Britta Perry"
print(f"{famous_person} once said, {quote}")

ws_name = " Britta Perry \nfrom \n\tcommunity "
print(ws_name)

print(ws_name.lstrip())

print(ws_name.rstrip())

print(ws_name.strip())