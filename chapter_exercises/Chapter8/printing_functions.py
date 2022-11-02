# 8-15
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