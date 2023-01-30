import pandas as pd

filepath = "gene_presence_absence.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(filepath, header=0)

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

# Transpose the DataFrame to switch columns and rows
df = df.transpose()
df.columns = df.iloc[0]
df = df.drop(df.index[0])

# Reset the index
df = df.reset_index()

# Move the first column to the last position
cols = df.columns.tolist()
df = pd.concat([df[cols[1:]], df[cols[0]]], axis=1)

# Show the resulting dataframe
print(df)


# Save the transposed DataFrame to a new CSV file
df.to_csv("pangenome_upsetplot.csv", index=True)
