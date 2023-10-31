#!/bin/bash

# Search for the gene_presence_absence.csv file in the current directory
csv_file=$(find . -type f -name "gene_presence_absence.csv" -print -quit)

if [ -z "$csv_file" ]; then
  echo "gene_presence_absence.csv file not found in the current directory."
  exit 1
fi

# Execute getDataFrame.py with the found CSV file
python getDataFrame.py --filename "$csv_file"

# Check if the Python script executed successfully
if [ $? -ne 0 ]; then
  echo "getDataFrame.py script encountered an error."
  exit 1
fi

# Search for the gene_presence_absence.csv file in the current directory
pan_file=$(find . -type f -name "pangenome_upsetplot.csv" -print -quit)

# Run upsetPlot.py
python upsetPlot.py --filename "$pan_file"

# Check if the second Python script executed successfully
if [ $? -ne 0 ]; then
  echo "upsetPlot.py script encountered an error."
  exit 1
fi

echo "Scripts executed successfully."
