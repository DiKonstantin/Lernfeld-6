from tkinter import *


root = Tk()

root.geometry('500x570+100+30')
root.title('Chatbot created by CtrlAltDefeat')
root.config(bg='grey')
root.resizable(False,False)

logoPic = PhotoImage(file=r'DesignOhneTitel.png')
logoPicLabel = Label(root, image=logoPic, bg='white')
logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('arial',20,'bold'),height=5,yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(centerFrame, font=('arial',20,'bold'))
questionField.pack(pady=10,fill=X)

askButton = Button(root)
askButton.pack()
askButton['text'] = 'Submit'


root.mainloop()