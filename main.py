from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3

#new information to chatbot
#data_list=['What you do in free time',
          # 'I memorize things in my free time']
bot=ChatBot('Bot')
trainer=ListTrainer(bot)
for files in os.listdir('data/english/'):

    data=open('data/english/'+files,'r',encoding='utf-8').readlines()
trainer.train(data)


def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You:'+question+'\n\n')
    textarea.insert(END, 'Bot:' + str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0,END)
root=Tk()
root.geometry('500x570+100+30')
root.title('Chatbot created by Sai Swetha')
root.config(bg='blue')
logopic=PhotoImage(file='pic.png')
logopiclabel=Label(root,image=logopic)
logopiclabel.pack(pady=5)#by default top

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)
textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)
questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)
askpic=PhotoImage(file='ask.png')
askButton=Button(root,image=askpic,command=botReply)
askButton.pack()
def click(event):
    askButton.invoke()
root.bind('<Return>',click)
root.mainloop()
