# -- coding: utf-8 --
seconds = input()
minutes = seconds / 60
seconds = seconds % 60
hours = minutes / 60
days = hours / 24
print('Дней=', days, 'часов=', hours, 'минут=', minutes, 'секунд=', seconds, sep=(" "))
