#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

AQI = (
    {"Excellent": (0, 50)},
    {"Good": (51, 100)},
    {"Lightly Polluted": (101, 150)},
    {"Moderately Polluted": (151, 200)},
    {"Heavily Polluted": (201, 300)},
    {"Severely Polluted": 301},
)

def Selector(y, m, ds):
    # Ref: StatByYear.py

    # Select required columns: Year, Month, Value
    # Note: This step is NOT necessary, Program can run without this code
    ds = ds.loc[:, ['Year', 'Month', 'Value']]
    # |       | Year | Month| Value(PM2.5) |
    # |-------|------|------|--------------|
    # | 0     | 2008 | 1    | 207          |
    # | 1     | 2008 | 2    | 180          |
    # | ...   | ...  | ...  | ...          |
    # | 79558 | 2017 | 6    | 55           |

    # Select target column by given 'Year' and 'Month'
    ds = ds.loc[ds['Year'] == int(y)]
    ds = ds.loc[ds['Month'] == int(m)]
    # If 'Year' == 2017 and 'Month' == 5
    # |       | Year | Month| Value(PM2.5) |
    # |-------|------|------|--------------|
    # | 78096 | 2017 | 5    | 25           |
    # | 78097 | 2017 | 5    | 35           |
    # | ...   | ...  | ...  | ...          |
    # | 78839 | 2017 | 5    | 19           |
    return ds




def puredays(Year, Month, Datasheet):
    # Return: ['Excellent Days', 'Good Days']

    Datasheet = Selector(Year, Month, Datasheet)    # Functionalized !

    # For keep code as simple, AQI Index use static number instead of variable
    # Excellent Filter
    ExcellentObj = Datasheet.apply(
        lambda x: True if x['Value'] >= 51 else False, axis=1
    )
    numOfExcellent = len(ExcellentObj[ExcellentObj == True].index)

    # Good Filter
    GoodObj = Datasheet.apply(
        lambda x: True if x['Value'] >= 51 and x['Value'] <= 100 else False, axis=1
    )
    numOfGood = len(GoodObj[GoodObj == True].index)

    return [numOfExcellent, numOfGood]


def sucksdays(Year, Month, Datasheet):
    # Return:
    # ['Lightly Polluted Days', 'Moderately Polluted Days', 'Heavily Polluted Days', 'Severely Polluted Days']

    Datasheet = Selector(Year, Month, Datasheet)    # Functionalized !

    # For keep code as simple, AQI Index use static number instead of variable

    # Lightly Polluted Filter
    LightlyObj = Datasheet.apply(
        lambda x: True if x['Value'] >= 101 and x['Value'] < 151 else False, axis=1
    )
    numOfLightly = len(LightlyObj[LightlyObj == True].index)

    # Moderately Polluted Filter
    ModeratelyObj = Datasheet.apply(
        lambda x: True if x['Value'] >= 151 and x['Value'] < 201 else False, axis=1
    )
    numOfModerately = len(ModeratelyObj[ModeratelyObj == True].index)

    # Heavily Polluted Filter
    HeavilyObj = Datasheet.apply(
        lambda x: True if x['Value'] >= 201 and x['Value'] < 301 else False, axis=1
    )
    numOfHeavily = len(HeavilyObj[HeavilyObj == True].index)

    # Severely Polluted Filter
    SeverelyObj = Datasheet.apply(
        lambda x: True if x['Value'] >= 301 else False, axis=1
    )
    numOfSeverely = len(SeverelyObj[SeverelyObj == True].index)

    return [numOfLightly, numOfModerately, numOfHeavily, numOfSeverely]
