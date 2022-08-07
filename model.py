from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def getScore(school, gpa, hours, residency, cap):
    
    # Clean Data
    df20 = pd.read_csv('naive_bayes/2020.csv', parse_dates=['Timestamp'])
    df21 = pd.read_csv('naive_bayes/2021.csv', parse_dates=['Timestamp'])
    df21.rename(columns = {"Credit Hours (Please include the exact number)": "Hours"}, inplace=True) 
    # frames = [df20, df21]
    # dfMerged = pd.concat(frames, ignore_index=True)
    # dfMerged['GPA'] = dfMerged['GPA'].apply(lambda gpa: float(gpa))
    # dfMerged['Timestamp'] = dfMerged['Timestamp'].apply(lambda date: date.date())

    newdf20 = df20[['Decision', 'College', 'GPA', 'Hours', 'Residency', 'CAP']].copy()
    newdf21 = df21[['Decision', 'College', 'GPA', 'Hours', 'Residency', 'CAP']].copy()

    newdf20.replace({'College': {'COLA': 1, 'CNS': 2, 'Moody': 3, 'McCombs': 4, 'Cockrell': 5, 'Education': 6,
                         'COFA': 7, 'Social Work': 8, 'Nursing': 9, 'Geosciences': 10, 'Information':11,
                         'Architecture': 12, 'Theatre and Dance': 13}}, inplace=True)

    newdf21.replace({'College': {'COLA': 1, 'CNS': 2, 'Moody': 3, 'McCombs': 4, 'Cockrell': 5, 'Education': 6,
                         'COFA': 7, 'Social Work': 8, 'Nursing': 9, 'Geosciences': 10, 'Information':11,
                         'Architecture': 12, 'Theatre and Dance': 13}}, inplace=True)

    newdf20.replace({'Decision': {'Denied': 0, 'Admitted': 1}, 'Residency': {"International": 0,"Out of state": 0, "In state": 1},
             'CAP': {'No': 0, 'Yes': 1}}, inplace=True)

    newdf21.replace({'Decision': {'Denied': 0, 'Admitted': 1}, 'Residency': {"International": 0,"Out of State": 0, "In State": 1},
             'CAP': {'No': 0, 'Yes': 1}}, inplace=True)

    df_merged = newdf20.append(newdf21, ignore_index=True)
    df_merged['GPA'] = df_merged['GPA'].apply(lambda x: float(x))

    target = df_merged.Decision
    inputs = df_merged.drop('Decision', axis='columns')

    X_train, X_test, Y_train, Y_test = train_test_split(inputs, target, test_size = 0.2)
    model = GaussianNB()
    model.fit(X_train, Y_train)

    students = pd.DataFrame(columns = ['College', 'GPA', 'Hours', 'Residency', 'CAP'])
    students = students.append({'College' : school , 'GPA' : gpa, 'Hours' : hours, 'Residency': residency , 'CAP': cap},
        ignore_index = True)

    student = model.predict_proba(students[:1])
    score = student[0][1]
    return 100*round(score,2)


