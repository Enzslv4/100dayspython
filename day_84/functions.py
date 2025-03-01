from data import print_board

def check_winner(board, player):
    winning_combinations = [
        ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  # Linhas
        ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  # Colunas
        ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']  # Diagonais
    ]
    
    for combination in winning_combinations:
        if all(board[pos] == player for pos in combination):
            return True
    return False


def tic_tac_toe():
    board = {key: ' ' for key in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']}
    players = ['X', 'O']
    turn = 0
    
    while ' ' in board.values():
        print_board(board)
        player = players[turn % 2]
        move = input(f"Jogador {player}, escolha a posição (ex: a1, b2): ")
        
        if move in board and board[move] == ' ':
            board[move] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Jogador {player} venceu!")
                return
            turn += 1
        else:
            print("Posição inválida. Tente novamente.")
    
    print_board(board)
    print("Empate!")