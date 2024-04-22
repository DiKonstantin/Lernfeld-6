from languages import language


def startSession():
    conversationRunning = True
    while conversationRunning:
        print("Welcome to Brain Language Conversation!")
        print("Type 'quit' to quit")
        inp = input("> ")
        if inp == "quit":
            conversationRunning = False
        else:
            print(inp)
    print("This is English")
    print(language.get_message("greet"))
    print("This is German")
    language.switch_language("de")
    print(language.get_message("greet"))


if __name__ == "__main__":
    startSession()
