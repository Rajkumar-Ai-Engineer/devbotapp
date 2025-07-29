from chains.command_chain import handle_user_input

def main():
    print("DevBotAI started..")
    print("Type 'exit' to end the conversation.")
    while True:
        user_input = input("Enter your prompt:")
        if user_input.lower() == 'exit':
            print("Exiting DevBotAI...")
            break
        try:
            response = handle_user_input(user_input)
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()