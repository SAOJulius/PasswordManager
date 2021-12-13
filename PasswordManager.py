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
    elif str(nutzername.get()) == "Anja Krams" and message.hexdigest() == "16163d72e046beff5cc61be81f22a57aafe0bd8f773ed9fcbf0f6fb0fed4770f":

        try:
            decrypt(get_key(passwort.get()), "encrypted-Datenbank.csv")
        except:
            pass

        loginWindow.destroy()
        hauptfenster()
        encrypt(get_key(schlüssel), "Datenbank.csv")


        with open("Datenbank.csv", "w") as f:
            f.write("")
    else:
        with open("Datenbank.csv", "w") as f:
            f.write("")
        time.sleep(3)


loginWindow = tk.Tk()
loginWindow.geometry('290x250')
loginWindow.title("Login Fenster")

label = tk.Label(text="Benutzername: ")
label.place(x=100, y=60)

nutzername = tk.Entry()
nutzername.place(x=65, y=90)

label1 = tk.Label(text="Passwort: ")
label1.place(x=100, y=140)

passwort = tk.Entry()
passwort.place(x=65, y=170)

button = tk.Button(command=buttonclick, text="Login ", width=10, height=1)
button.place(x=100, y=200)

loginWindow.mainloop()
