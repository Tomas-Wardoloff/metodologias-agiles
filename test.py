from main import Rover

def test_informa_posicion_y_orientacion_iniciales():
    assert Rover().posicion_y_orientacion_iniciales() == ((0, 0), "N")

def test_rover_gira():
    assert Rover().rotar_orientacion() == "W"