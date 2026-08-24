from main import Rover

def test_informa_posicion_y_orientacion_iniciales():
    assert posicion_y_orientacion_iniciales() == ((0, 0), "N")