# альтернативный вариант решения
first=int(input("Первое число : "))
seconds= int(input("Второе число : "))
third=int(input("Третье число : "))
if first==seconds==third:
    print("вы ввели три одинаковых числа")
elif first==seconds or first==third or seconds==third:
    print("вы ввели два одинаковых числа")
elif not first==seconds==third:
    print("вы ввели три разных числа")
#elif first != seconds != third:
    #print("вы не ввели одинаковых чисел")


#  решение
first=int(input())
seconds= int(input())
third=int(input())
if first==seconds and seconds==third and first==third:
    print(3)
elif first==seconds or first==third or seconds==third:
    print(2)
else:
    print(0)