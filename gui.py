import tkinter as tk
from tkinter import Canvas
from threading import Thread
from traffic import TrafficLight  # Importation de la classe TrafficLight

class TrafficLightGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Feu Tricolore")

        # Initialisation de l'objet TrafficLight
        self.traffic_light = TrafficLight()

        # Création du canevas pour dessiner les cercles
        self.canvas = Canvas(root, width=200, height=500)
        self.canvas.pack(pady=20)

        # Création des cercles pour chaque état du feu
        self.red_circle = self.canvas.create_oval(50, 50, 150, 150, fill="gray")
        self.yellow_circle = self.canvas.create_oval(50, 175, 150, 275, fill="gray")
        self.green_circle = self.canvas.create_oval(50, 300, 150, 400, fill="gray")

        # Bouton pour démarrer le feu tricolore
        self.start_button = tk.Button(root, text="Démarrer le Feu", font=("Helvetica", 14), command=self.run_traffic_light)
        self.start_button.pack(pady=20)

    def update_lights(self):
        """
        Met à jour les couleurs des cercles en fonction de l'état actuel du feu.
        """
        # Récupérer l'état actuel du feu et changer la couleur du cercle correspondant
        state = self.traffic_light.get_state()

        if state == "Rouge":
            self.canvas.itemconfig(self.red_circle, fill="red")
            self.canvas.itemconfig(self.yellow_circle, fill="gray")
            self.canvas.itemconfig(self.green_circle, fill="gray")
        elif state == "Jaune":
            self.canvas.itemconfig(self.red_circle, fill="gray")
            self.canvas.itemconfig(self.yellow_circle, fill="yellow")
            self.canvas.itemconfig(self.green_circle, fill="gray")
        elif state == "Vert":
            self.canvas.itemconfig(self.red_circle, fill="gray")
            self.canvas.itemconfig(self.yellow_circle, fill="gray")
            self.canvas.itemconfig(self.green_circle, fill="green")

    def run_traffic_light(self):
        """
        Lance le cycle du feu tricolore dans un thread séparé pour ne pas bloquer l'interface.
        """
        # Créer un thread pour que l'interface ne se bloque pas pendant que le feu tourne
        thread = Thread(target=self.traffic_light.run)
        thread.daemon = True  # Pour que le thread se termine lorsque le programme principal termine
        thread.start()

        # Mise à jour régulière de l'interface pour refléter les changements d'état
        self.update_gui()

    def update_gui(self):
        """
        Met à jour l'interface en boucle pour afficher l'état actuel du feu.
        """
        self.update_lights()  # Actualiser l'état
        self.root.after(1000, self.update_gui)  # Relancer la mise à jour de l'interface après 1 seconde

# Point d'entrée du programme
if __name__ == "__main__":
    root = tk.Tk()
    gui = TrafficLightGUI(root)
    root.mainloop()
