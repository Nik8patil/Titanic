import numpy as np
import pandas as pd


def basic_exploration(df):
    print('Rows:{} Column:{}'.format(str(df.shape[0]), str(df.shape[1])))
    print(df.info())
    print('Statistics for Numerical Columns')
    print(df.describe())
    print('Statistics for Categorical Columns')
    print(df.describe(include='object'))
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['Count']
    print(null_df[null_df['Count'] > 0])

    def iqr_outlier(array):
        per_75 = np.nanpercentile(array, 75)
        per_25 = np.nanpercentile(array, 25)
        iqr = per_75-per_25
        upper_b = per_75 + (1.5*iqr)
        lower_b = per_25 - (1.5*iqr)
        return [i for i in array if i > upper_b or i < lower_b]
    df_n = df.select_dtypes(exclude='object')
    for i in df_n:
        a = iqr_outlier(df_n[i])
        print(a)
        # Test



    