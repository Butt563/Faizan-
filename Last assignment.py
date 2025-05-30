class ChatBot:
    def __init__(self):
        self.responses = {
            'greet': ['Hi!', 'Hey!', 'Hello!'],
            'bye': ['See you later!', 'Bye!', 'Goodbye!']
        }

    def get_response(self, message):
        message = message.lower()
        if 'hello' in message or 'hi' in message:
            return self.responses['greet'][0]
        elif 'bye' in message:
            return self.responses['bye'][0]
        elif 'how are you' in message:
            return self.responses['how are you'][0]
        else:
            return "I am sorry sir I can't understand."

def main():
    bot = ChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Chatbot:", bot.get_response(user_input))

if __name__ == "__main__":
    main()
