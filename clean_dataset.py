import pandas as pd


df = pd.read_csv('dataset.csv')

sorted_df = df.sort_values(by='popularity', ascending=False)
clean_df = sorted_df.drop_duplicates(subset=['track_name'])

clean_df.to_csv('clean_dataset.csv')




