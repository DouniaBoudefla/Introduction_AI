board=[[-1, 0, -1], [1, 0, -1], [1, -1, 1]]


print(board)
print('\n\n')

# Développer une fonction python visualiser permettrant d'afficher à l'écran une grille de jeu

def visualiser(board):
    chars = {
    -1: 'X',
    +1: 'O',
    0: '.'
    }
    str_line = '+-------------+'
    print('\n' + str_line)
    for row in board:
        for cell in row:
            symbol = chars[cell]
            print(f': {symbol} :', end='')
        print('\n' + str_line)

visualiser(board)
print('\n\n')

# Développer une fonction etatsVoisins permettant d'obtenir touts les indices de cases vides à partir de l'état courant du jeu

def etatsVoisins(board):
    indices = []
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == 0:
                indices.append([row,cell])
    return indices


etatsVoisins(board)
depth=len(etatsVoisins(board))
print(depth)
print(etatsVoisins(board))
print('\n\n')

#  Développer ue fonction choixValide permettant de vérifier que le choix rentré par l'utilisateur est valide (c'est-à-dire correspondant une case vide dans le jeu).

def choixValide(x,y,board):
    indices = etatsVoisins(board)
    return [x, y] in indices

print(choixValide(0,1,board))
print(choixValide(0,0,board))
print('\n\n')

# Développer une fonction aGagne qui retourne si le joueur passé en paramètre a gagné.

def aGagne(board, joueur):

    # Check rows
    for row in board:
        if all(cell == joueur for cell in row):
            return True
        
    # Check columns
    for col in range(len(board[0])):
        if all(row[col] == joueur for row in board):
            return True
        
    # Check diagonals
    if all(board[i][i] == joueur for i in range(len(board))) or all(board[i][len(board) - i - 1] == joueur for i in range(len(board))):
        return True

    return False

print(aGagne(board,-1)) # pour le joueur humain (-1)
print(aGagne(board,1)) # pour la machine (1)
print('\n\n')

# Ecrire une fonction tourJoueurHumain qui saisit la position x et y de la case, vérifie si elle n'est pas déjà occupée et met à jour le jeu.

def tourJoueurHumain(board):
    x = int(input("Saisir la position x (ligne) : "))
    y = int(input("Saisir la position y (colonne) : "))

    if choixValide(x, y, board):
        board[x][y] = -1 
        return board
    else:
        print("Mauvais choix - Recommencer")

board=tourJoueurHumain(board)

# Ecrire une fonction tourMachine qui choisit aléatoirement la position x et y de la case, vérifie si elle n'est pas déjà occupée et met à jour le jeu.

from random import choice
def tourMachine(board):
    indices = etatsVoisins(board)
    
    if indices:
        position = choice(indices)
        x, y = position
        board[x][y] = 1  # Mettre à jour le jeu avec le choix de la machine
    
    return board

print(tourMachine(board))
print('\n\n')

# Ecrire le programme principal permettant de simuler le jeu de morpion

def jeuMorpion() :
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(9):
        visualiser(board)

        # Tour du joueur humain
        board = tourJoueurHumain(board)

        # Vérifier si le joueur humain a gagné
        if aGagne(board, -1):
            print("\nLe joueur humain a gagné")
            print("\nJeu Final")
            visualiser(board)
            return

        # Vérifier si le match est nul
        if not etatsVoisins(board):
            print("Match nul")
            break

        visualiser(board)

        # Tour de la machine
        board = tourMachine(board)

        # Vérifier si la machine a gagné
        if aGagne(board, 1):
            print("\nLa machine a gagné")
            print("\nJeu Final")
            visualiser(board)
            return


print('JEU MORPION:\n')
jeuMorpion()

# Programmer une fonction minimax qui retourne le meilleur choix [best row, best col,best score] au sens de l'algorithme de minimax