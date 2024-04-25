import asyncio
import time
from brain.languages import language
import concurrent.futures


class Cortex:
    """
    The Main Brain Class

    This Class must be loaded as object and will hande the requests and provides the answers. The Class will log
    every Instance with a timestamped file.

    Attributes:
        message_queue (asyncio.Queue): Queue to send messages to.
        answer_queue (asyncio.Queue): Queue to read answers from.

    """

    def __init__(self):
        """
        Initialize the Cortex Class.

        This method will initiate all queues and opens the log_ file for writing.

        Args:
            No Args
        """
        self.message_queue = asyncio.Queue()
        self.answer_queue = asyncio.Queue()

        current_timestamp = int(time.time())
        filename = "log_" + str(current_timestamp) + ".txt"
        self.file = open(filename, "w")

    async def start_session(self):
        """
        This method will start the main loop of the Cortex Class. This loop will handly asynchronosly the
        message_qeueue and will then send an Anwer into the answer_queue.

        """
        conversation_running = True
        await self.send_message(language.get_message("greet"))
        await self.send_message(language.get_message("announce_quit"))

        while conversation_running:
            await asyncio.sleep(0.1)  # small delay to not have an CPU-overloading loop
            if not self.message_queue.empty():
                next_message = await self.message_queue.get()  # get the next message from the stack. this loop will handle each message one by one.

                # handle now the "quit" message
                if next_message == "quit":
                    conversation_running = False
                # now handle all other messages incoming
                else:
                    ##### REPLACE THE CODE HERE FOR YOUR LOGIC #####
                    await self.send_answer("You entered " + next_message)

        await self.send_answer(language.get_message("quit"))
        self.file.close()

    async def send_message(self, message):
        """
        This method will send a message to the Cortex Class and put it in the message_queue.
        :param message:
        :return: None
        """
        await self.message_queue.put(message)
        self.file.write(message + "\n")
        self.file.flush()

    async def send_answer(self, message):
        """
        This method will send a message the answer_queue. Should only be called from inside the Cortex Class.
        :param message:
        :return: None
        """
        await self.answer_queue.put(message)
        self.file.write(message + "\n")
        self.file.flush()

    async def get_next_answer(self):
        """
        This method will read the next answer from the answer_queue.
        :return: None
        """
        while self.answer_queue.empty():
            await asyncio.sleep(0.1)
        return await self.answer_queue.get()


async def input_loop(brain):
    loop = asyncio.get_event_loop()
    while True:
        user_input = await loop.run_in_executor(None, input, "")
        print()
        await brain.send_message(user_input)


async def output_loop(brain):
    while True:
        answer = await brain.get_next_answer()
        if answer:
            print("Received answer:", answer)
            print("Enter text:", end=" ", flush=True)


async def main():
    brain = Cortex()
    asyncio.create_task(brain.start_session())
    asyncio.create_task(input_loop(brain))
    asyncio.create_task(output_loop(brain))

    # Create an event to keep the main coroutine running indefinitely
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
