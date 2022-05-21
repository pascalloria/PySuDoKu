# sudoku
# taille : 9*9
# Pas plusieur fois le meme nombre dans une ligne,
# colonne
# dans un mini carré

import random
import copy

HEIGHT = 9
WIDTH = 9

numbers = range(1, WIDTH + 1)
grid_complete = []


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


def carre(numbers_rows, grid, x, y):
    r = -1
    for a in range(x, x + 3):
        r += 1
        for i in range(y, y + 3):
            numbers_free = generate_number()
            substract_list_in_list(grid[a][:y], numbers_free)
            substract_list_in_list(numbers_rows[r], numbers_free)
            for j in range(0, a):
                search_remove(grid[j][i], numbers_free)
            if len(numbers_free) >= 1:
                grid[a][i] = random_append(numbers_free, numbers_rows[r])
            else:
                return True

test_squares = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
def generate_grid():
    grid = []
    for i in range(HEIGHT):
        # génération d'une grille de HEIGHT*WITDH
        grid.append(random.sample(numbers, WIDTH))

    numbers_rows = [[], [], []]
    for square in test_squares:
        x, y = square
        if x == 3 or 6 :
            if y == 0:
                numbers_rows = [[], [], []]
        if carre(numbers_rows, grid, x, y) ==True:
            return

    for i in range(HEIGHT):
        grid_complete.append(grid[i])

while not len(grid_complete) > 1:
    generate_grid()
grid_solution = copy.deepcopy(grid_complete)

for i in range(0, 47):
    a = random.randint(0, 8)
    b = random.randint(0, 8)
    grid_complete[a][b] = ""

for i in range(HEIGHT):
    print(grid_complete[i])

print("====SOLUTION=========")

for i in range(HEIGHT):
    print(grid_solution[i])

"""==============TEST DE CONFORMITE DE LA GRILLE GENERE=============="""


# pour vérifier faire une somme de chaque ligne / chaque colonne et / chaque carré et le résultat doit etre 45
# test somme des éléments de la ligne
def test_row(x):
    somme = 0
    for e in grid_solution[x]:
        somme += e
    return somme


# test somme des éléments de la colonne
def test_collumn(x):
    somme = 0
    for i in range(0, 9):
        somme += grid_solution[i][x]
    return somme


# test somme des éléments du carré
def test_square(x, y):
    somme = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            somme += grid_solution[i][j]
    return somme


# liste contenant les résultats des test
row_tests = []
collumn_tests = []
square_tests = []
# Test ligne et colonnes
for i in range(0, 9):
    if test_row(i) == 45:
        row_tests.append(True)
    else:
        row_tests.append(False)
    if test_collumn(i) == 45:
        collumn_tests.append(True)
    else:
        collumn_tests.append(False)

# liste contenant la position du coin supérieur gauche de chaque carré
# Test des carrés
for square in test_squares:
    x, y = square
    if test_square(x, y) == 45:
        square_tests.append(True)
    else:
        square_tests.append(False)

print()
# test ligne/ colonne / carrée
"""if not False in row_tests:
    print("Toutes les lignes sont correct")
if not False in collumn_tests:
    print("Toutes les colonnes sont correct")
if not False in square_tests:
    print("Tous les carrés sont correct")"""
# test de tout les éléments en meme temps.
if not False in row_tests and collumn_tests and square_tests:
    print("La grille a été généré correctement")
else:
    print("Erreur : La grille n'a pas été généré correctement")

"""==============FIN DU TEST DE CONFORMITE DE LA GRILLE GENERE=============="""
