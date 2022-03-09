import pandas as pd


data = pd.read_csv("../clean_dataset/combined_data.csv")

data.drop(['album id', 'alternate names'], axis=1, inplace=True)

data.to_csv("../clean_dataset/combined_data.csv", index=False)