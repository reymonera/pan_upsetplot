import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import UpSet, plot, from_memberships

filepath = "pangenome_upsetplot.csv"
df = pd.read_csv(filepath)

upset = from_memberships(df)
plot(upset, subset_size='count')
plt.savefig('foo.png')