
# Generating an UpSet plot for your pangenome results

Exactly what the title says, but I didn't bother with naming this with a fancy name since it's basically a bunch of scripts I'm currently using for a multitude of projects and I thought someone who is desperate and lonely like me might like to use this because they feel unimportant (dw, you are, just like me fr).

## What it does
Ehm, you basically will have your `collapsed_gene_presence_abscence.csv` in the same directory as these scripts and then you will execute the `generateUpSet.sh` script like this:
```
bash generateUpSet.sh -m 0
```
The `-m` option is for setting a minimum incidence.

And then you just go to grab something while this runs. It doesn't take that long unless you're dealing with stupid *Pseudomonas*, I guess (yes, that's what I'm doing right now).

I need to change the `collapsed_` thing, I didn't knew it was working like this. More work for me from the future. But it is good to know this still serves its purpose.
## Why you did this
Because I need to do stuff to feel relevant and I thought this was it. That being said, in a more serious tone, I really wanted to start being more diligent with my programming and what I normally do.

### What music do you recommend to do pangenomic analysis
There's a great remix of Pokemon Gym Leader music on YT. Go and find it, you'll feel your soul will elevate from this realm.

## Libraries needed for these scripts to work
This script basically works with a bunch of libraries because fuck good programming practices. These are the libraries:
```
pandas
matplotlib
upsetplot
```

## To-Do List
- There's an error appearing when you execute really big .csv files. I'll need to check on that.
- For now, the minimum of incidences being plotted is determined by the script. I want to parse this through the bash command instead. So yeah.
