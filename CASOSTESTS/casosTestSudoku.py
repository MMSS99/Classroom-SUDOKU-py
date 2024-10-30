correcto = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

filasIncorrectas = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 2]]

columnasIncorrectas = [[1, 2, 3],
              [2, 3, 1],
              [2, 3, 1]]

columnasFilasIncorrectas = [[1, 2, 3, 4],
              [2, 3, 1, 2],
              [4, 1, 2, 3],
              [2, 3, 1, 4]]

numerosFueraRango = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

valorIncorrectoString = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

valorIncorrectoFloat = [[1, 1.5],
              [1.5, 1]]

cuadradoIncorrectoFila = [[1, 2, 3],
             [2, 3, 1]]

cuadradoIncorrectoColumna = [[1, 2, 3],
              [2, 3, 1],
              [3, 1]]
inputVacio = [[]]

# Para evitar importar una variable al usar:
# from modulo import *
# se emplea __nombreVariable
# En nuestro caso utilizo import as
# porque necesito noombrar el espacio de nombres
# que define de este modulo
# por lo que no puedo usar *
# Este caso test no pasa el filtro
# attr.startswith('__') el el main

unaListaUnValor = [[1]]