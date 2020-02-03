# NeuroFlow Data Analyst Exercise 1
# By: Sarvottam Salvi
# Date: January 30, 2020

#### Importing libraries and files ####

#Libraries
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Subjective Measures Dataset
Measures = pd.read_csv('C:/Users/bsalv/OneDrive/Documents/Job Application Materials/Neuroflow/Data Analyst Exercise/subj_measures.csv')

#### Cleaning Subjective Measures Dataset ####
# Converting Date to Date-Time
Measures['date'] = pd.to_datetime(Measures['date'])

#### Visualizations ####
    
# User Selection: Ask for input on the id of the individual
UserID = int(input("Enter the User's ID: "))
   
# Get list of User IDs and look for at least one match, use while to re-ask input.
UserData = Measures.drop(Measures[(Measures['user_id'] != UserID)].index)

# Time Frame: Set default as weekly
TimeScale = input("Enter Daily, Weekly, Semi-Monthly or Monthly to select the period over which average values are calculated: ")
    # Assert to make someone choose between the options provided only one option should be possible.

# Creating the dataset with the grouping by type: 
if (TimeScale == "Daily"):
    UserData['DateGroup'] = UserData['date'] - pd.to_timedelta(1, unit='d') 
    UserData = UserData.groupby(['type', pd.Grouper(key='DateGroup', freq='D')])['value'].mean().reset_index().sort_values('DateGroup')
elif (TimeScale == "Weekly"):
    UserData['DateGroup'] = UserData['date'] - pd.to_timedelta(7, unit='d')
    UserData = UserData.groupby(['type', pd.Grouper(key='DateGroup', freq='W')])['value'].mean().reset_index().sort_values('DateGroup')
elif (TimeScale == "Semi-Monthly"):
    UserData['DateGroup'] = UserData['date'] - pd.to_timedelta(15, unit='d')
    UserData = UserData.groupby(['type', pd.Grouper(key='DateGroup', freq='SM')])['value'].mean().reset_index().sort_values('DateGroup')
else:
    # Assumes months are 30 day periods - could actually use the month.
    UserData['DateGroup'] = UserData['date'] - pd.to_timedelta(30, unit='d')
    UserData = UserData.groupby(['type', pd.Grouper(key='DateGroup', freq='M')])['value'].mean().reset_index().sort_values('DateGroup')

# Measurements: Ask for which measures they want to see - one input for each: all (y/n) or one my one (y/n for each)- save in a list.
questionlist = []

AllQuestions = input('Do you want to see responses to all questions? [Y/N] ')
if (AllQuestions == 'Y'):
    questionlist = ['sleep', 'ruminationStress', 'anticipatoryStress', 'mood']

if (AllQuestions == 'N'):
    for question in ['sleep', 'ruminationStress', 'anticipatoryStress', 'mood']:
        check = input('Do you want to see data on ' + question + '? [Y/N] ')
        if (check == 'Y'):
            questionlist.append(question)  
    

# Plotting Week - Week number of axis instead of particular date
plt.figure(3)
for question in questionlist:
    Temp = UserData.drop(UserData[(UserData['type'] != question)].index)
    Temp = Temp.reset_index(drop=True)
    Progress = plt.plot(Temp.index.values , Temp['value'], label = question)

plt.legend()
plt.title(TimeScale + ' Progress')
plt.xlabel(TimeScale)
plt.ylabel('Average Score')

