import pytest
from RECURSOS.lineaCorrecta import compLineas
import CASOSTESTS.casosTestSudoku as casosTest

@pytest.mark.parametrize("casoSudoku, esCorrecto", 
                                [(casosTest.correcto, True),
                                (casosTest.filasIncorrectas, False),
                                (casosTest.columnasIncorrectas, True),
                                (casosTest.columnasFilasIncorrectas, False),
                                (casosTest.numerosFueraRango, True),
                                (casosTest.valorIncorrectoString, False),
                                (casosTest.valorIncorrectoFloat, False),
                                (casosTest.cuadradoIncorrectoFila, False),
                                (casosTest.cuadradoIncorrectoColumna, False),
                                (casosTest.inputVacio, False),
                                (casosTest.unaListaUnValor, False)])

def test_comprobarLineas(casoSudoku, esCorrecto):
    assert compLineas(casoSudoku) == esCorrecto