#Comprobamos que el sudoku no tenga una lista en su interior que rompa su forma de cuadrado excediendo en carácteres el número de listas en la matriz.

def compEstandar(matrix):
    if not matrix or len(matrix) < 2:
        return False
    
    for i in (matrix):
        if len(i) != len(matrix):
            return False
        for j in range(len(i)):
            check = isinstance(i[j], int)
            if check == False:
                return False
    return True

if __name__ == '__main__':
    import sys
    sys.path.append('..')
    import TESTS.casosTestSudoku as casosTest

    for caso in casosTest.__dict__:
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Tiene el sudoku una forma estandarizada n*n? = "] + [compEstandar(casosTest.__dict__[caso])])