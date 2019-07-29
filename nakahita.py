from decimal import *
import os

getcontext().prec = 100


def pi_nakahita():
    j = 1
    pi = Decimal(3)
    i = 2
    while True:
        os.system("clear")
        pi += j * (Decimal(4)/(Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
        print(i, pi)
        j *= -1
        i += 2


pi_nakahita()
