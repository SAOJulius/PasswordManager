import tkinter as tk
from csv import writer
from tkinter import *

def hauptfenster():

    def csvschreiben():
        list = [benutzerentry.get(), passwortentry.get(), anwendungsentry.get()]
        with open("Datenbank.csv", "a", newline="") as f:
            writer(f).writerow(list)

    def csvlesen():

        with open("Datenbank.csv", "r") as f:
            lines = f.readlines()
            for x in lines:
                result = []
                result = x.split(',')[2]
                if str(entry.get() + "\n") == str(result):
                    label4.delete("1.0", "end")
                    label5.delete("1.0", "end")
                    label4.insert(1.0, x.split(',')[0])
                    label5.insert(1.0, x.split(',')[1])
                    break
                else:
                    pass

    mainwindow = tk.Tk()
    mainwindow.geometry('300x500')
    mainwindow.title("Passwort Manager")

    label = tk.Label(text="Benutzername: ")
    label.place(x=65, y=30)

    benutzerentry = tk.Entry()
    benutzerentry.place(x=65, y=60)

    label1 = tk.Label(text="Passwort: ")
    label1.place(x=65, y=100)

    passwortentry = tk.Entry()
    passwortentry.place(x=65, y=130)

    button = tk.Button(command=csvschreiben, text="Passwort erstellen ", width=20, height=1)
    button.place(x=65, y=230)

    label2 = tk.Label(text="Anwendung: ")
    label2.place(x=65, y=170)

    anwendungsentry = tk.Entry()
    anwendungsentry.place(x=65, y=200)

    label3 = tk.Label(text="Anwendung: ")
    label3.place(x=65, y=300)

    entry = tk.Entry()
    entry.place(x=65, y=330)

    button2 = tk.Button(command=csvlesen, text="Passwort abfragen", width=20, height=1)
    button2.place(x=65, y=360)

    label4 = Text(mainwindow, height=1, width=20, borderwidth=0)
    label4.place(x=65, y=400)

    label5 = Text(mainwindow, height=1, width=20, borderwidth=0)
    label5.place(x=65, y=430)

    mainwindow.mainloop()
