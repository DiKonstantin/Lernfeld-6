import time

from languages import language


def startSession():
    current_timestamp = int(time.time())
    filename = "_" + str(current_timestamp) + ".txt"
    file = open(filename, "w")
    conversation_running = True
    print(filename)
    print(language.get_message("greet"))
    print(language.get_message("announce_quit"))

    while conversation_running:
        inp = input("> ")
        file.write(inp + "\n")
        if inp == "quit":
            conversation_running = False
        elif inp == "--l":
            file.write(language.get_message("enter_language") + " ")
            lang = input(language.get_message("enter_language"))
            file.write(lang + "\n")
            language.switch_language(lang)
            print(language.get_message("greet"))
            file.write(language.get_message("greet") + "\n")
        else:
            print("You entered: " + inp)
            file.write("You entered: " + inp + "\n")

    print(language.get_message("end_conversation"))


if __name__ == "__main__":
    startSession()
