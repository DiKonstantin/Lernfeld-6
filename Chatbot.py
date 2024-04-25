import tracemalloc
import asyncio
import threading
from tkinter import *
from tkinter import messagebox
from brain import Cortex  # Import the Brain class from brain.py

class Chatbot:
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

        centerFrame = Frame(master)
        centerFrame.pack()

        scrollbar = Scrollbar(centerFrame)
        scrollbar.pack(side=RIGHT)

        self.textarea = Text(centerFrame, font=('arial', 20, 'bold'), height=5, yscrollcommand=scrollbar.set, wrap='word')
        self.textarea.pack(side=LEFT)
        scrollbar.config(command=self.textarea.yview)

        self.questionField = Entry(centerFrame, font=('arial', 20, 'bold'))
        self.questionField.pack(pady=10, fill=X)

        askButton = Button(master, text="Submit", command=self.submit_button_click)
        askButton.pack()

    async def submit_button_click(self):
        question_text = self.questionField.get()
        self.textarea.insert(END, f"\nYou entered: {question_text}\n")
        await self.brain_instance.send_message(question_text)
        self.questionField.delete(0, END)

    async def output_loop(self):
        while True:
            answer = await self.brain_instance.get_next_answer()
            if answer:
                self.textarea.insert(END, f"\nReceived answer: {answer}\n")
                self.textarea.see(END)

def run_gui(chatbot):
    root = Tk()
    chatbot.master = root  # Set the master of the chatbot to the new Tk instance
    root.mainloop()


async def main():
    tracemalloc.start()  # Enable tracemalloc to get the object allocation traceback

    root = Tk()  # Create a Tk instance for the GUI
    chatbot = Chatbot(root)  # Create Chatbot instance
    root_thread = threading.Thread(target=run_gui, args=(chatbot,))  # Run GUI in a separate thread with Chatbot instance
    root_thread.start()

    await asyncio.create_task(chatbot.output_loop())  # Run the asyncio event loop with Chatbot instance in a separate thread

if __name__ == "__main__":
    asyncio.run(main())
