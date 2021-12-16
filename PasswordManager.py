import hashlib
import time
import tkinter as tk

from mainWindow import hauptfenster
from verschlüsseln import encrypt, get_key, decrypt


def buttonclick():
    schlüssel = passwort.get()
    message = hashlib.sha256()
    message.update(bytes(schlüssel, 'utf-8'))

    if schlüssel == "":
        pass
    elif str(
            nutzername.get()) == "Anja Krams" and message.hexdigest() == "16163d72e046beff5cc61be81f22a57aafe0bd8f773ed9fcbf0f6fb0fed4770f":
        try:
            decrypt(get_key(passwort.get()), "encrypted-Datenbank.csv")
        except:
            pass
        mainwindow.destroy()
        hauptfenster()
        try:
            encrypt(get_key(schlüssel), "Datenbank.csv")
        except:
            pass

        with open("Datenbank.csv", "w") as f:
            f.write("")
    else:
        with open("Datenbank.csv", "w") as f:
            f.write("")
        time.sleep(3)


mainwindow = tk.Tk()
mainwindow.geometry('290x220')
mainwindow.title("Login Fenster")
mainwindow['background'] = 'grey'

label = tk.Label(text="Benutzername: ", background="grey", activebackground="grey")
label.place(x=65, y=30)

nutzername = tk.Entry(background="grey")
nutzername.place(x=65, y=60)

label1 = tk.Label(text="Passwort: ", background="grey", activebackground="grey")
label1.place(x=65, y=110)

passwort = tk.Entry(background="grey")
passwort.place(x=65, y=140)

button = tk.Button(background="grey", activebackground="grey", command=buttonclick, text="Login ", width=10)
button.place(x=100, y=170)

mainwindow.mainloop()
