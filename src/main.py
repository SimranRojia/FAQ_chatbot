from src.chatbot import chatbot

def main():
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit']:
            break
        response = chatbot(user_query)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
