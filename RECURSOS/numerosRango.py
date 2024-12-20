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

    for linea in matrix:
        for numerin in linea:
            if numerin > len(matrix):
                return False
    return True

if __name__ == '__main__':
    import CASOSTESTS.casosTestSudoku as casosTest

    for caso in casosTest.__dict__:
        if not caso.startswith('__'):

            print ([casosTest.__dict__[caso]] + [", ¿Los números del sudoku están dentro de su rango? = "] + [compNumeros(casosTest.__dict__[caso])])

