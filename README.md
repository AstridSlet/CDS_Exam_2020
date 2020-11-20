## Getting and analysing twitter data with Python and R

This repository seeks to provide a simple way of getting and analyzing twitter data, if you are in possession of a txt file with tweet ID’s. 

# 1) 
The file hydrate_tweets_intro.md contains a short guide on how to hydrate tweet ID’s and get a json file with the full tweets and tweet metadata from the txt file using the python library Twarc. 

# 2)
The folder 2_split_and_wordcloud contains the necessary files for handling twitter data, and plotting word clouds.

The 2_split_and_wordcloud folder contains:
analysis.py (script for preprocessing hydrated tweets, splitting data to dates or by hashtags, plotting word clouds)
stopwords.txt (file containing all stopwords, i.e. words that we want excluded in our wordclouds)
wordclouds folder (folder for containing word clouds)
wave.png (picture which holds shape for the wordcloud; can be substituted by another .png files)


# 3)
The sentiment analysis markdown contains a guide on how to get the sentiment scores of the different portion of tweets using the danish sentiment score library Sentida and how to make visualisations of the development in sentiment over time using the gganimate package. 
