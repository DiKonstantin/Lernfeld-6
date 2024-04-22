from languages import language


def startSession():
    conversationRunning = True
    print(language.get_message("greet"))
    print(language.get_message("announce_quit"))

    while conversationRunning:
        inp = input("> ")
        if inp == "quit":
            conversationRunning = False
        elif inp == "--l":
            lang = input(language.get_message("enter_language"))
            language.switch_language(lang)
            print(language.get_message("greet"))
        else:
            print(inp)

    print(language.get_message("end_conversation"))


if __name__ == "__main__":
    startSession()
