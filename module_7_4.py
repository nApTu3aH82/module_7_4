# -*- coding: utf-8 -*-
team1_num = int(input('Введите количество участников первой команды: '))
team2_num = int(input('Введите количество участников второй команды: '))
score_1 = int(input('Введите количество решенных задач первой команды: '))
score_2 = int(input('Введите количество решенных задач второй команды: '))
team1_time = float(input('Введите время, за которое первая команда решила задачи: '))
team2_time = float(input('Введите время, за которое вторая команда решила задачи: '))
task_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / task_total, 2)
# print(f'Общее количество решенных задач: {task_total}')
# print(f"Среднее время на решение одной задачи: {time_avg} с.")
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print('В команде Мастера кода участников: %s' % team1_num)
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {}' .format(score_2))
print('Команда Волшебники двора решили задачи за {} сек.' .format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результаты битвы: {challenge_result}')
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу')