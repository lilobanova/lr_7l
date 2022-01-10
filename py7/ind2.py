#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    s = list(map(float, input().split()))
    A = float(input("Введите A, первый элемент задаваемого диапазона:"))
    B = float(input("Введите B, последний элемент задаваемого диапазона:"))
    tr = ([el for el in s if A <= el <= B or B <= el <= A])
    print(f"Количество элементов списка, лежащих в диапазоне от А до В = {len(tr)}")
    summ = 0
    s_max = s[0]
    i_max = 0
    for i, item in enumerate(s):
        if item >= s_max:
            i_max, s_max = i, item
    print(f"Максимальный элемент = {s_max}")
    summ = sum([elem for ind, elem in enumerate(s) if ind > i_max])
    print(f"Сумма элементов, расположенные после максимального элемента = {summ}")
    s2 = [abs(elem) for elem in s]
    s2.sort(reverse=True)
    print(s2)
    