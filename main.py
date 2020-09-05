#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
from utils import AvgByYear
from utils import QueryByDay
from utils import StatByMonth
from utils import StatByYear
import pandas as pd


INTEGRATED_FILE = './Beijing_2008-2017_HourlyPM25.csv'

def banner():
    print("""

        這是 Banner
        這邊製作你的學號、姓名、報告名稱 etc.

    """)

def menu():
    ds = pd.read_csv(os.path.abspath("Beijing_2008-2017_HourlyPM25.csv"), encoding='latin1')
    while True:
        func = input("""
    1 - 查詢某天某時刻的PM2.5
    2 - 查詢某月空氣質量優的天數
    3 - 查詢某月空氣質量差的天數
    4 - 某年重度污染的天數
    5 - 某年空氣質量的日均值
    q - Quit

    >> """)
        if func is 'q':
            exit()
        elif func is '1':
            y = input("Year (2008-2017): ")
            m = input("Month (1-12): ")
            d = input("Day (1-31): ")
            h = input("Hour (0-23): ")

            print("\n============================================================")
            print("{}/{}/{} {}:00 | AQI Index: {}µg/mg³".format(
                    y, m, d, h,
                    QueryByDay.get(y, m, d, h, ds)
                )
            )
            print("============================================================\n")

        elif func is '2':
            y = input("Year (2008-2017): ")
            m = input("Month (1-12): ")

            result = StatByMonth.puredays(y, m, ds)

            print("\n============================================================")
            print("{}/{}".format(y, m))
            print("Excellent(0-50): {} Days".format(result[0]))
            print("Good(51-100): {} Days".format(result[1]))
            print("============================================================\n")
        elif func is '3':
            y = input("Year (2008-2017): ")
            m = input("Month (1-12): ")

            result = StatByMonth.sucksdays(y, m, ds)

            print("\n============================================================")
            print("{}/{}".format(y, m))
            print("Lightly Polluted(101-150): {} Days".format(result[0]))
            print("Moderately Polluted(151-200): {} Days".format(result[1]))
            print("Heavily Polluted Days(201-300): {} Days".format(result[1]))
            print("============================================================\n")
        elif func is '4':
            y = input("Year (2008-2017): ")

            result = StatByYear.baddays(y, ds)   # ['Heavily', 'Severely']

            print("\n============================================================")
            print("Year {}".format(y))
            print("Heavily Polluted(201-300): {} Days\nSeverely Polluted(300+): {} Days".format(
                    result[0], result[1]
                )
            )
            print("============================================================\n")
        elif func is '5':
            y = input("Year (2008-2017): ")
            print("\n============================================================")
            print("Year {} | Avg. AQI Index: {}µg/mg³".format(
                    y, AvgByYear.value(y, ds)
                )
            )
            print("============================================================\n")




if __name__ == '__main__':
    banner()
    menu()
