import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import UpSet, plot, from_memberships, from_indicators
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--filename", required=True, help="Path to the input CSV file")
parser.add_argument("--min_incidences", required=True, help="Minimum incidences for the pangenome plot")

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of --filename and --min_incidences
filename = args.filename
min_incidences = int(args.min_incidences)

# Now, you can use the 'filename' variable in your script
print(f"Processing CSV file: {filename}")

df = pd.read_csv(filename).astype(bool)
df = df.drop(df.columns[0], axis=1)

# Generate a minimum incidence UpSet Plot
UpSet(from_indicators(lambda df: df.select_dtypes(bool),
                      data=df),
      min_subset_size=min_incidences, show_counts=True).plot()

plt.savefig('min_incidences.png')

# Generate a total incidence UpSet Plot
UpSet(from_indicators(lambda df: df.select_dtypes(bool),
                      data=df),
      show_counts=True).plot()

plt.savefig('total_incidences.png')
