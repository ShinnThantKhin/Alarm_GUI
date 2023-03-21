# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:29:39 2022

@author: Grace
"""

from tkinter import *
from threading import *
import datetime 
import winsound
from time import strftime
from tkinter import font
from tkinter import Label
from tkinter import messagebox as tkmsg
import time
from tkinter import ttk

window=Tk()
window.title('Set Alarm')
window.geometry('500x300')
    
def Threading():
    t1=Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm = f"{hrs.get()}:{mins.get()}:{secs.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time==set_alarm:
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            Info="It's "+set_alarm+"!\nThe Alarm is ringing!"
            Msg=tkmsg.askretrycancel('Alarm',Info)
            
hrsoption = ('00', '01', '02', '03', '04', '05', '06', '07',
             '08', '09', '10', '11', '12', '13', '14', '15',
             '16', '17', '18', '19', '20', '21', '22', '23', 
             '24')

minsoption = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')

secsoption = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')

hrs=StringVar()
mins=StringVar()
secs=StringVar()

greet1=Label(window,text="Alarm Clock",font=('Times New Roman', 30, 'bold'),fg="Black").place(x=150,y=10)
greet2=Label(window,text="Set Time",font=('Times New Roman', 30, 'bold'),fg="Black").place(x=180,y=70)

hrbtn=ttk.Combobox(window, value=hrsoption, width=5, font = ('Times New Roman', 20, 'bold'), textvariable=hrs).place(x=120,y=150)
hrs.set(hrsoption[0])

minbtn=ttk.Combobox(window,width=5,font = ('Times New Roman', 20, 'bold'), value=minsoption, textvariable=mins).place(x=220,y=150)
mins.set(minsoption[0])

secbtn=ttk.Combobox(window,width=5,font = ('Times New Roman', 20, 'bold'), value=secsoption, textvariable=secs).place(x=320,y=150)
secs.set(secsoption[0])

setbtn=Button(window,text="set alarm",command=Threading, bg="dark grey",fg="white",font = ('Times New Roman', 15, 'bold')).place(x=210,y=230)

window.mainloop()