import pandas as pd
import os

files = ["data/transposition_errors.csv", "data/small_typo_errors.csv", "data/phonetic_errors.csv", "data/other_errors.csv"]

output_folder = 'data_lowercase'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for file in files:
    df = pd.read_csv(file)
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    filename = os.path.basename(file).replace(".csv", "_lowercase.csv")
    output_file = os.path.join(output_folder, filename)
    df.to_csv(output_file, index=False)
    print(f"Lowercase file saved as: {output_file}")
