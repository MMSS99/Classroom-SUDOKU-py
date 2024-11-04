import pytest
from RECURSOS.sudokuEstandar import compEstandar
import CASOSTESTS.casosTestSudoku as casosTest

@pytest.mark.parametrize("casoSudoku, esCorrecto", 
                                [(casosTest.correcto, True),
                                (casosTest.filasIncorrectas, True),
                                (casosTest.columnasIncorrectas, True),
                                (casosTest.columnasFilasIncorrectas, True),
                                (casosTest.numerosFueraRango, True),
                                (casosTest.valorIncorrectoString, False),
                                (casosTest.valorIncorrectoFloat, False),
                                (casosTest.cuadradoIncorrectoFila, False),
                                (casosTest.cuadradoIncorrectoColumna, False),
                                (casosTest.inputVacio, False),
                                (casosTest.unaListaUnValor, False),
                                (casosTest.tipoDatoErroneo, False),
                                (casosTest.tipoDatoErroneo2, False),
                                (casosTest.unaListaUnValor, False)])

def test_comprobarDatos(casoSudoku, esCorrecto):
    assert compEstandar(casoSudoku) == esCorrecto