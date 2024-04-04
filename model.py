import os
import pandas as pd


df = pd.read_csv(os.path.join("SampleDataset", "sampleJD.csv"))
print(df.info())


duplicate_rows = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicate_rows)
