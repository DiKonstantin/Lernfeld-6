import time

from languages import language


def startSession():
    current_timestamp = int(time.time())
    filename = "_" + str(current_timestamp) + ".txt"
    file = open(filename, "w")
    conversation_running = True
    print(filename)
    print(language.get_message("greet"))
    print("If you want to switch languages type --l into the console\n")
    print("*"*32)
    print(language.get_message("options"))
    print("1. " + language.get_message("one")
     + "\n2. " + language.get_message("two")
     + "\n3. " + language.get_message("three")
     + "\n4. " + language.get_message("four")
     + "\n5. " + language.get_message("five")
     + "\n6. " + language.get_message("six")
     + "\n7. " + language.get_message("seven")
     + "\n8. " + language.get_message("eight")
     + "\n9. " + language.get_message("nine"))
    while conversation_running:
        inp = input("> ")
        file.write(inp + "\n")
        if inp == "1":
            print("You chose: " + inp +".")
            print() #Antwort auf User Input

            print(language.get_message("leave_message"))
            leaveInp = input("> ")
            if leaveInp == "y" or inp == "Y" or leaveInp == "j" or leaveInp == "J":
              print("Im glad it helped you, if you still have any Questions in detail regarding your problem feel free to call one of our Experts")
            elif leaveInp == "n" or leaveInp == "N":
                print("Im sorry to hear, maybe we can help you over the Phone you can call us: +49 16672891552")
            else:
                conversation_running = False
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
