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


def baddays(Year, Datasheet):
    # Return: ['Heavily Polluted Days', 'Severely Polluted Days']

    # Select required columns: Year, Value
    # Note: This step is NOT necessary, Program can run without this code
    Datasheet = Datasheet.loc[:, ['Year', 'Value']]
    # |       | Year | Value(PM2.5) |
    # |-------|------|--------------|
    # | 0     | 2008 | 207          |
    # | 1     | 2008 | 180          |
    # | ...   | ...  | ...          |
    # | 79558 | 2017 | 55           |

    # Select target column by given 'Year'
    Datasheet = Datasheet.loc[Datasheet['Year'] == int(Year)]
    # If 'Year' == 2017
    # |       | Year | Value(PM2.5) |
    # |-------|------|--------------|
    # | 75215 | 2017 | 505          |
    # | 75216 | 2017 | 485          |
    # | ...   | ...  | ...          |
    # | 79558 | 2017 | 55           |

    # For keep code as simple, AQI Index use static number instead of variable
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

    return [numOfHeavily, numOfSeverely]
