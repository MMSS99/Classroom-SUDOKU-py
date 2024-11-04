import pytest
from RECURSOS.comprobarSudoku import compSudoku
import CASOSTESTS.casosTestSudoku as casosTest

@pytest.mark.parametrize("casoSudoku, esCorrecto", 
                                [(casosTest.correcto, True),
                                (casosTest.filasIncorrectas, False),
                                (casosTest.columnasIncorrectas, False),
                                (casosTest.columnasFilasIncorrectas, False),
                                (casosTest.numerosFueraRango, False),
                                (casosTest.valorIncorrectoString, False),
                                (casosTest.valorIncorrectoFloat, False),
                                (casosTest.cuadradoIncorrectoFila, False),
                                (casosTest.cuadradoIncorrectoColumna, False),
                                (casosTest.inputVacio, False),
                                (casosTest.unaListaUnValor, False),
                                (casosTest.tipoDatoErroneo, False),
                                (casosTest.tipoDatoErroneo2, False),
                                (casosTest.unaListaUnValor, False)])

def test_SudokuCorrecto(casoSudoku, esCorrecto):
    assert compSudoku(casoSudoku) == esCorrecto