#https://github.com/dfleta/sudokuModules/blob/main

# Requires a PYTHONPATH and __init__ (709 librorata) on /RECURSOS/ to initialize????
    
if __name__ == '__main__':
    import TESTS.casosTestSudoku as casosTest
    from RECURSOS.comprobarSudoku import compSudoku

    for caso in casosTest.__dict__:
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Es un sudoku correcto? = "] + [compSudoku(casosTest.__dict__[caso])])

