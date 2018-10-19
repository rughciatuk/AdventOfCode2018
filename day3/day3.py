
def create_matrix(number):
    # (x, y)
    matrix = {}
    matrix[1] = [0, 0]
    top = 0
    for num in range(2, number + 1):
        cord = (matrix[num - 1])[:]

        # Create a new layer of the square, y is the same and x is bigger by one
        if (cord[0] == top and cord[1] == -top):
            top += 1
            cord[0] = top
        elif (cord[0] == top and cord[1] < top):  # Need to move up
            cord[1] += 1
        elif (cord[0] > -top and cord[1] == top):  # Need to move left
            cord[0] -= 1
        elif (cord[0] == -top and cord[1] > -top):  # Need to move down
            cord[1] -= 1
        elif(cord[0] < top and cord[1] == -top):  # Need to move right
            cord[0] += 1

        matrix[num] = cord

    return matrix


def create_matrix_sum(number):
    # (x, y)
    matrix = {}
    matrix[(0, 0)] = 1
    top = 0
    old_cord = (0, 0)

    while(matrix[old_cord] < number):
        new_cord = tuple()
        if (old_cord[0] == top and old_cord[1] == -top):
            top += 1
            new_cord = (top, old_cord[1])
        elif (old_cord[0] == top and old_cord[1] < top):  # Need to move up
            new_cord = (old_cord[0], old_cord[1] + 1)
        elif (old_cord[0] > -top and old_cord[1] == top):  # Need to move left
            new_cord = (old_cord[0] - 1, old_cord[1])
        elif (old_cord[0] == -top and old_cord[1] > -top):  # Need to move down
            new_cord = (old_cord[0], old_cord[1] - 1)
        elif(old_cord[0] < top and old_cord[1] == -top):  # Need to move right
            new_cord = (old_cord[0] + 1, old_cord[1])

        sum = 0
        checking = [
            (new_cord[0] + 1, new_cord[1]),
            (new_cord[0] + 1, new_cord[1] + 1),
            (new_cord[0], new_cord[1] + 1),
            (new_cord[0] - 1, new_cord[1] + 1),
            (new_cord[0] - 1, new_cord[1]),
            (new_cord[0] - 1, new_cord[1] - 1),
            (new_cord[0], new_cord[1] - 1),
            (new_cord[0] + 1, new_cord[1] - 1)
        ]
        for pos in checking:
            if pos in matrix:
                sum += matrix[pos]
        matrix[new_cord] = sum
        old_cord = new_cord

    return matrix


print(create_matrix_sum(277678))
