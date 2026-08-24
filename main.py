class Rover:
    def __init__(self, posicion=(0, 0), orientacion="N"):
        self.posicion = posicion
        self.orientacion = orientacion

    def posicion_y_orientacion_iniciales(self):
        return (self.posicion, self.orientacion)