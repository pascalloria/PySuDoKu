# sudoku
# taille : 9*9
# Pas plusieur fois le meme nombre dans une ligne,
# colonne
# dans un mini carré

import random

HEIGHT = 9
WIDTH = 9


numbers = range(1, WIDTH + 1)


def generate_number():
    numbers_free = [x for x in numbers]
    return numbers_free


def search_remove(x, list):
    if x in list:
        list.remove(x)


def substract_list_in_list(list1, list2):
    for e in list1:
        search_remove(e, list2)


def random_append(list1, list2):
    x = random.choice(list1)
    list2.append(x)
    return x


def generate_grid():
    grid = []
    for i in range(HEIGHT):
        # generate row with no duplicates HEIGHT time
        grid.append(random.sample(numbers, WIDTH))
    """========== TOP===================="""
    # 1 er carré
    numbers_free = generate_number()
    for e in grid[0][0:3]:
        search_remove(e, numbers_free)
    for j in range(1, 3):
        for i in range(0, 3):
            grid[j][i] = random.choice(numbers_free)
            numbers_free.remove(grid[j][i])

    # 2eme carré
    numbers_free = generate_number()
    for e in grid[0][3:6]:
        search_remove(e, numbers_free)
    for e in grid[1][:3]:
        search_remove(e, numbers_free)
    for i in range(3, 6):
        grid[1][i] = random.choice(numbers_free)
        numbers_free.remove(grid[1][i])
    for e in grid[1][:3]:
        if e not in numbers_free:
            if e not in grid[0][3:6]:
                numbers_free.append(e)
    for i in range(3, 6):
        grid[2][i] = random.choice(numbers_free)
        numbers_free.remove(grid[2][i])

    # 3eme carrée
    numbers_free = generate_number()
    for e in grid[0][6:9]:
        search_remove(e, numbers_free)
    for e in grid[1][:6]:
        search_remove(e, numbers_free)
    if len(numbers_free) == 3:
        for i in range(6, 9):
            grid[1][i] = random.choice(numbers_free)
            numbers_free.remove(grid[1][i])
    else:
        generate_grid()
        return
    for e in grid[1][:6]:
        if e not in numbers_free:
            if e not in grid[0][6:9]:
                numbers_free.append(e)
    for e in grid[2][:6]:
        search_remove(e, numbers_free)
    for i in range(6, 9):
        grid[2][i] = random.choice(numbers_free)
        numbers_free.remove(grid[2][i])
    """================== millieu==============="""
    # first line
    numbers_rows = [[], [], []]
    for j in range(0, 9):
        numbers_free = generate_number()
        for i in range(0, 3):
            for elem in numbers_rows:
                substract_list_in_list(elem, numbers_free)
            search_remove(grid[i][j], numbers_free)
            for e in numbers_rows:
                search_remove(e, numbers_free)
        if len(numbers_free) >= 1:
            grid[3][j] = random.choice(numbers_free)
            if j in range(0, 3):
                numbers_rows[0].append(grid[3][j])
            elif j in range(3, 6):
                numbers_rows[1].append(grid[3][j])
            else:
                numbers_rows[2].append(grid[3][j])
        else:
            generate_grid()
            return
    # LIGNE 2 et 3 du carré 1
    for a in range(4, 6):
        for i in range(0, 3):
            numbers_free = generate_number()
            substract_list_in_list(numbers_rows[0], numbers_free)
            for j in range(0, a):
                search_remove(grid[j][i], numbers_free)
            if len(numbers_free) >= 1:
                grid[a][i] = random_append(numbers_free, numbers_rows[0])
            else:
                generate_grid()
                return
        # LIGNE 2 et 3 du carré 2
        for i in range(3, 6):
            numbers_free = generate_number()
            substract_list_in_list(grid[a][:3], numbers_free)
            substract_list_in_list(numbers_rows[1], numbers_free)
            for j in range(0, a):
                search_remove(grid[j][i], numbers_free)
            if len(numbers_free) >= 1:
                grid[a][i] = random_append(numbers_free, numbers_rows[1])
            else:
                generate_grid()
                return
        # LIGNE 2 et 3 du carré 3
        for i in range(6, 9):
            numbers_free = generate_number()
            substract_list_in_list(grid[a][:6], numbers_free)
            substract_list_in_list(numbers_rows[2], numbers_free)
            for j in range(0, a):
                search_remove(grid[j][i], numbers_free)
            if len(numbers_free) >= 1:
                grid[a][i] = random_append(numbers_free, numbers_rows[2])
            else:
                generate_grid()
                return
    "===========BOT=============="
    numbers_rows = [[], [], []]
    for j in range(0, 9):
        numbers_free = generate_number()
        for i in range(0, 6):
            for elem in numbers_rows:
                substract_list_in_list(elem, numbers_free)
            search_remove(grid[i][j], numbers_free)
            for e in numbers_rows:
                search_remove(e, numbers_free)
        if len(numbers_free) >= 1:
            grid[6][j] = random.choice(numbers_free)
            if j in range(0, 3):
                numbers_rows[0].append(grid[6][j])
            elif j in range(3, 6):
                numbers_rows[1].append(grid[6][j])
            else:
                numbers_rows[2].append(grid[6][j])
        else:
            generate_grid()
            return
    # LIGNE 2 et 3 du carré 1
    for a in range(7, 9):
        for i in range(0, 3):
            numbers_free = generate_number()
            substract_list_in_list(numbers_rows[0], numbers_free)
            for j in range(0, a):
                search_remove(grid[j][i], numbers_free)
            if len(numbers_free) >= 1:
                grid[a][i] = random_append(numbers_free, numbers_rows[0])
            else:
                generate_grid()
                return
        # LIGNE 2 et 3 du carré 2
        for i in range(3, 6):
            numbers_free = generate_number()
            substract_list_in_list(grid[a][:3], numbers_free)
            substract_list_in_list(numbers_rows[1], numbers_free)
            for j in range(0, a):
                search_remove(grid[j][i], numbers_free)
            if len(numbers_free) >= 1:
                grid[a][i] = random_append(numbers_free, numbers_rows[1])
            else:
                generate_grid()
                return
        # LIGNE 2 et 3 du carré 3
        for i in range(6, 9):
            numbers_free = generate_number()
            substract_list_in_list(grid[a][:6], numbers_free)
            substract_list_in_list(numbers_rows[2], numbers_free)
            for j in range(0, a):
                search_remove(grid[j][i], numbers_free)
            if len(numbers_free) >= 1:
                grid[a][i] = random_append(numbers_free, numbers_rows[2])
            else:
                generate_grid()
                return



    for i in range(HEIGHT):
        print(grid[i])


generate_grid()
