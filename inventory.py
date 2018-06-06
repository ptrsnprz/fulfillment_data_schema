import pandas as pd
import numpy as np
from time import strftime
import re
from datetime import datetime

def inventory(x):
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
        for sku in df.sku:
            if isinstance(sku, int):
                print('True')
            else:
                print('False')
    except:
        pass

    try:
        for store in df.storeNumber:
            if isinstance(store, int):
                print('True')
            else:
                print('False')
    except:
        pass

# if __name__ == '__main__':

df = pd.read_csv("test_inventory.csv")

# df = df.applymap(fulfillment_stores)

inventory(df)

# inventory(df)
# print(df)
# print(df.startTime)

# print(df)  # debug
