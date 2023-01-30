import pandas as pd
from upsetplot import UpSet

filepath = "pangenome_upsetplot.csv"
df = pd.read_csv(filepath)

ax_dict = UpSet(df, subset_size='count').plot()