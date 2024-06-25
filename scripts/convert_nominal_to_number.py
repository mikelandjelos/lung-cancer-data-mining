import pandas as pd

file_path = "./datasets/lung_cancer.csv"

df = pd.read_csv(file_path)

print("Initial dataset:")
print(df.head())

level_mapping = {"Low": 1, "Medium": 2, "High": 3}

df["Level"] = df["Level"].map(level_mapping)

print("\nDataset after converting 'Level' attribute:")
print(df.head())

df.to_csv("./datasets/lung_cancer_conv.csv", index=False)
