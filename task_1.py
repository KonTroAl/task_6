"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile
from collections import namedtuple

"""
First
"""
# company = {"LG": 20000, "HP": 300000, "MSI": 80000, "ProDuction": 100000, "GasLight": 150000}
# company_max = []
# max_val = []
# count = 3
# lst = list(company.values())
#
#
# @profile
# def func_1():
#     while len(max_val) != count:
#         val = 0
#         i = 1
#         for a in lst:
#             if a > val:
#                 i += 1
#                 val = a
#         max_val.append(val)
#         lst.remove(val)
#
#     for k, v in company.items():
#         for c in max_val:
#             if v == c:
#                 company_max.append(k)
#     return max_val, company_max
#
#
# print(func_1())

"""
Несмотря на неоптимизированный код, проблем с памятью согласно профилировке не выявлено
"""

# @profile
# def func_2():
#     while len(max_val) != count:
#         max_val.append(max(lst))
#         lst.remove(max(lst))
#
#     company_max = []
#     for k, v in company.items():
#         for c in max_val:
#             if v == c:
#                 company_max.append(k)
#     return max_val, company_max
#
#
# print(func_2())

"""После оптимизации кода удалось уменьшить количество вызовов отдельных компонентов кода. Профилирование второй\
вариации кода также не выявило серьезных затрат памяти."""

"""
Second
"""

Company = namedtuple('Firms', 'Name Profit_1 Profit_2 Profit_3 Profit_4')
num = int(input("Введите количество предприятий для расчета прибыли: "))


def profit(num):
    my_dict = {}
    res = 0
    i = 0
    b_name = []
    s_name = []
    b = 0
    s = 0
    f = Company
    while i < num:
        name = input("Введите название предприятия: ")
        lst = (input("Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")).split(
            " ")
        f = Company(Name=name, Profit_1=lst[0], Profit_2=lst[1], Profit_3=lst[2], Profit_4=lst[3])
        i += 1
        f_sum = int(f.Profit_1) + int(f.Profit_2) + int(f.Profit_3) + int(f.Profit_4)
        my_dict[name] = f_sum
        res += f_sum
    avg = res / num
    for k, v in my_dict.items():
        if v > avg:
            b = v
            b_name.append(k)
        else:
            s = v
            s_name.append(k)

    return f'Средняя годовая прибыль всех предприятий: {avg} руб. \n' \
           f'Предприятия, с прибылью выше среднего значения: {" ".join(b_name)} \n' \
           f'Предприятия, с прибылью ниже среднего значения: {" ".join(s_name)}'


print(profit(num))
