import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import UpSet, plot, from_memberships, from_indicators

filepath = "pangenome_upsetplot.csv"
#df = pd.read_csv(filepath, index_col=0).astype(bool)
df = pd.read_csv(filepath).astype(bool)
df = df.drop(df.columns[0], axis=1)


#df = df.set_index("Gene")

#movies = pd.read_csv("https://raw.githubusercontent.com/peetck/IMDB-Top1000-Movies/master/IMDB-Movie-Data.csv")
#movies_by_genre = from_memberships(movies.Genre.str.split(','), data=movies)

#UpSet(from_indicators(["BAKTA_bbacilliformis14.fna", "BAKTA_bbacilliformis15.fna", "BAKTA_bbacilliformis35.fna", "BAKTA_bbacilliformis29.fna"],data=df)).plot()

UpSet(from_indicators(lambda df: df.select_dtypes(bool),
                      data=df),
      min_subset_size=5, show_counts=True).plot()

plt.savefig('min_five_incidences.png')

UpSet(from_indicators(lambda df: df.select_dtypes(bool),
                      data=df),
      show_counts=True).plot()

plt.savefig('total_incidences.png')

#upset = from_memberships(df)
#plot(upset, subset_size='count')