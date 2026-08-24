class Rover:
    def __init__(self, posicion=(0, 0), orientacion="N"):
        self.posicion = posicion
        self.orientacion = orientacion

    def posicion_y_orientacion_iniciales(self):
        return (self.posicion, self.orientacion)

    def rotar_orientacion(self, giro):
       
        if self.orientacion == "N" and giro == "L":
            self.orientacion = "W"
        elif self.orientacion == "N" and giro == "R":
            self.orientacion = "E"
        elif self.orientacion == "E" and giro == "L":
            self.orientacion = "N"
        elif self.orientacion == "E" and giro == "R":
            self.orientacion = "N"
        elif self.orientacion == "W" and giro == "L":
                self.orientacion = "S"
        elif self.orientacion == "W" and giro == "R":
                self.orientacion = "N"
        elif self.orientacion == "S" and giro == "L":
                self.orientacion = "W"
        elif self.orientacion == "S" and giro == "R":
                self.orientacion = "E"
        
        return self.orientacion

    def avanzar(self):
        if self.orientacion == "N":
            self.posicion = (self.posicion[0], self.posicion[1] + 1)
        elif self.orientacion == "E":
            self.posicion = (self.posicion[0] + 1, self.posicion[1])
        elif self.orientacion == "S":
            self.posicion = (self.posicion[0], self.posicion[1] - 1)
        elif self.orientacion == "W":
            self.posicion = (self.posicion[0] - 1, self.posicion[1])
        return self.posicion

    def retroceder(self):
        return 0