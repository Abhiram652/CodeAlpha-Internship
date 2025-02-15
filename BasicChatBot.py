import random
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm a chatbot, so I don't have feelings, but I'm here to help!"]
    ],
    [
        r"what is your name?",
        ["I'm a basic chatbot. You can call me ChatBot!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ").lower()
        if user_input == "quit":
            print("Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    start_chat()
