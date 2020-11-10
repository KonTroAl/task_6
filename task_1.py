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
from collections import defaultdict
from functools import reduce

"""Python 3.8  OC: 64x"""

"""
First
"""
company = {"LG": 20000, "HP": 300000, "MSI": 80000, "ProDuction": 100000, "GasLight": 150000}
company_max = []
max_val = []
count = 3
lst = list(company.values())


@profile
def func_1():
    while len(max_val) != count:
        val = 0
        i = 1
        for a in lst:
            if a > val:
                i += 1
                val = a
        max_val.append(val)
        lst.remove(val)

    for k, v in company.items():
        for c in max_val:
            if v == c:
                company_max.append(k)
    return max_val, company_max


print(func_1())

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     16.2 MiB     16.2 MiB           1   @profile
    35                                         def func_1():
    36     16.2 MiB      0.0 MiB           4       while len(max_val) != count:
    37     16.2 MiB      0.0 MiB           3           val = 0
    38     16.2 MiB      0.0 MiB           3           i = 1
    39     16.2 MiB      0.0 MiB          15           for a in lst:
    40     16.2 MiB      0.0 MiB          12               if a > val:
    41     16.2 MiB      0.0 MiB           9                   i += 1
    42     16.2 MiB      0.0 MiB           9                   val = a
    43     16.2 MiB      0.0 MiB           3           max_val.append(val)
    44     16.2 MiB      0.0 MiB           3           lst.remove(val)
    45                                         
    46     16.2 MiB      0.0 MiB           6       for k, v in company.items():
    47     16.2 MiB      0.0 MiB          20           for c in max_val:
    48     16.2 MiB      0.0 MiB          15               if v == c:
    49     16.2 MiB      0.0 MiB           3                   company_max.append(k)
    50     16.2 MiB      0.0 MiB           1       return max_val, company_max

Несмотря на неоптимизированный код, проблем с памятью согласно профилировке не выявлено
"""


@profile
def func_2():
    while len(max_val) != count:
        max_val.append(max(lst))
        lst.remove(max(lst))

    company_max = []
    for k, v in company.items():
        for c in max_val:
            if v == c:
                company_max.append(k)
    return max_val, company_max


print(func_2())

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    79     16.2 MiB     16.2 MiB           1   @profile
    80                                         def func_2():
    81     16.2 MiB      0.0 MiB           4       while len(max_val) != count:
    82     16.2 MiB      0.0 MiB           3           max_val.append(max(lst))
    83     16.2 MiB      0.0 MiB           3           lst.remove(max(lst))
    84                                         
    85     16.2 MiB      0.0 MiB           1       company_max = []
    86     16.2 MiB      0.0 MiB           6       for k, v in company.items():
    87     16.2 MiB      0.0 MiB          20           for c in max_val:
    88     16.2 MiB      0.0 MiB          15               if v == c:
    89     16.2 MiB      0.0 MiB           3                   company_max.append(k)
    90     16.2 MiB      0.0 MiB           1       return max_val, company_max

После оптимизации кода удалось уменьшить количество вызовов отдельных компонентов кода. Профилирование второй\
вариации кода также не выявило серьезных затрат памяти."""

########################################################################################################################

"""
Second
"""


@profile
def profit():
    Company = namedtuple('Firms', 'Name Profit_1 Profit_2 Profit_3 Profit_4')
    num = int(input("Введите количество предприятий для расчета прибыли: "))
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


print(profit())

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   120     16.2 MiB     16.2 MiB           1   @profile
   121                                         def profit():
   122     16.2 MiB      0.0 MiB           1       Company = namedtuple('Firms', 'Name Profit_1 Profit_2 Profit_3 Profit_4')
   123     16.2 MiB      0.0 MiB           1       num = int(input("Введите количество предприятий для расчета прибыли: "))
   124     16.2 MiB      0.0 MiB           1       my_dict = {}
   125     16.2 MiB      0.0 MiB           1       res = 0
   126     16.2 MiB      0.0 MiB           1       i = 0
   127     16.2 MiB      0.0 MiB           1       b_name = []
   128     16.2 MiB      0.0 MiB           1       s_name = []
   129     16.2 MiB      0.0 MiB           1       b = 0
   130     16.2 MiB      0.0 MiB           1       s = 0
   131     16.2 MiB      0.0 MiB           1       f = Company
   132     16.2 MiB      0.0 MiB           3       while i < num:
   133     16.2 MiB      0.0 MiB           2           name = input("Введите название предприятия: ")
   134     16.2 MiB      0.0 MiB           4           lst = (input("Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")).split(
   135     16.2 MiB      0.0 MiB           2               " ")
   136     16.2 MiB      0.0 MiB           2           f = Company(Name=name, Profit_1=lst[0], Profit_2=lst[1], Profit_3=lst[2], Profit_4=lst[3])
   137     16.2 MiB      0.0 MiB           2           i += 1
   138     16.2 MiB      0.0 MiB           2           f_sum = int(f.Profit_1) + int(f.Profit_2) + int(f.Profit_3) + int(f.Profit_4)
   139     16.2 MiB      0.0 MiB           2           my_dict[name] = f_sum
   140     16.2 MiB      0.0 MiB           2           res += f_sum
   141     16.2 MiB      0.0 MiB           1       avg = res / num
   142     16.2 MiB      0.0 MiB           3       for k, v in my_dict.items():
   143     16.2 MiB      0.0 MiB           2           if v > avg:
   144     16.2 MiB      0.0 MiB           1               b = v
   145     16.2 MiB      0.0 MiB           1               b_name.append(k)
   146                                                 else:
   147     16.2 MiB      0.0 MiB           1               s = v
   148     16.2 MiB      0.0 MiB           1               s_name.append(k)
   149                                         
   150     16.3 MiB      0.0 MiB           1       return f'Средняя годовая прибыль всех предприятий: {avg} руб. \n' \
   151                                                    f'Предприятия, с прибылью выше среднего значения: {" ".join(b_name)} \n' \
   152                                                    f'Предприятия, с прибылью ниже среднего значения: {" ".join(s_name)}'


Несмотря на неоптимизированный код, проблем с памятью согласно профилировке не выявлено
"""


@profile
def profit_2():
    Company = namedtuple('Firms', 'Name Profit_1 Profit_2 Profit_3 Profit_4')
    num = int(input("Введите количество предприятий для расчета прибыли: "))
    my_aver = {}
    res = 0
    i = 0
    while i < num:
        name = input("Введите название предприятия: ")
        lst = (input("Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")).split(
            " ")
        firm = Company(
            Name=name,
            Profit_1=int(lst[0]),
            Profit_2=int(lst[1]),
            Profit_3=int(lst[2]),
            Profit_4=int(lst[3]))
        i += 1
        my_aver[firm.Name] = (firm.Profit_1 + firm.Profit_2 + firm.Profit_3 + firm.Profit_4) / 4
    for v in my_aver.values():
        res += v
    res = res / num

    for k, v in my_aver.items():
        if v > res:
            print(f"{k} - прибыль выше среднего значения")
        elif v < res:
            print(f"{k} - прибыль ниже среднего значения")
        elif v == res:
            print(f"{k} - средняя прибыль")


profit_2()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   199     16.3 MiB     16.3 MiB           1   @profile
   200                                         def profit_2():
   201     16.3 MiB      0.0 MiB           1       Company = namedtuple('Firms', 'Name Profit_1 Profit_2 Profit_3 Profit_4')
   202     16.3 MiB      0.0 MiB           1       num = int(input("Введите количество предприятий для расчета прибыли: "))
   203     16.3 MiB      0.0 MiB           1       my_aver = {}
   204     16.3 MiB      0.0 MiB           1       res = 0
   205     16.3 MiB      0.0 MiB           1       i = 0
   206     16.3 MiB      0.0 MiB           3       while i < num:
   207     16.3 MiB      0.0 MiB           2           name = input("Введите название предприятия: ")
   208     16.3 MiB      0.0 MiB           4           lst = (input("Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")).split(
   209     16.3 MiB      0.0 MiB           2               " ")
   210     16.3 MiB      0.0 MiB           4           firm = Company(
   211     16.3 MiB      0.0 MiB           2               Name=name,
   212     16.3 MiB      0.0 MiB           2               Profit_1=int(lst[0]),
   213     16.3 MiB      0.0 MiB           2               Profit_2=int(lst[1]),
   214     16.3 MiB      0.0 MiB           2               Profit_3=int(lst[2]),
   215     16.3 MiB      0.0 MiB           2               Profit_4=int(lst[3]))
   216     16.3 MiB      0.0 MiB           2           i += 1
   217     16.3 MiB      0.0 MiB           2           my_aver[firm.Name] = (firm.Profit_1 + firm.Profit_2 + firm.Profit_3 + firm.Profit_4) / 4
   218     16.3 MiB      0.0 MiB           3       for v in my_aver.values():
   219     16.3 MiB      0.0 MiB           2           res += v
   220     16.3 MiB      0.0 MiB           1       res = res / num
   221                                         
   222     16.3 MiB      0.0 MiB           3       for k, v in my_aver.items():
   223     16.3 MiB      0.0 MiB           2           if v > res:
   224     16.3 MiB      0.0 MiB           1               print(f"{k} - прибыль выше среднего значения")
   225     16.3 MiB      0.0 MiB           1           elif v < res:
   226     16.3 MiB      0.0 MiB           1               print(f"{k} - прибыль ниже среднего значения")
   227                                                 elif v == res:
   228                                                     print(f"{k} - средняя прибыль")


После оптимизации кода профилировка памяти не выявила проблем и особозатратных строк кода"""

########################################################################################################################

"""
Third
"""


@profile
def func_3():
    my_dict = defaultdict(list)
    print(my_dict)

    a = list(input("Введите первое число в шестнадцатеричной СС: ").upper())
    for i in range(len(a)):
        my_dict[1].append(a[i])

    b = list(input("Введите второе число в шестнадцатеричной СС: ").upper())
    for i in range(len(b)):
        my_dict[2].append(b[i])

    print(my_dict)

    my_list = []
    my_list.append(int("".join(my_dict[1]), 16))
    my_list.append(int("".join(my_dict[2]), 16))

    my_sum = list(hex(reduce(lambda x, y: x + y, my_list))[2:].upper())
    for i in range(len(my_sum)):
        my_dict["sum"].append(my_sum[i])

    my_mul = list(hex(reduce(lambda x, y: x * y, my_list))[2:].upper())
    for i in range(len(my_mul)):
        my_dict["mul"].append(my_mul[i])

    print(my_dict)


func_3()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   275     16.3 MiB     16.3 MiB           1   @profile
   276                                         def func_3():
   277     16.3 MiB      0.0 MiB           1       my_dict = defaultdict(list)
   278     16.3 MiB      0.0 MiB           1       print(my_dict)
   279                                         
   280     16.3 MiB      0.0 MiB           1       a = list(input("Введите первое число в шестнадцатеричной СС: ").upper())
   281     16.3 MiB      0.0 MiB           3       for i in range(len(a)):
   282     16.3 MiB      0.0 MiB           2           my_dict[1].append(a[i])
   283                                         
   284     16.3 MiB      0.0 MiB           1       b = list(input("Введите второе число в шестнадцатеричной СС: ").upper())
   285     16.3 MiB      0.0 MiB           4       for i in range(len(b)):
   286     16.3 MiB      0.0 MiB           3           my_dict[2].append(b[i])
   287                                         
   288     16.3 MiB      0.0 MiB           1       print(my_dict)
   289                                         
   290     16.3 MiB      0.0 MiB           1       my_list = []
   291     16.3 MiB      0.0 MiB           1       my_list.append(int("".join(my_dict[1]), 16))
   292     16.3 MiB      0.0 MiB           1       my_list.append(int("".join(my_dict[2]), 16))
   293                                         
   294     16.3 MiB      0.0 MiB           3       my_sum = list(hex(reduce(lambda x, y: x + y, my_list))[2:].upper())
   295     16.3 MiB      0.0 MiB           4       for i in range(len(my_sum)):
   296     16.3 MiB      0.0 MiB           3           my_dict["sum"].append(my_sum[i])
   297                                         
   298     16.3 MiB      0.0 MiB           3       my_mul = list(hex(reduce(lambda x, y: x * y, my_list))[2:].upper())
   299     16.3 MiB      0.0 MiB           6       for i in range(len(my_mul)):
   300     16.3 MiB      0.0 MiB           5           my_dict["mul"].append(my_mul[i])
   301                                         
   302     16.3 MiB      0.0 MiB           1       print(my_dict)

Несмотря на неоптимизированный код, проблем с памятью согласно профилировке не выявлено
"""


@profile
def func_4():
    my_dict = defaultdict(list)
    print(my_dict)

    for val in range(2):
        a = list(input(f"Введите {val + 1}-е число в шестнадцатеричной СС: ").upper())
        my_dict[val + 1] = a
    print(my_dict)

    my_sum = sum([int("".join(i), 16) for i in my_dict.values()])
    my_dict["sum"] = list('%X' % my_sum)

    my_mul = reduce(lambda x, y: x * y, [int("".join(i), 16) for i in my_dict.values()])
    my_dict["mul"] = list('%X' % my_mul)

    print(my_dict)


func_4()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   343     16.3 MiB     16.3 MiB           1   @profile
   344                                         def func_4():
   345     16.3 MiB      0.0 MiB           1       my_dict = defaultdict(list)
   346     16.3 MiB      0.0 MiB           1       print(my_dict)
   347                                         
   348     16.3 MiB      0.0 MiB           3       for val in range(2):
   349     16.3 MiB      0.0 MiB           2           a = list(input(f"Введите {val + 1}-е число в шестнадцатеричной СС: ").upper())
   350     16.3 MiB      0.0 MiB           2           my_dict[val + 1] = a
   351     16.3 MiB      0.0 MiB           1       print(my_dict)
   352                                         
   353     16.3 MiB      0.0 MiB           5       my_sum = sum([int("".join(i), 16) for i in my_dict.values()])
   354     16.3 MiB      0.0 MiB           1       my_dict["sum"] = list('%X' % my_sum)
   355                                         
   356     16.3 MiB      0.0 MiB          10       my_mul = reduce(lambda x, y: x * y, [int("".join(i), 16) for i in my_dict.values()])
   357     16.3 MiB      0.0 MiB           1       my_dict["mul"] = list('%X' % my_mul)
   358                                         
   359     16.3 MiB      0.0 MiB           1       print(my_dict)

Профилирование второй вариации кода также не выявило серьезных затрат памяти."""
