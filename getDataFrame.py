import pandas as pd
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--filename", required=True, help="Path to the input CSV file")

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of --filename
filename = args.filename

# Now, you can use the 'filename' variable in your script
print(f"Processing CSV file: {filename}")

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(filename, header=0)

# Drop columns 1 and 2
df = df.drop(df.columns[[1, 2]], axis=1)

# Skip the first row
df = df.iloc[1:,:]

# Store the rownames column in a variable
rownames = df.iloc[:, 0]

# Drop the rownames column from the dataframe
df = df.drop(df.columns[0], axis=1)
    
# Replace empty slots with 0 and filled slots with 1
df = df.applymap(lambda x: 0 if pd.isnull(x) else 1)

# Add the rownames column back to the dataframe
df.insert(0, "Gene", rownames)
df = df.set_index("Gene")

# Save the transposed DataFrame to a new CSV file
df.to_csv("pangenome_upsetplot.csv", index=True)
