import pandas as pd
import numpy as np
from time import strftime
import re
from datetime import datetime

def fulfillment_stores(x):
    try:
        if df.isnull().values.any():
            print('There are missing values in the file.\n')
            dx = np.where(pd.isnull(df))
            print(df.loc[df.iloc[dx].index, :])

        else:
            print('No values are missing. OK')
    except:
        pass

    try:
        for zip in df.zipcode:
            if len(str(zip)) <= 5:
                print('True')
            else:
                print('False')
    except:
        pass

    try:
        for country in df.country:
            if len(str(country)) == 2:
                print('True')
            else:
                print('False')
    except:
        pass

    try:
        for state in df.state:
            if len(str(state)) == 2:
                print('True')
            else:
                print('False')
    except:
        pass

    try:
        for day in df.day:
            if len(str(day)) == 3:
                print('True')
            else:
                print('False')
    except:
        pass

# if __name__ == '__main__':

df = pd.read_csv("test_nodes.csv")

# df = df.applymap(fulfillment_stores)

fulfillment_stores(df)
# print(df)
# print(df.startTime)

# print(df)  # debug
