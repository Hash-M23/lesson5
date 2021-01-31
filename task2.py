from collections import deque

hex_1 = deque(input('Введите первое число: '))
hex_2 = deque(input('Введите второе число: '))

summ = int(''.join(hex_1), 16) + int(''.join(hex_2), 16)
multiplication = int(''.join(hex_1), 16) * int(''.join(hex_2), 16)

print(hex(summ), hex(multiplication))
hex_summ = str(hex(summ))[2:]
hex_mult = str(hex(multiplication))[2:]

print('Их сумма: ', list(hex_summ),
      '\nИх произведение: ', list(hex_mult))