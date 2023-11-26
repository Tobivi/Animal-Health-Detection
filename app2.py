import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you",
        ["I'm good, thank you.", "I'm doing well."]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot.", "You can call me ChatGPT."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Take care!"]
    ],
]

chatbot = Chat(pairs, reflections)

def chat_with_user():
    print("Hello! I'm a chatbot. You can type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_user()
