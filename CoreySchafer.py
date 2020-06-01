# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:56:29 2020

@author: padra
"""


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


###  Read a csv into a dataframe  ###
df = pd.read_csv('data/xxx.csv', index_col='Respondent')
schema_df = pd.read_csv('data/yyy.csv', index_col='Column')

### EXPLORING A DATASET ###
df.shape    # Prinsts  (rows, columns)   Is an atribute, so not parenthesis
df.info()   # List the names, number of non-nulls, datatypes   (object usual is a string)
pd.set_option(display.max_columns = 85)  # In juypter this increases the number of columns shown to 85
pd.set_option(display.max_rows = 85)  # In juypter this increases the number of rows shown to 85

df.head()       # Displays the first 5 rows
df.head(10)     # Displays the first 10 rows
df.tail(10)     # Displays the last 10 rows

schema_df


# Defining a dictionary containing lists
people = {
        "first": ["Corey", "Jane", 'John'],
        "last" : ["Schafer", "Doe", "Doe"],
        "email": ["CoreyMSchafer@email.com", "JaneDoe@email.com", 'JohnDoe@email.com']}
people['email']

import pandas as pd

df = pd.DataFrame(people)

df['email']     # Return a series
df.email        # Return the same thing, but column must have different name to attribute or method
type(df['email'])
df[['email']]     # Return a dataframe
type(df[['email']])

df[['last', 'email']]

df.columns
type(df.columns)

##################
## LOC AND ILOC ##
##################


# extract rows and columns with INTERGER location  #
df.iloc[0]  #  Outputs first row as a series (column format)
df.iloc[[0, 1]] #   Outputs a dataframe
df.iloc[[0, 1], 0] #   Extract the email in the first column

# extract rows and columns with loaction  #
df.loc[0]   # First row
df.loc[[0, 1]]   # First and second row
df.loc[[0, 1], ['first', 'last']]   # First and second row and specified columns


df.shape        #  Show (rows, columns)
df.columns      #  Show column names
df['Hobbyist']  # shows head and tail
df['Hobbyist'].value_counts()   #  Creates a frequency table

df.loc[0]                       # Turns the first row into a column
df.loc[[0,1,2], 'Hobbyist']     # Return first three values for Hobbyist
df.loc[0:2, 'Hobbyist']         # Sames as above
df.loc[0:2, 'Hobbyist':'Employmnent']   # Slicing is inclusive of start and end


##################
###  INDICIES  ###
##################


df['email']
df.set_index('email', inplace=True)
df.index
df.loc['CoreyMSchafer@gmail.com']
df.loc['CoreyMSchafer@gmail.com', 'last']
# df.loc[0, 'last'] gives an error
df.iloc[0, 1] # works, but email in no longer counted as a column
df.reset_index(inplace=True) # resets index

# switch to csv version
# df.set_index('Respondent', inplace=True) however, do this in csv read in
schema_df.loc['Hobbyest']                   # Outputs row for Hobbyiest
schema_df.loc['MgrIdiot', 'QuestionText']   # Outputs QuestionText value for MgrIdiot
schema_df.sort_index(inplace=True)
schema_df.sort_index(ascending=False, inplace=True)

###################
###  FILTERING  ###
###################


filt = (df['last'] == "Doe")
df[filt]    
df.loc[filt, 'email']    # Can specify the columns we want with iloc

filt = ((df['last'] == "Doe") & df['first'] == "John"))     # Demo the and operator
filt = ((df['last'] == "Schafer") | df['first'] == "John")) # Demo the or operator

df.loc[~filt, 'email']    # Demo the not operator

high_salary = (df['ConvertedComp'] > 70000)
df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
filt = df['Country'].isin(countires)
df.loc[filt, 'Country']     # Apply countries filter and return Country column

filt = df['LanguageWorkedWith'].str.contains('Python', na=False)    #  Need to set na= to prevent error
df.loc[filt, 'LanguageWorkedWith']     # Apply filter and return LanguageWorkedWith column


#######################
##  UPDATING VALUES  ##
#######################

# rename / modify all columes
df.columns
df.columes = ['first_name', 'last_name', 'email']
df,columns = [x.opper for x in df columns]      ### Change colume names to uppercase
df.columns = df.columns.str.replace(' ', '_')     ### Replace spaces with underscores
# rename some volumes
df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace = true)

# Update values
df.loc[2]
df.loc[2] = ['john', 'Smith'. 'JohnSmith@email.com']    # Replace enitre row
df.loc[2, ['last', 'email']]
df.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com'] # Replace some values in a row
df.loc[2, 'first']
df.loc[2, 'first'] = 'John'  # Replace one value in a row
df.at[2, 'first'] = 'John'  # Replace one value in a row ???

filt = (df['email']=='JohnDoe@email.com')
df[filt]['last'] = 'Smith'  # This does not work!!!  This statement outputs a copy (not a view)
df.loc[filt, 'last'] = 'Smith'  # This does work as uses a view.

 Apply functions 
df['email'].str.lower()
df['email'] = df['email'].str.lower()

#apply - Call a function on our values
# Apply on series
df['email'].apply(len)
def update_email(email):
    return email.upper()
df['email'].apply(update_email) # pass in the function without (), we don't want to execute it
df['email'] = df['email'].apply(update_email)
df['email'].apply(lambda x: x.lower())  # Does the same thing using a lambda function
#Apply on dataframe
df.apply(len)   # Give the length of each series in the dataframe
len(df['email'])
df.apply(len, axis='columns')   # 'rows' is the default
df.apply(pd.Series.min)     # gives the min of each series - alphabetically
df.apply(lambda x: x.min()) # Note that x here, is a series.  Can only use series function

# applymap - Apply to each value of a datasest
df.applymap(len)    # No longer getting the lenght of a series
df.applymap(str.lower)  # Only works if all values of dataframe are strings

# map
df['first'].map{{'Corey': 'Chris', 'Jane': 'Mary'}} # Replaces values, removes if missing

#replace
df['first'].replace{{'Corey': 'Chris', 'Jane': 'Mary'}} # Replaces values, 

# Apply what we have learned to real data
df.rename(columes={'ConvertedComp': 'SalaryUSD'})   # Check that change went through
df.rename(columes={'ConvertedComp': 'SalaryUSD'}, inplace = True)   # Apply change

df['Hobbyist']
df['Hobbyist'].map{{'Yes': True, 'No', False}}
df['Hobbyist'] = df['Hobbyist'].map{{'Yes': True, 'No', False}}


###################################
## ADD / REMOVE COLUMES AND ROWS ##
###################################

# columes
df['first'] + ' ' + df['last']
df['full_name'] = df['first'] + ' ' + df['last'] # Cannot use dot notation, as attributes are assigned that way

df.drop(columns=['first', 'last'], inplace = True)
df['full_name'].str.split(' ')          # return a list, can set this back to df
df['full_name'].str.split(' ', expland) # expand to a df
df[['first', 'last']] = df['full_name'].str.split(' ', expland)


# rows
df.append({'first': Tony})  # This will give an error becase there is no index
df.append({'first': Tony}, ignore_index=True)   # phyton will choose an index.  Other values set to Nan

people = {
        "first": ["Tony", "Steve"],
        "last" : ["Stark", "Rodgers"],
        "email": ["IronMan@avenge.com", "Cap@avenge.com"]}
df2 = pd.DataFrame(people)
df2
df.append(df2, ignore_index=True, sort=False) # Sort will be set to False by default
df = df.append(df2, ignore_index=True, sort=False)  # no inplace option

df.drop(index = 4, inplace=True) # Drops the row corresponding to the index of 4
filt = ('last'=='Doe')
df.drop(index=df[filt].index)    # using condition.  Note the use of index. Otherwise use loc


##################
## SORTING DATA ##
##################

df.sort_values(by='last')   # Sort by last name
df.sort_values(by='last', ascending=False)  # Sort by decending last name
df.sort_vallues(by=['last', 'first'])       # Sort on two variables
df.sort_vallues(by=['last', 'first'], ascending=[False, True], inplace = True)  # Including both asc and desc order

df.sort_index() # sorts by index

df['last'].sort_values()    # Sorts a series (not a dataframe)

# Apply what we have learned to real data
df.sort_values(by=['Country', inplace=True])    # Sort data by countries
df['Country'].head(50) # look at first 50 rows
df[['Country', 'ConvertedComp']].head(50) 
df.sort_values(by=['Country', inplace=True, ascending=[True, False]])    # Sort data by country with highest salaries first
# Nan is minus infinity

# find largest and smallest values
df['ConvertedComp'].nlargest(10)    # Gives 10 largest salary
df.nlargest(10, 'ConvertedComp')    # Returns the full dataframe
df.nsmallest(10, 'ConvertedComp')    # Gives the 10 smallest


###################################
## GROUPING AND AGGREGATING DATA ##
###################################

df.head()
df['ConvertedComp'].head(15)    # Outputs the first 15 values
df['ConvertedComp'].median()    # Outputs the median income
df.median()     # Finds all numerical series and outputs median value
df.describe()   # Gives a brother range of metrics for numerical values - proc mean
df['ConvertedComp'].count()     # Gives the number of non NaN values
df['Hobbyist'].value_counts()   # Returns a proc freq of Hobbyist series
df['SocialMedia'].value_counts()    # Returns a frequency table for SocialMedia series
df['SocialMedia'].value_counts(normalize=True) # Percentage - Values sum to 1

# Grouping data
df['Country'].value_counts()
country_grp = df.groupby(['Country'])     # Returns a DataFrameGroupBy object
country_grp.get_group('India')      # Returns df dataframe for only India - Similar to filter

filt = df['Country'] == "India"
df.loc[filt]                        # Returns the same this as groupby object
df.loc[filt].['SocialMedia'].value_counts()     # Returns the top sites for india

country_grp['SocialMedia'].value_counts()               # Most popular my country
country_grp['SocialMedia'].value_counts().head(50)      # Force to show 50 rows
country_grp['SocialMedia'].value_counts().loc['India']  # Show India only
country_grp['SocialMedia'].value_counts(normalize=True).loc['India']  # Shows percentages

country_grp['ConvertedComp'].median()                   # Median salary by country
country_grp['ConvertedComp'].median().loc['Germany']    # Median salary for Germany
country_grp['ConvertedComp'].agg(['median', 'mean'])    # Gives the median and mean

filt = df['Country'] == "India"
df.loc[filt]                      
df.loc[filt].['LanguageWorkedWith'].str.contains('Python')  # Return true or false
df.loc[filt].['LanguageWorkedWith'].str.contains('Python').sum()  # counts number who know python

country_grp['LanguageWorkedWith'].str.contains('Python').sum()   #  !!! Will not work  !!!  This is a series groupby object not a series
country_grp['LanguageWorkedWith'].apply(lambda x: x.str.countains('Python').sum())  #  Need to use apply to create x which is a series

# what percentage know python in each country
country_respondents = df['Count'].count()    #  Count respondents
country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.countains('Python').sum())  #  Count who uses python
python_df = pd.concat([country_respondent, country_uses_python], axis='columns', sort=False) # Joins by country
python_df.remane(columes{'Country': 'NumRespondents', 'LanguageWorkedWith' : 'NumKnowsPython'}. inplace=True)
python_df['PctKnowsPython'] = (python_df['NumKnowsPython'] / python_df['NumRespondents']) * 100
python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)
python_df.head(50)
python_df.loc['Japan']   # Country names are the index for python_df


#########################################
##  MISSING VALUES AND CASTING DTYPES  ##
#########################################



























