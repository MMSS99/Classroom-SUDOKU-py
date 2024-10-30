import pytest
from RECURSOS.columnaCorrecta import compColumnas
import CASOSTESTS.casosTestSudoku as casosTest

@pytest.mark.parametrize("casoSudoku, esCorrecto", 
                                [(casosTest.correcto, True),
                                (casosTest.filasIncorrectas, False),
                                (casosTest.columnasIncorrectas, False),
                                (casosTest.columnasFilasIncorrectas, False),
                                (casosTest.numerosFueraRango, True),
                                (casosTest.valorIncorrectoString, False),
                                (casosTest.valorIncorrectoFloat, False),
                                (casosTest.cuadradoIncorrectoFila, False),
                                (casosTest.cuadradoIncorrectoColumna, False),
                                (casosTest.inputVacio, False),
                                (casosTest.unaListaUnValor, False)])

def test_comprobarDatos(casoSudoku, esCorrecto):
    assert compColumnas(casoSudoku) == esCorrecto