import tracemalloc
import asyncio
import threading
from tkinter import *
from tkinter import messagebox
from brain import Cortex  # Import the Brain class from brain.py


class ChatbotGUI:
    def __init__(self, master, cortex):
        self.master = master
        self.brain_instance = cortex

        self.master.geometry('500x570+100+30')
        self.master.title('Chatbot created by CtrlAltDefeat')
        self.master.config(bg='grey')
        self.master.resizable(False, False)

        self.logoPic = PhotoImage(file=r'DesignOhneTitel.png')
        self.logoPicLabel = Label(master, image=self.logoPic, bg='white')
        self.logoPicLabel.pack(pady=5)

        self.center_frame = Frame(master)
        self.center_frame.pack()

        self.scrollbar = Scrollbar(self.center_frame)
        self.scrollbar.pack(side=RIGHT)

        self.textarea = Text(self.center_frame, font=('arial', 12, 'bold'), height=5, yscrollcommand=self.scrollbar.set,
                             wrap='word')
        self.textarea.pack()
        self.scrollbar.config(command=self.textarea.yview)

        self.questionField = Entry(self.center_frame, font=('arial', 20, 'bold'))
        self.questionField.pack(pady=10, fill=X)

        self.ask_button = Button(master, text="Submit", command=self.submit_button_click)
        self.ask_button.pack()

    def submit_button_click(self):
        question_text = self.questionField.get()
        self.brain_instance.send_message(question_text)
        self.questionField.delete(0, END)
        self.textarea.insert(END, f"Me: {question_text} \n")


    async def output_loop(self):
        while True:
            await asyncio.sleep(0.1)
            answer = self.brain_instance.get_next_answer()
            if answer:
                self.textarea.insert(END, f"Chatty: {answer}\n")
                self.textarea.see(END)

def run_cortex(cortex):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(cortex.start_session())
    loop.close()

def run_chatbotOutput(chatbot):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(chatbot.output_loop())
    loop.close()

def main():
    tracemalloc.start()
    root = Tk()  # Create a Tk instance for the GUI
    cortex = Cortex()
    chatbot = ChatbotGUI(root, cortex)  # Create Chatbot instance
    thread1 = threading.Thread(target=run_cortex, args=(cortex,))
    thread1.start()
    thread2 = threading.Thread(target=run_chatbotOutput, args=(chatbot,))
    thread2.start()
    print("Vor der ASY")
    chatbot.master.mainloop()
    thread1.join()
    thread2.join()

    print("5 vor 12")
    exit()



if __name__ == "__main__":
    asyncio.run(main())
