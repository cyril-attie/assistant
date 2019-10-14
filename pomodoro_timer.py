#!/home/tumbling20s/projects/assistant/venv/bin/python
'''
Sets a 45min timer after displaying an info message. 
5 min before the end alerts the user. The user can delay by not accepting nor closing the alert message.   
'''
from tkinter import messagebox,Tk
from time import sleep
from os import system

# hide main window
root = Tk()
root.withdraw()
s=messagebox.showinfo("Info", "You got 45 min")

MINUTES=45
sleep((MINUTES-5)*60)

# message box display
s=messagebox.showwarning("Warning","5 min to Finnish")

if s=='ok':
    sleep(300)
    os.system('systemctl suspend')