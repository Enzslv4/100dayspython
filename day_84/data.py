def print_board(board):
    mainStructure = f"""     |      |     
  {board['a1']}  |  {board['a2']}   |  {board['a3']}   
     |      |     
------------------
     |      |     
  {board['b1']}  |  {board['b2']}   |  {board['b3']}   
     |      |     
------------------
     |      |     
  {board['c1']}  |  {board['c2']}   |  {board['c3']}   
     |      |     
"""
    print(mainStructure)