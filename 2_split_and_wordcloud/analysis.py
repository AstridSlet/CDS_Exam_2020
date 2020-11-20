import json
import pandas as pd
import numpy as np
from textblob import TextBlob
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt
plt.style.use('classic')
import emoji
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from os import path

# load tweets as pd
tweets = pd.read_json("therealtweets.json", lines=True)

# only selecting danish and original tweets
tweets = tweets[(tweets['lang'] == 'da') & (tweets['retweeted'] == False)]

# selecting relevant columns
tweets = tweets[['created_at', 'id', 'full_text','entities', 'retweet_count', 'favorite_count', 'retweeted']]

## create function to clean the tweets
# first define the patterns of emojis in text form 
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"  # below is specific emojis that weren't included in the above
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\U0001f923"
        u'\U0001f914'
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)

# define cleaning function that remove emojis + other stuff
def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #remove "add mentions" ie @ followed by any upper/lower case letter / any number in a 'raw string' (this is why you put the r in there)
    text = re.sub(r'#', '', text) #remove hashtags
    text = re.sub(r'RT[\s]+', '', text) #remove RT's (retweets) followed by one or more wide spaces
    text = re.sub(r'https?:\/\/\S+', '', text) #remove hyperlinks 
    text = emoji_pattern.sub(r'', text) #remove emojis

    return text

# apply clean function to tweets
tweets['full_text'] = tweets['full_text'].apply(cleanText)

## Creating a column for which specificies what hashtags has been used in each tweet
# For 'dkpol"
def nested_find_value(d, needle='dkpol'):
    # we assume d is always a list or dictionary
    haystack = d.values() if isinstance(d, dict) else d
    
    for hay in haystack:
        if isinstance(hay, (__builtins__.list, __builtins__.dict)):
            yield from nested_find_value(hay, needle)
        else:
            yield hay == needle

def find(d, needle='dkpol'):
    return any(nested_find_value(d, needle))

tweets['dkpol'] = tweets["entities"].apply(find)

# For 'dkgreen"
def nested_find_value(d, needle='dkgreen'):
    # we assume d is always a list or dictionary
    haystack = d.values() if isinstance(d, dict) else d
    
    for hay in haystack:
        if isinstance(hay, (__builtins__.list, __builtins__.dict)):
            yield from nested_find_value(hay, needle)
        else:
            yield hay == needle

def find(d, needle='dkgreen'):
    return any(nested_find_value(d, needle))

tweets['dkgreen'] = tweets["entities"].apply(find)

## Splitting the data up into "before anniversary", "after anniversary" and "entire time"
# Preparing the data
tweets['created_at'] = pd.to_datetime(tweets['created_at']) # make column into date format 

# Splitting the data into 3
split_date = '2020-05-04'
tweets_before = tweets[(tweets['created_at'] <= split_date)]
tweets_after = tweets[(tweets['created_at'] >= split_date)]

tweets_before

## Now we want a lot of workcloud plots! One for each time * one for each hashtag 
# We generate a list for each dataframe we want plotted. First element is the dataframe, and second element is the name of the dataframe
tweets_before_dkpol = [tweets_before[(tweets_before['dkpol'] == True)], "tweets_before_dkpol"]
tweets_before_dkgreen = [tweets_before[(tweets_before['dkgreen'] == True)], "tweets_before_dkgreen"]
tweets_after_dkpol = [tweets_after[(tweets_after['dkpol'] == True)], "tweets_after_dkpol"]
tweets_after_dkgreen = [tweets_after[(tweets_after['dkgreen'] == True)], "tweets_after_dkgreen"]
tweets_before = [tweets_before, "tweets_before"]
tweets_after = [tweets_after, "tweets_after"]

# We make a list of these lists
dfs = [tweets_before,
tweets_after,
tweets_before_dkpol,
tweets_before_dkgreen,
tweets_after_dkpol,
tweets_after_dkgreen]

# We prepare stuff for a loop, that makes wordclouds for each of these dataframes
# 1) for the shape of the plots
wave_mask = np.array(Image.open( "wave.jpg")) # for the shape of the plots

# 2) we need a word stoplist (which words not to plot in our plots)
text_file = open("stopwords.txt", 'r') # Downloading stoplist in danish
stopwords = text_file.readlines()

stopwords = [re.sub("\\n", "", word) for word in stopwords] # Cleaning the stoplist (Using regex to delete the '\n' using list comprehension)
stopwords.extend(["gør","gå",'håber','første','bør','først','går', 'gør',"altså","år","sådan",'på','så','få','også','være','måske','får','når', 'gøre','før','må','været','står','fået'])
stopwords = set(stopwords)

# Getting a picture for the shape of our plots (sexy) (http://python-graph-gallery.com/wp-content/uploads/wave.jpg)
wave_mask = np.array(Image.open( "wave.jpg"))

# We make a function that gives plots for each of these, and saves them
for df, df_name in dfs:
    word_list = ' '.join([twt for twt in df['full_text']]) #joining all the single tweets into one word variable
    
    # generate a wordcloud 
    wordcloud = WordCloud(mask=wave_mask,stopwords = stopwords, background_color ='black', min_font_size = 10, width = 1000, height = 800).generate(word_list)
    
    # plot it, and save the plots
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    save_name = "".join(['./wordclouds/', df_name, '.png'])
    plt.savefig(save_name)
    plt.show()
