#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd


def value(Year, Datasheet):
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

    # Get average value of 'Year'
    result = Datasheet['Value'].mean()

    # Return float number to 2 decimal place
    return round(result, 2)

