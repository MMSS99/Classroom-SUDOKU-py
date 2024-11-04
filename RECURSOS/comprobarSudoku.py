#https://github.com/dfleta/sudokuModules/blob/main

# Requires a PYTHONPATH and __init__ (709 librorata) on /RECURSOS/ to initialize????

import sys
sys.path.append('..')
from RECURSOS.columnaCorrecta import compColumnas
from RECURSOS.lineaCorrecta import compLineas
from RECURSOS.numerosRango import compNumeros

def compSudoku(matrix):
    if compColumnas(matrix) and compLineas(matrix) and compNumeros(matrix):
        return True
    else:
        return False
    
if __name__ == '__main__':
    import CASOSTESTS.casosTestSudoku as casosTest

    for caso in casosTest.__dict__:
        if not caso.startswith('__'):

            print ([casosTest.__dict__[caso]] + [", ¿Es un sudoku correcto? = "] + [compSudoku(casosTest.__dict__[caso])])

