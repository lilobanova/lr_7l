#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = list(map(int, input().split()))
    count = 0
    if len(s) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    m = sum([a for a in s if (2 < a < 20) and (a % 8 == 0)])
    for a in s:
        if (2 < a < 20) and (a % 8 == 0):
            count += 1
    print(f"Сумма элементов больших 2, меньших 20 и кратных 8 = {m}"
          f"\nКоличество элементов больших 2, меньших 20 и кратных 8 = {count}")
