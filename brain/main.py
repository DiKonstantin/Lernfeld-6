import asyncio
import time
from brain.languages import language
import concurrent.futures

class Brain:
    """The Main Brain Class"""

    def __init__(self):
        self.message_queue = asyncio.Queue()
        self.answer_queue = asyncio.Queue()

        current_timestamp = int(time.time())
        filename = "log_" + str(current_timestamp) + ".txt"
        self.file = open(filename, "w")

    async def startSession(self):
        conversation_running = True
        await self.sendMessage(language.get_message("greet"))
        await self.sendMessage(language.get_message("announce_quit"))

        while conversation_running:
            await asyncio.sleep(0.1)  # prevent too much load
            if not self.message_queue.empty():
                next_message = await self.message_queue.get()
                self.file.write(next_message + "\n")
                if next_message == "quit":
                    conversation_running = False
                else:
                    await self.sendAnswer("You entered " + next_message)

        await self.sendAnswer(language.get_message("quit"))
        self.file.close()

    async def sendMessage(self, message):
        await self.message_queue.put(message)

    async def sendAnswer(self, message):
        await self.answer_queue.put(message)
        self.file.write(message + "\n")
        self.file.flush()

    async def getNextAnswer(self):
        while self.answer_queue.empty():
            await asyncio.sleep(0.1)
        return await self.answer_queue.get()

async def input_loop(brain):
    loop = asyncio.get_event_loop()
    while True:
        user_input = await loop.run_in_executor(None, input, "")
        print()
        await brain.sendMessage(user_input)

async def output_loop(brain):
    while True:
        answer = await brain.getNextAnswer()
        if answer:
            print("Received answer:", answer)
            print("Enter text:", end=" ", flush=True)

async def main():
    brain = Brain()
    asyncio.create_task(brain.startSession())
    asyncio.create_task(input_loop(brain))
    asyncio.create_task(output_loop(brain))

    # Create an event to keep the main coroutine running indefinitely
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

