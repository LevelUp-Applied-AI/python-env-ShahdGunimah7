import pathlib
import pandas as pd

# Build path to data/sample.csv relative to this file
data_path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"

df = pd.read_csv(data_path)

print("Shape:", df.shape)
print("\nHead:")
print(df.head())

print("\nDescribe:")
print(df.describe())