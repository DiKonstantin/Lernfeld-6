import time
import asyncio

from languages import language


class Brain:
    """The Main Brain Class"""

    def __init__(self):
        self.message_queue = []
        self.answer_queue = []

        current_timestamp = int(time.time())
        filename = "log_" + str(current_timestamp) + ".txt"
        self.file = open(filename, "w")

    async def startSession(self):
        conversation_running = True
        self.sendAnswer(language.get_message("greet"))
        self.sendAnswer(language.get_message("announce_quit"))

        while conversation_running:
            await asyncio.sleep(0.1)  # prevent to much load
            if self.message_queue:
                print("GotMessage")
                next_message = self.message_queue.pop(0)
                self.file.write(next_message + "\n")
                if next_message == "quit":
                    conversation_running = False
                else:
                    self.sendAnswer("You entered " + next_message)

        self.sendAnswer(language.get_message("quit"))

    def sendMessage(self, message):
        self.message_queue.append(message)

    def sendAnswer(self, message):
        self.answer_queue.append(message)
        self.file.write(message)

    async def getNextAnswer(self):
        if self.answer_queue:
            return self.answer_queue.pop(0)
        return None
#        try:
#            return await asyncio.wait_for(self.answer_queue.pop(0), timeout=1)
#        except asyncio.TimeoutError:
#            return None


async def main():
    brain = Brain()
    asyncio.create_task(brain.startSession())  # Start the session coroutine

    while True:
        user_input = input("Enter text: ")
        brain.sendMessage(user_input)

        answer = await brain.getNextAnswer()
        if answer:
            print("Received answer:", answer)

if __name__ == "__main__":
    asyncio.run(main())
