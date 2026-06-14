responses = {
    "hello": "Hi there!",
    "how are you": "I am fine. Thanks for asking!",
    "bye": "Goodbye!"
}

print("Bot: Hello! Type 'exit' to quit.")

while True:
    user = input("You: ").lower().strip()

    if user == "exit":
        print("Bot: Exiting chatbot...")
        break

    reply = responses.get(user, "Sorry, I don't understand.")
    print("Bot:", reply)