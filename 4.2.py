"""

Задача №2.

На шаховій дошці стоїть слон. Відзначте положення слона на дошці і
всі клітинки, які б’є слон. Клітинку, де стоїть слон, відзначте буквою
B, клітинки, які б’є слон, відзначте символами *, решта клітинок
заповніть крапками. Програма отримує на вхід координати слона на
шаховій дошці в шаховій нотації, тобто, у вигляді e2, де спочатку
записується номер стовпця (буква від a до h, зліва направо), потім
номер рядка (цифра від 1 до 8, знизу догори). Виведіть на екран
зображення шахової дошки як у вихідних даних.

Виконала: Гриб Наталія Григорівна, 31І група
"""

def print_chessboard(bishop_position):
    chessboard = [['.' for _ in range(8)] for _ in range(8)]

    # Convert chess notation to indices
    col = ord(bishop_position[0]) - ord('a')
    row = int(bishop_position[1]) - 1

    # Mark bishop's position
    chessboard[row][col] = 'B'

    # Mark attacked squares diagonally
    for i in range(8):
        for j in range(8):
            if abs(row - i) == abs(col - j) and (i != row or j != col):
                chessboard[i][j] = '*'

    # Print the chessboard
    for row in chessboard:
        print(" ".join(row))

# Input bishop's position
bishop_position = input("Enter the bishop's position (e.g., e2): ")

# Validate input
if len(bishop_position) == 2 and bishop_position[0].isalpha() and bishop_position[1].isdigit():
    print_chessboard(bishop_position)
else:
    print("Invalid input. Please enter a valid chess notation (e.g., e2).")
