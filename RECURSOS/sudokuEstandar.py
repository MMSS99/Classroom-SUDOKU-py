#Comprobamos que el sudoku no tenga una lista en su interior que rompa su forma de cuadrado excediendo en carácteres el número de listas en la matriz.

def compEstandar(matrix):

    if isinstance(matrix, list) == False:
        return False
    
    if not matrix or len(matrix) < 2:
        return False
    
    for i in (matrix):
        if len(i) != len(matrix):
            return False
        for j in range(len(i)):
            if isinstance(i[j], int) == False:
                return False
            if i[j] < 1:
                return False
    return True

if __name__ == '__main__':
    import sys
    sys.path.append('..')
    import CASOSTESTS.casosTestSudoku as casosTest

    for caso in casosTest.__dict__:
        if not caso.startswith('__'):

            print ([casosTest.__dict__[caso]] + [", ¿Tiene el sudoku una forma estandarizada n*n? = "] + [compEstandar(casosTest.__dict__[caso])])