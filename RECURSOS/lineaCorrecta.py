# Pasamos por todos los elementos de la lista y contamos que aparezcan una sola vez.
#if __name__ == '__main__':
#    from sudokuEstandar import compEstandar
#else:
#    from .sudokuEstandar import compEstandar
import sys
sys.path.append('..')
from RECURSOS.sudokuEstandar import compEstandar

def compLineas(matrix):
    if compEstandar(matrix) == False:
        return False
    
    for i in matrix:
        for j in i:
            if i.count(j) != 1:
                return False
    return True
            
if __name__ == '__main__':
    import CASOSTESTS.casosTestSudoku as casosTest

    for caso in casosTest.__dict__:
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Son las líneas del sudoku correctas? = "] + [compLineas(casosTest.__dict__[caso])])