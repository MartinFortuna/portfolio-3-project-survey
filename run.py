#############################################
# Census: Ireland's population 2011 to 2016
# Data Source:
# https://data.gov.ie/dataset/e2022-population-2011-to-2016/resource/ff12fd4b-63a7-48e3-9c8b-a8f309f78cfa
#############################################

# Import Libraries
import pandas as pd
import os
from datetime import datetime

# Function 'input_options' to validade de options chosen
def input_options(opt, prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("\n>> Sorry! You need to choose a given number. <<")
            continue
        if value <= 0 or value >3:
            print("\n>> Sorry! You need to choose a given number. <<")
            continue
        else:
            if opt == 2 and value == 3:
                print("\n>> Sorry! You need to choose a given number. <<")
                continue
            else:
                print("\n>> Ok! <<")
                break 
    return value

# Function 'opt_query' to build the query according with options chosen
def opt_query(optType, optChosen):
    if optType == 1:
        match optChosen:
            case 1:
                return ""
            case 2:
                return "census_year == 2011 and "
            case 3:
                return "census_year == 2016 and "
    elif optType == 2:
        match optChosen:
            case 1:
                return "gender == 'Both sexes' and " 
            case 2:
                return "gender == 'Female' and " 
            case 3:
                return "gender == 'Male' and " 
    elif optType == 3:
        match optChosen:
            case 1:
                return "age_group == 'All ages' and " 
            case 2:
                return "age_group != 'All ages' and "
    elif optType == 4:
        match optChosen:
            case 1:
                return "county_city == 'State'" 
            case 2:
                return "county_city != 'State'"