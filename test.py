from main import Rover

def test_informa_posicion_y_orientacion_iniciales():
    assert Rover().posicion_y_orientacion_iniciales() == ((0, 0), "N")

def test_rover_gira():
    assert Rover().rotar_orientacion("L") == "W"
    assert Rover().rotar_orientacion("R") == "E"

def test_rover_avanza():
    rover = Rover()
    assert rover.avanzar() == (0, 1)
    assert rover.avanzar() == (0, 2)
    assert rover.avanzar() == (0, 3)

    rover2 = Rover(posicion=(1, 1), orientacion="E")
    assert rover2.avanzar() == (2, 1)
    assert rover2.avanzar() == (3, 1)
    assert rover2.avanzar() == (4, 1)