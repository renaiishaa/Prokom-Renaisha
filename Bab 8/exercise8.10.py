messages = [
    "Hello, how are you?",
    "Have a nice day!",
    "Keep learning Python.",
    "Good luck with your work."
]

sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

send_messages(messages, sent_messages)

print("\nOriginal messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)