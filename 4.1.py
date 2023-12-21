"""

Задача №1.

Напишіть програму, яка приймає на вхід список чисел і число (в
окремих рядках), після чого виводить всі позиції через пропуск, на
яких це число зустрічається в переданому списку (позиції у списку
нумеруються з 1). Позиції повинні бути виведені в порядку зростання.
Якщо число не знайдено в списку, потрібно вивести рядок None (без
лапок, з великої літери).

Виконала: Гриб Наталія Григорівна, 31І група
"""

def find_positions(numbers, target):
    positions = [i + 1 for i, num in enumerate(numbers) if num == target]
    return positions if positions else None

# Ввід списку чисел
numbers = []
while True:
    try:
        num = int(input("Введіть число (0 для завершення вводу): "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

# Ввід шуканого числа
target_number = int(input("Введіть шукане число: "))

# Знаходимо та виводимо позиції
positions = find_positions(numbers, target_number)
print(positions)
