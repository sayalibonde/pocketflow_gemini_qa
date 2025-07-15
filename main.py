from chatbot_flow import create_flow

def main():
    flow = create_flow()
    print("🤖 Gemini PocketFlow Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: 👋 Bye!")
            break

        result = flow.run({"input": user_input})
        print("Bot:", result)

if __name__ == "__main__":
    main()
