from random import randrange

def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    if len(board) == 0:
      WhoIsNext()
      for column in range(3):
        board.append([])
        for row in range(3):
          board[column].append(row)
      board[1][1] = "X"

    col = 1
    for column in range(len(board)):
      rowList = []
      for row in board[column]:
        try:
          rowList.append(row+col)
        except:
          rowList.append(row)

      print("+-------+-------+-------+")
      print("|       |       |       |")
      print(f"|   {rowList[0]}   |   {rowList[1]}   |   {rowList[2]}   |")
      print("|       |       |       |")
      col += 3
      
    print("+-------+-------+-------+")
    print("")

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    global sign
    WhoIsNext()
    allowMovement = False
    
    while not allowMovement:
      try:
        clientChoice = int(input("ingresa tu movimiento: "))
        if clientChoice < 1 or clientChoice >= 10:
          allowMovement = True
          sign = True
          global tie
          tie = True
          print("finalizado el programa")
        else:
          for i in MakeListOfFreeFields(board):
            if clientChoice == (i[1]+1)+i[0]*3:
              allowMovement = True
              board[i[0]][i[1]] = "O"
              break
          if not allowMovement:
            print("ese espacio está ocupado, por favor elige otro")
          print("")
          global clientMove
          clientMove = False
      except:
        print("por favor, ingresa solo números")


def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    empty = []
    for column in range(len(board)):
      for row in board[column]:
        if (row != "X") and (row != "O"):
          empty.append((column, row))

    global tie
    tie = False
    if len(empty) == 1:
      global sign
      tie = True
      sign = True
      if not clientMove:
        DisplayBoard(board)
      print("se agotaron los espacios, hay empate")
    return empty

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    global sign
    if not VictoryFor(board, sign) and len(MakeListOfFreeFields(board)) > 1:
      WhoIsNext()
      allow = False
      while not allow:
        computerMovement = randrange(9)
        for i in MakeListOfFreeFields(board):
          if i[0]*3+i[1]+1 == computerMovement:
            allow = True
            board[i[0]][i[1]] = "X"
            DisplayBoard(board)
            break

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    global clientMove
    if not sign:
      rowCounter = 0
      for row in board:
        rowCounter += 1
        O_Row = 0
        X_Row = 0
        for i in row:
          if i == "O":
            O_Row += 1
          elif i == "X":
            X_Row += 1
        if O_Row == 3 or X_Row == 3:
          if not clientMove:
            DisplayBoard(board)
          print("victoria en la fila", rowCounter)
          sign = True

      if not sign:
        for column in range(len(board)):
          O_Row = 0
          X_Row = 0
          for row in range(len(board)):
            if board[row][column] == "X":
              X_Row += 1
            elif board[row][column] == "O":
              O_Row += 1
          if O_Row == 3 or X_Row == 3:
            if not clientMove:
              DisplayBoard(board)
            print("victoria en la columna", (column+1))
            sign = True
      
      if not sign:
        O_Row = 0
        X_Row = 0
        for i in range(len(board)):
          if board[i][i] == "X":
            X_Row += 1
            i += 1
          elif board[i][i] == "O":
            O_Row += 1
            i += 1
        if O_Row == 3 or X_Row == 3:
          if not clientMove:
            DisplayBoard(board)
          print("victoria en la diagonal descendente")
          sign = True
      
      if not sign:
        O_Row = 0
        X_Row = 0
        for row in range(len(board)):
          allowCounter = True
          for i in range(len(board)-1-row, -1, -1):
            if board[row][len(board)-1-row] == "X" and allowCounter:
              allowCounter = False
              X_Row += 1
            elif board[row][i] == "O" and allowCounter:
              allowCounter = False
              O_Row += 1
              
        if O_Row == 3 or X_Row == 3:
          if not clientMove:
            DisplayBoard(board)
          print("victoria en la diagonal ascendente")
          sign = True

    return sign

def WhoIsNext():
  # La función avisa el turno de cada participante.
  global clientMove
  if clientMove:
    #El cliente utiliza como fichas la letra 'O'
    print("tu turno, ", end="")
    return True
  else:
      #La computadora utiliza como fichas la letra 'X'
    print("turno de la computadora")
    clientMove = True
    return False

def endOfTheGame():
  global clientMove
  if not tie:
    if not clientMove:
      print("felicidades, ganaste")
    else:
      print("buen intento...")
      print("desafía a la computadora nuevamente!")

#
## __INIT__ function
#
def init():
  board = []
  clientMove = False
  sign = False
  tie = False

  DisplayBoard(board)
  while not VictoryFor(board, sign):
    EnterMove(board)
    DrawMove(board)
  endOfTheGame()

#
## INIT
#

init()
