# 
#if __name__ == '__main__':
#    from sudokuEstandar import compEstandar
#else:
#    from .sudokuEstandar import compEstandar
import sys
sys.path.append('..')
from RECURSOS.sudokuEstandar import compEstandar

def compNumeros(matrix):
    if compEstandar(matrix) == False:
        return False

    for i in matrix:
        for j in i:
            if j > len(matrix):
                return False
    return True

if __name__ == '__main__':
    import TESTS.casosTestSudoku as casosTest

    for caso in casosTest.__dict__:
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Los números del sudoku están dentro de su rango? = "] + [compNumeros(casosTest.__dict__[caso])])

