def chatbot():
    print("Welcome to the Mishra chatbot😊.")
    while True:
        user_input = input("You: ")
        user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: How can i help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine.")
        elif "what is your name" in user_input:
            print("Chatbot: My name is Mishra ji")
        elif "quit" in user_input or "exit" in user_input:
            print("Chatbot: Thanks for chattig with me😊.")
            break
        else:
            print("Chatbot: Im not getting your point.")

chatbot()