import tkinter as tk
from Bonuslvl3 import PlaceholderEntry
import random
import time


nombre_hasard = random.randint(1,100)

temps = time.time()

tentatives = 5


class justprix():


    def justprixpy(self, event=None):

        global nombre_hasard, tentatives, temps

        proposition = self.entre.get()

        if proposition.isdigit():

            proposition = int(proposition)

            temps_passee = int(time.time() - temps)
            temps_passee = 60 - temps_passee

            self.temps.set(f"Temps: {temps_passee}s")
                
            if temps_passee <= 0:

                self.infovar.set("Votre dernière réponse ne sera donc pas pris en compte car le temps est écoulé.")
                self.window.destroy()

            if proposition < nombre_hasard:
                self.infovar.set("C'est plus")

            elif proposition > nombre_hasard:
                self.infovar.set("C'est moins")

            else:
                self.infovar.set("C'est gagné !")
                self.window.destroy()

            tentatives -= 1 
            self.tentativevar.set(f"{tentatives} Tentatives")
            if tentatives == 0:
                self.infovar.set("C'est perdu!")
                self.window.destroy()

        else:
            self.infovar.set("Tu dois entrer un nombre")


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Juste prix")
        self.window.minsize(600, 400)
        self.window.maxsize(600, 400)
        self.window.config(bg="#000")
        self.window.iconbitmap("justeprix/ressources/Logo_Juste_Prix_2015.ico")

        self.widget()

    def text(self):
        self.infovar = tk.StringVar()
        self.infovar.set("Bonne chance...")

        self.tentativevar = tk.StringVar()
        self.tentativevar.set("5 Tentatives")

        self.temps = tk.StringVar()
        self.temps.set("Temps: 60s")


        self.titre = tk.Label(self.window, text="Juste Prix", font=("Courrier",25), bg="#000", fg="#fff")
        self.titre.place(x= 230,y= 40)

        self.tentative = tk.Label(self.window, textvariable=self.tentativevar , font=("Courrier",10), bg="#000", fg="#fff")
        self.tentative.place(x= 510,y= 20)

        self.seconde = tk.Label(self.window, textvariable=self.temps, font=("Courrier",10), bg="#000", fg="#fff")
        self.seconde.place(x= 20,y= 20)

        self.reponse = tk.Label(self.window, textvariable=self.infovar, font=("Courrier", 15), bg="#000", fg="#fff")
        self.reponse.place(x= 240,y= 260)

            

    def entrer(self):
        self.entre = PlaceholderEntry(self.window, 'Entre ta proposition')
        self.entre.bind('<Return>', self.justprixpy)
        self.entre.focus()
        self.entre.place(x= 210,y= 200)

    def boutton(self):
        self.boutton = tk.Button(self.window, text='Valider', font=("Courrier", 10), bg='#555', fg='black', command=self.justprixpy)
        self.boutton.place(x= 360,y= 197)

    def widget(self):
        self.text()
        self.entrer()
        self.boutton()


w = justprix()
w.window.mainloop()