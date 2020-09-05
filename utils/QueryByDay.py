#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

def get(Year, Month, Day, Hour, Datasheet):
    PM_Value = Datasheet.query(
        "Year == @Year & Month == @Month & Day == @Day & Hour == @Hour")['Value'].values[0]
    return PM_Value
