import pytest
from RECURSOS.comprobarSudoku import compSudoku
import CASOSTESTS.casosTestSudoku as casosTest

@pytest.mark.parametrize("casoSudoku, esCorrecto", 
                                [(casosTest.correcto, True),
                                (casosTest.incorrect, False),
                                (casosTest.incorrect1, False),
                                (casosTest.incorrect2, False),
                                (casosTest.incorrect3, False),
                                (casosTest.incorrect4, False),
                                (casosTest.incorrect5, False),
                                (casosTest.irregular, False),
                                (casosTest.irregular2, False),
                                (casosTest.nuevo, False),
                                (casosTest.__oculto, False)])

def test_SudokuCorrecto(casoSudoku, esCorrecto):
    assert compSudoku(casoSudoku) == esCorrecto