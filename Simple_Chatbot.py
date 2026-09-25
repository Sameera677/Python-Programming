def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hi", "hello", "hey"]:
        return "Hi!"

    elif text in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"

    elif text in ["bye", "goodbye", "see you"]:
        return "Goodbye!"

    elif text == "what is your name?":
        return "I am a simple chatbot!"

    else:
        return "I don't understand that."


def chatbot():
    print("=" * 45)
    print("       Hi! I'm your Chatbot")
    print("Bot: Type 'bye' whenever you want to exit.")
    print("=" * 45)

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            break


if __name__ == "__main__":
    chatbot()