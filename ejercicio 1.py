import copy

# esta funcion es la que realiza el calculo de la cantidad de minas adyacentes


def count_mines(board, row, col):
    # defino los desplazamientos para las 8 direcciones alrededor de una celda
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    count = 0

    for dr, dc in directions:
        # a la fila le resto o le sumo la direccion (dr: directionRow)
        r = row + dr
        # a la columna le resto o le sumo la direccion (dc: directionColumn)
        c = col + dc

        if (0 <= r and 0 <= c):
            if (r < len(board) and c < len(board[r])):
                count += board[r][c]

    return count

# esta funcion cambia los 1 (minas) por 9 y los 0 por el numero de cantidad de minas totales.


def minesweeper(board):
    # creo un tablero "resultado" copiando el array original
    result = copy.deepcopy(board)

    for r in range(len(result)):
        for c in range(len(result[r])):
            # si es 1 cambio a 9
            if board[r][c] == 1:
                result[r][c] = 9
            # si no, calculo la cantidad de minas que tiene al rededor
            else:
                result[r][c] = count_mines(board, r, c)

    return result


# Ejemplo de uso (acepta otras formas de tableros)
input_board = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]
output_board = minesweeper(input_board)

for row in output_board:
    print(row)
