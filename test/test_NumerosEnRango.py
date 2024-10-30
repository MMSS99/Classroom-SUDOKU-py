import pytest
from RECURSOS.numerosRango import compNumeros
import CASOSTESTS.casosTestSudoku as casosTest

@pytest.mark.parametrize("casoSudoku, esCorrecto", 
                                [(casosTest.correcto, True),
                                (casosTest.filasIncorrectas, True),
                                (casosTest.columnasIncorrectas, True),
                                (casosTest.columnasFilasIncorrectas, True),
                                (casosTest.numerosFueraRango, False),
                                (casosTest.valorIncorrectoString, False),
                                (casosTest.valorIncorrectoFloat, False),
                                (casosTest.cuadradoIncorrectoFila, False),
                                (casosTest.cuadradoIncorrectoColumna, False),
                                (casosTest.inputVacio, False),
                                (casosTest.unaListaUnValor, False)])

def test_comprobarDatos(casoSudoku, esCorrecto):
    assert compNumeros(casoSudoku) == esCorrecto