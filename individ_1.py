#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите возраст: "))
    if n % 10 == 1:
        print(f"Мне {n} год")
    elif 1 < n % 10 < 5:
        print(f"Мне {n} года")
    else:
        print(f"Мне {n} лет", file=sys.stderr)
        exit(1)
