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

# Function 'load_csv' to read csv and put the data into a dataframe
def load_csv():
    # Select specific columns to Analyse
    selectCols = ['Sex', 'County and City', 'CensusYear', 'Age Group', 'VALUE']
    # Load .csv file
    try:
        df = pd.read_csv('./census_ie.csv', usecols= selectCols)
    except FileNotFoundError:
        df = pd.DataFrame()
        return df
    # Rename Columns
    df.rename(columns = {'Sex':'gender', 'County and City': 'county_city', 'CensusYear':'census_year'
                         ,'Age Group': 'age_group', 'VALUE':'total'}, inplace = True)
    return df

# Function 'input_saveFile' to validade option chosen and export .csv file
def input_saveFile(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("\n>> Sorry! Choose a valid option. <<")
            continue
        if value <= 0 or value >2:
            print("\n>> Sorry! Choose a valid option. <<")
            continue
        else:
            if value == 1:
                print("\n>> Ok! \n>> Saving file ... ")
                fPath = os.getcwd() #get the file path
                fileName = "result_" + datetime.now().strftime("%m%d%y_%H%M%S") + ".csv" #build a unique name based on datetime
                dfResult.to_csv(fileName, index=False)
                print(">> File '" + str(fileName) + "' saved at '"+ fPath + "' directory. \n>> Bye! <<")
                break
            else:
                print("\n>> Ok! Thank you for using the system. \n>> Bye! <<")
                break        
    return value

# Display - Welcome message
msgVar= '********************************************************************* \n' 
msgVar = msgVar + "Ireland's Census: population 2011 to 2016. \n"
msgVar = msgVar + 'Total population by:  Age Group | County/City | Gender | Census Year \n' 
msgVar = msgVar + '********************************************************************* \n'  
msgVar = msgVar + ("You can choose multiple options to analyse. ")
print (msgVar)

# Display - Options to chose
optYear = input_options(3, '\nCensus Year - options: \n 1 - Both years \n 2 - 2011 \n 3 - 2016  \nChoose a number for "Census Year" (1, 2 or 3): ')
optGender = input_options(3, '\nGender - options: \n 1 - All genders \n 2 - Female \n 3 - Male  \nChoose a number for "Gender" (1, 2 or 3): ')
optAge = input_options(2, '\nAge - options: \n 1 - All ages \n 2 - Ages by group \nChoose a number for "Age" (1 or 2): ')
optRegion = input_options(2, '\nRegion - options: \n 1 - All regions \n 2 - Regions by County/City \nChoose a number for "Region" (1 or 2): ')
print("\n<< Processing your data ....................... >> \n ")

# Build the query according with options chosen
cYear = opt_query(1, optYear)
cGender = opt_query(2, optGender)
cAge = opt_query(3, optAge)
cRegion = opt_query(4, optRegion)

# Concatenate parameter to the query
query = cYear + cGender + cAge + cRegion

# Load dataframe
census_ie = load_csv()

# If the dataframe is empty, it's because a exception happened at 'load_csv' function.
# and the program will display a message
if census_ie.empty:
    print(">> Sorry! Error loading file! \n>> Make sure que file 'census_ie.csv' is on the '" + os.getcwd() + "' directory and try again.")
else:
    # Load a dataframe according to the query
    dfResult = census_ie.query(query)
    # Display the results
    print(dfResult)
    # Display options to save file 
    optFile = input_saveFile('\nDo you want do save the data into a file? \n(1 = Yes, 2 = No): ')