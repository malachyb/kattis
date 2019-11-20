def switch_quad(x, y):
    quads = {
        (0, 0): 1,
        (1, 0): 2,
        (1, 1): 3,
        (0, 1): 4
    }
    return quads[x < 0, y < 0]


print(switch_quad(int(input()), int(input())))
