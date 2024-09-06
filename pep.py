#import this
# выделить + ctrl+alt+L = исправит орфографические ошибки
#from dicts import numbers

#цикл while
# while 1 > 0:  # True. Этот цикл выполняется до момента выполнения его условия
#     number = int(input('Набери число: '))
#     if number % 2 == 0:  # нужно определить четное число или нет
#         print('Число четное')
#         continue  # если выполняется условие выше, то цикл начинается заново
#     else:
#         print('Число не четное')
#     print('меня не забыли')
#     # break # останавливает цикл
# print('Я за циклом')


                    #ДОМАШНЯЯ РАБОТА
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ = 0
while index_ < len(my_list):
    if my_list[index_] < 0:
        break
    if my_list[index_] > 0:
        print(my_list[index_])
    index_ += 1
