import tkinter as tk
from csv import writer
from tkinter import *




def hauptfenster():
    AnwendungsMenü = []

    def arrayfüllen():

        AnwendungsMenü.clear()
        try:
            with open("Datenbank.csv", "r") as file:

                for line in file:
                    array = line.split(',')
                    AnwendungsMenü.append(array[2])
        except:
            pass

    arrayfüllen()


    def csvschreiben():
        list = [benutzerentry.get(), passwortentry.get(), anwendungsentry.get()]
        with open("Datenbank.csv", "a", newline="") as f:
            writer(f).writerow(list)
            arrayfüllen()


    def csvlesen():

        with open("Datenbank.csv", "r") as f:

            for line in f:
                array = line.split(',')
                if str(array[2]) == format(variable.get()):
                    label4.configure(text=array[0])
                    label5.configure(text=array[0])
                else:
                    pass


    mainwindow = tk.Tk()
    mainwindow.geometry('300x800')
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

    variable = tk.StringVar(mainwindow)
    variable.set(AnwendungsMenü[0])
    dropdown = tk.OptionMenu(mainwindow, variable, *AnwendungsMenü)
    dropdown.place(x=65, y=330)


    button2 = tk.Button(command=csvlesen, text="Passwort abfragen", width=20, height=1)
    button2.place(x=65, y=390)

    label4 = tk.Label(text="")
    label4.place(x=65, y=430)

    label5 = tk.Label(text="")
    label5.place(x=65, y=460)





    mainwindow.mainloop()
