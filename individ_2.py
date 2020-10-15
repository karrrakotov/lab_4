#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
mx = a
mn = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if b < mn:
    mn = b
if c < mn:
    mn = c
print(f"Максимальное число: {mx}")
print(f"Минимальное число: {mn}")
