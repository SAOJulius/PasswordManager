import tkinter as tk
from csv import writer


def hauptfenster():
    AnwendungsMenue = []

    def optionmenueauffüllen():
        AnwendungsMenue.clear()
        try:
            with open("Datenbank.csv", "r") as file:

                for line in file:
                    array = line.split(',')
                    AnwendungsMenue.append(array[2])
                dropdown.place(x=65, y=330)
        except:
            pass

    def csvschreiben():
        list = [benutzerentry.get(), passwortentry.get(), anwendungsentry.get()]
        with open("Datenbank.csv", "a", newline="") as f:
            writer(f).writerow(list)
            benutzerentry.delete(0, "end")
            passwortentry.delete(0, "end")
            anwendungsentry.delete(0, "end")

    def csvlesen():
        with open("Datenbank.csv", "r") as f:

            for line in f:
                array = line.split(',')
                if str(array[2]) == format(variable.get()):
                    label4.configure(text=array[0])
                    label5.configure(text=array[0])
                else:
                    pass

    def datensatzlöschen():
        with open("Datenbank.csv", "r") as file:
            for line in file:
                array = line.split(',')
                if array[2] == format(variable.get()):
                    abfragefenster()

                else:
                    pass

    def löschenre():
        pop.destroy()

    def Löschen():
        with open("Datenbank.csv", "w") as file:
            for line in file:
                array = line.split(',')
                if array[2] == format(variable.get()):
                    try:
                        writer(file).writerow("")
                        optionmenueauffüllen()
                    except:
                        pass

                else:
                    pass

    optionmenueauffüllen()

    root = tk.Tk()
    root.geometry('300x500')
    root.title("Passwort Manager")

    def abfragefenster():
        global pop
        pop = tk.Toplevel(root)
        pop.geometry('250x130')
        pop.title("Achtung")

        labelfrage = tk.Label(pop, text="Wirklich löschen? ")
        labelfrage.place(x=70, y=20)

        buttonJa = tk.Button(pop, command=Löschen, text="Ja", height=1, width=5)
        buttonJa.place(x=55, y=60)

        buttonNein = tk.Button(pop, command=löschenre, text="Nein", height=1, width=5)
        buttonNein.place(x=145, y=60)


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

    variable = tk.StringVar()
    variable.set(AnwendungsMenue[0])
    dropdown = tk.OptionMenu(root, variable, *AnwendungsMenue)
    dropdown.place(x=65, y=330)

    button2 = tk.Button(command=csvlesen, text="abfragen", width=7, height=1)
    button2.place(x=65, y=390)

    label4 = tk.Label(text="")
    label4.place(x=65, y=430)

    label5 = tk.Label(text="")
    label5.place(x=65, y=460)

    button3 = tk.Button(command=abfragefenster, text="löschen", width=7, height=1)
    button3.place(x=150, y=390)

    root.mainloop()

