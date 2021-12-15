import csv
import tkinter as tk
from csv import writer


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

    def csvschreiben():
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
        dropdown1 = tk.OptionMenu(root, variable, *AnwendungsMenue)
        dropdown1.place(x=65, y=330)

        optionmenueauffüllen()

    def csvlesen():
        with open("Datenbank.csv", "r") as f:
            for line in f:
                array = line.split(';')
                if array[2] == format(variable.get()):
                    label4.configure(text=array[0])
                    label5.configure(text=array[1])
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
        dropdown1 = tk.OptionMenu(root, variable, *AnwendungsMenue)
        dropdown1.place(x=65, y=330)

    optionmenueauffüllen()

    root = tk.Tk()
    root.geometry('300x500')
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

        buttonJa = tk.Button(pop, background="red", activebackground="red", command=Löschen, text="Ja", height=1, width=5)
        buttonJa.place(x=55, y=60)

        buttonNein = tk.Button(pop, background="grey", activebackground="grey", command=löschenre, text="Nein", height=1, width=5)
        buttonNein.place(x=145, y=60)

    label = tk.Label(text="Benutzername: ", background="grey", activebackground="grey")
    label.place(x=65, y=30)

    benutzerentry = tk.Entry(background="grey")
    benutzerentry.place(x=65, y=60)

    label1 = tk.Label(text="Passwort: ",  background="grey", activebackground="grey")
    label1.place(x=65, y=100)

    passwortentry = tk.Entry(background="grey")
    passwortentry.place(x=65, y=130)

    button = tk.Button(command=csvschreiben, background="grey", activebackground="grey", text="Passwort erstellen ", width=20, height=1)
    button.place(x=65, y=230)

    label2 = tk.Label(text="Anwendung: ",  background="grey", activebackground="grey")
    label2.place(x=65, y=170)

    anwendungsentry = tk.Entry(background="grey")
    anwendungsentry.place(x=65, y=200)

    label3 = tk.Label(text="Anwendung: ",  background="grey", activebackground="grey")
    label3.place(x=65, y=300)

    variable = tk.StringVar()
    variable.set(AnwendungsMenue[0])
    dropdown = tk.OptionMenu(root, variable, *AnwendungsMenue)
    dropdown.place(x=65, y=330)

    button2 = tk.Button(background="grey", activebackground="grey", command=csvlesen, text="abfragen", width=7, height=1)
    button2.place(x=65, y=390)

    label4 = tk.Label(text="",  background="grey", activebackground="grey")
    label4.place(x=65, y=430)

    label5 = tk.Label(text="",  background="grey", activebackground="grey")
    label5.place(x=65, y=460)

    button3 = tk.Button(background="grey", activebackground="grey", command=abfragefenster, text="löschen", width=7, height=1)
    button3.place(x=150, y=390)

    root.mainloop()
