import time

class TrafficLight:
    def __init__(self):
        self.state = "Rouge"  # L'état initial est rouge

    def change_to_green(self):
        """
        Passe l'état du feu au vert (10 secondes).
        """
        self.state = "Vert"
        print("La lumière est verte. Passez !")
        time.sleep(10)  # Durée du vert est de 10 secondes

    def change_to_yellow(self):
        """
        Passe l'état du feu au jaune (2 secondes).
        """
        self.state = "Jaune"
        print("La lumière est jaune. Ralentissez !")
        time.sleep(2)  # Durée du jaune est de 2 secondes

    def change_to_red(self):
        """
        Passe l'état du feu au rouge (15 secondes).
        """
        self.state = "Rouge"
        print("La lumière est rouge. Arrêtez !")
        time.sleep(15)  # Durée du rouge est de 15 secondes

    def get_state(self):
        """
        Retourne l'état actuel du feu.
        """
        return self.state

    def run(self):
        """
        Démarre le cycle du feu tricolore : 
        Rouge -> Vert -> Jaune -> Rouge, en respectant les durées définies.
        """
        while True:
            self.change_to_red()     # Commence par le rouge
            self.change_to_green()   # Puis passe au vert
            self.change_to_yellow()  # Ensuite passe au jaune

# Point d'entrée du programme
if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.run()
