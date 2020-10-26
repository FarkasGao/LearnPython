messages = ["This is a message", 
            "This is another message",
            "This is the third message",]
messages_get = []            
def show_message(messages):
    for message in messages:
        print(message)
        
def sent_message(messages, to):
    while messages:
        sent = messages.pop()
        print(f"sent \"{sent}\"")
        to.append(sent)
        
show_message(messages)
sent_message(messages, messages_get)

print(messages)
print(messages_get)