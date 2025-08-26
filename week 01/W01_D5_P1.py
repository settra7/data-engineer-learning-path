import pandas as pd

df = pd.read_csv('D:\\IT Courses\\Data Engineer\\Titanic Dataset\\W01_D5_P1_train.csv', sep=',', encoding='utf-8')

df.sort_values(by='Age', ascending=False, inplace=True)

print(df.head(10))