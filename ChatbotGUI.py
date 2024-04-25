import tracemalloc
import asyncio
import threading
from tkinter import *
from tkinter import messagebox
from brain import Cortex  # Import the Brain class from brain.py


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        self.brain_instance = Cortex()

        master.geometry('500x570+100+30')
        master.title('Chatbot created by CtrlAltDefeat')
        master.config(bg='grey')
        master.resizable(False, False)

        logoPic = PhotoImage(file=r'DesignOhneTitel.png')
        logoPicLabel = Label(master, image=logoPic, bg='white')
        logoPicLabel.pack(pady=5)

        center_frame = Frame(master)
        center_frame.pack()

        scrollbar = Scrollbar(center_frame)
        scrollbar.pack(side=RIGHT)

        self.textarea = Text(center_frame, font=('arial', 20, 'bold'), height=5, yscrollcommand=scrollbar.set,
                             wrap='word')
        self.textarea.pack()
        scrollbar.config(command=self.textarea.yview)

        self.questionField = Entry(center_frame, font=('arial', 20, 'bold'))
        self.questionField.pack(pady=10, fill=X)

        ask_button = Button(master, text="Submit", command=lambda: asyncio.create_task(self.submit_button_click()))
        ask_button.pack()

    async def submit_button_click(self):
        question_text = self.questionField.get()
        await self.brain_instance.send_message(question_text)
        self.questionField.delete(0, END)

    async def output_loop(self):
        while True:
            answer = await self.brain_instance.get_next_answer()
            if answer:
                self.textarea.insert(END, f"\nReceived answer: {answer}\n")
                self.textarea.see(END)


async def main():
    tracemalloc.start()  # Enable tracemalloc to get the object allocation traceback

    root = Tk()  # Create a Tk instance for the GUI
    chatbot = ChatbotGUI(root)  # Create Chatbot instance
    cortex = Cortex()
    await asyncio.gather(chatbot.output_loop(), root.mainloop())

    # await asyncio.create_task(chatbot.output_loop())  # Run the asyncio event loop with Chatbot instance in a separate thread


if __name__ == "__main__":
    asyncio.run(main())
