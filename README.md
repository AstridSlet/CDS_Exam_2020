# Getting and analysing twitter data with Python and R

This repository seeks to provide a simple way of getting and analyzing twitter data, if you are in possession of a txt file with tweet ID’s. 

The file hydrate_tweets_intro.md contains a short guide on how to hydrate tweet ID’s and get a json file with the full tweets and tweet metadata from the txt file using the python library Twarc. 

The .py file contains a guide on how to do the preprossing of the twitter data in the json file, as well as a method for plotting word clouds ie illustrations of the most frequent words in the cleaned twitter data. In addition it provides a way of splitting your data in portions e.g. before/after a specific data. 

The sentiment analysis markdown contains a guide on how to get the sentiment scores of the different portion of tweets using the danish sentiment score library Sentida and how to make visualisations of the development in sentiment over time using the gganimate package. 
