#!/bin/bash

# Parsing arguments
# Initialize variables with default values
min_incidences_argument=""

# Parse command-line options
while getopts "m:" opt; do
  case $opt in
    m )
      min_incidences_argument="$OPTARG"
      ;;
    \? )
      echo "Invalid option: -$OPTARG" 1>&2
      exit 1
      ;;
    : )
      echo "Option -$OPTARG requires an argument." 1>&2
      exit 1
      ;;
  esac
done

# Shift to remove the parsed options
shift $((OPTIND-1))

# Check if required arguments are provided
if [ -z "$min_incidences_argument" ]; then
  echo "Usage: $0 -m <min_incidences_argument>"
  exit 1
fi

echo "Minimum incidences taken for the plot: $min_incidences_argument"

#####

# Search for the gene_presence_absence.csv file in the current directory
csv_file=$(find . -type f -name "collapsed_gene_presence_absence.csv" -print -quit)

if [ -z "$csv_file" ]; then
  echo "gene_presence_absence.csv file not found in the current directory."
  exit 1
fi

# Execute getDataFrame.py with the found CSV file
python3 getDataFrame.py --filename "$csv_file"

# Check if the Python script executed successfully
if [ $? -ne 0 ]; then
  echo "getDataFrame.py script encountered an error."
  exit 1
fi

# Search for the gene_presence_absence.csv file in the current directory
pan_file=$(find . -type f -name "pangenome_upsetplot.csv" -print -quit)

# Run upsetPlot.py
python3 upsetPlot.py --filename "$pan_file" --min_incidences "$min_incidences_argument"

# Check if the second Python script executed successfully
if [ $? -ne 0 ]; then
  echo "upsetPlot.py script encountered an error."
  exit 1
fi

echo "Scripts executed successfully."
