# -- coding: utf-8 --
name = input('Как вас зовут')
age = int(input('Введите ваш возраст'))
if 0 < age < 75:
    if age >= 16 and name != 'Иван':
        print('Поздравляем вы поступили в ВГУИТ')
    else:
        print('Извините, вы не поступили')
        if age < 16:
            remainder = 16 - age
            if remainder < 5:
                print('Вначале окончите школу, вам осталось', remainder, 'год(а)', sep=' ')
            else:
                print('Вначале окончите школу, вам осталось', remainder, 'лет', sep=' ')
else:
    print('Ошибка')
