import pandas as pd
try:
    df = pd.read_csv('challenge_2.csv')
    print(df.to_string())
except:
    print('Error')