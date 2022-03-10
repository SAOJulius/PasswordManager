import csv
import tkinter as tk
from csv import writer

import pyperclip as pc

print("testststs")
def hauptfenster():
    AnwendungsMenue = []

    def optionmenueauffüllen():
        AnwendungsMenue.clear()
        try:
            with open("Datenbank.csv", "r") as file:
                for line in file:
                    array = line.split(';')
                    AnwendungsMenue.append(array[2])
        except:
            pass

    copy1 = []
    copy3 = []

    def csvlesen(choice):
        choice = variable.get()

        with open("Datenbank.csv", "r") as f:
            for line in f:
                array = line.split(';')
                if array[2] == format(variable.get()):
                    label4.configure(text=array[0])
                    label5.configure(text=array[1])
                    copy1.clear()
                    copy3.clear()
                    copy1.append(array[0])
                    copy3.append(array[1])

                else:
                    pass

    def datensatzlöschen():
        with open("Datenbank.csv", "r", newline="") as file:

            for line in file:
                array = line.split(';')
                if array[2] == format(variable.get()):
                    abfragefenster()

                else:
                    pass

    def löschenre():
        pop.destroy()

    def Löschen():
        lines = list()
        with open('Datenbank.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            for line in reader:
                x = 0
                for word in line:
                    if str(word) == format(variable.get()).rstrip():
                        x = x + 1
                    else:
                        pass

                if x == 0:
                    lines.append(line)
                else:
                    pass

        with open("Datenbank.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            file.write("")
            for array in lines:
                writer.writerow(array)

        pop.destroy()
        try:
            dropdown.destroy()
        except:
            pass
        optionmenueauffüllen()
        dropdown1 = tk.OptionMenu(root, variable, *AnwendungsMenue, command=csvlesen)
        dropdown1.place(x=100, y=20)

    optionmenueauffüllen()

    def copy():

        pc.copy(copy1[0])

    def copy2():
        pc.copy(copy3[0])

    def neuesPasswort():

        def csvschreiben():
            global csvschreiben
            list = [benutzerentry.get(), passwortentry.get(), anwendungsentry.get()]
            with open("Datenbank.csv", "a", newline="") as f:
                writer(f, delimiter=";").writerow(list)
                benutzerentry.delete(0, "end")
                passwortentry.delete(0, "end")
                anwendungsentry.delete(0, "end")
            try:
                dropdown.destroy()
            except:
                pass
            optionmenueauffüllen()
            dropdown1 = tk.OptionMenu(root, variable, *AnwendungsMenue, command=csvlesen)
            dropdown1.place(x=100, y=20)
            optionmenueauffüllen()

        global pop2
        pop2 = tk.Toplevel(root)
        pop2.geometry('290x300')
        pop2.title("Achtung")
        pop2['background'] = 'grey'

        label = tk.Label(pop2, text="Benutzername: ", background="grey", activebackground="grey")
        label.place(x=65, y=30)

        benutzerentry = tk.Entry(pop2, background="grey")
        benutzerentry.place(x=65, y=60)

        label1 = tk.Label(pop2, text="Passwort: ", background="grey", activebackground="grey")
        label1.place(x=65, y=100)

        passwortentry = tk.Entry(pop2, background="grey")
        passwortentry.place(x=65, y=130)

        label2 = tk.Label(pop2, text="Anwendung: ", background="grey", activebackground="grey")
        label2.place(x=65, y=160)

        anwendungsentry = tk.Entry(pop2, background="grey")
        anwendungsentry.place(x=65, y=190)

        button = tk.Button(pop2, command=csvschreiben, background="grey", activebackground="grey",
                           text="Passwort erstellen ", width=20, height=1)
        button.place(x=65, y=230)

    global root
    root = tk.Tk()
    root.geometry('282x235')
    root.title("Passwort Manager")
    root['background'] = 'grey'

    def abfragefenster():
        global pop
        pop = tk.Toplevel(root)
        pop.geometry('250x130')
        pop.title("Achtung")
        pop['background'] = 'grey'

        labelfrage = tk.Label(pop, background="grey", activebackground="grey", text="Wirklich löschen? ")
        labelfrage.place(x=70, y=20)

        buttonJa = tk.Button(pop, background="red", activebackground="red", command=Löschen, text="Ja", height=1,
                             width=5)
        buttonJa.place(x=55, y=60)

        buttonNein = tk.Button(pop, background="grey", activebackground="grey", command=löschenre, text="Nein",
                               height=1, width=5)
        buttonNein.place(x=145, y=60)

    variable = tk.StringVar()
    variable.set(AnwendungsMenue[0])
    dropdown = tk.OptionMenu(root, variable, *AnwendungsMenue, command=csvlesen)
    dropdown.place(x=100, y=20)

    button2 = tk.Button(background="grey", activebackground="grey", command=neuesPasswort, text="Neu ", width=7,
                        height=1)
    button2.place(x=65, y=90)

    label4 = tk.Label(text="", background="grey", activebackground="grey")
    label4.place(x=65, y=130)

    label5 = tk.Label(text="", background="grey", activebackground="grey")
    label5.place(x=65, y=170)

    button3 = tk.Button(background="grey", activebackground="grey", command=abfragefenster, text="Löschen", width=7,
                        height=1)
    button3.place(x=150, y=90)

    button4 = tk.Button(background="grey", activebackground="grey", command=copy, text="Copy", width=7, height=1)
    button4.place(x=150, y=130)

    button5 = tk.Button(background="grey", activebackground="grey", command=copy2, text="Copy", width=7, height=1)
    button5.place(x=150, y=170)

    root.mainloop()
