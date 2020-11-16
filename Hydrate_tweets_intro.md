# Hydrating tweets using Twarc

If you are in possession of a list of tweet ID’s you can get the full tweets and tweet metadata using the python library Twarc. This library can provide a json file with the full twitter data if you input a txt file with the tweet ID’s. This process of getting the full twitter data is called hydrating. NB The tweet ID’s in the txt file should be on separate lines, with no separators.

In order to hydrate tweets you need to set up a twitter app (developer account), which you can apply for via their website. When you have created the twitter app you will get four keys (‘consumer key’, ‘consumer secret’, ‘access token’ and ‘access token secret’), that you use to identify yourself, when you want to extract twitter data. 

This guide tells you how to use Twarc in the terminal. First you check that you have python installed.

# Check python version
python --version

# Install twarc library
pip3 install twarc 

#Now you need to configure twarc in the terminal 

# Configure twarc
twarc configure

#Twarc will now ask you to enter the four keys from the twitter app and press enter between each key.

# Enter twitter keys
consumer key: xxxxxxx
consumer_secret: xxxx
access_token: xxxx
access_token_secret: xxxx


#When you have set all the keys, twarc asks you to log into your twitter account. You copy/paste the provided URL from the terminal into a browser and login and authorize the app. This will give you a pin that you need to type into the terminal.
When you have successfully done this, you are ready to start using twarc. 
You then need to change your directory in the terminal into the folder, where you keep the txt file with the tweet ID’s. 

# Check directory 
pwd

# Change directory to my_folder, where the txt file is placed
cd documents/my_folder  

#When you are in this folder, you can hydrate the tweet ID’s in the txt file using the ‘twarc hydrate’ command. You tell twarc which txt file to hydrate and what it should call the json output file: 

# Hydrate tweets 
twarc hydrate tweet_id_list.txt > hydrated_tweets.json


#The provided guide above follows the steps in this guide: 
https://scholarslab.github.io/learn-twarc/05-install-twarc.html 

###### The end ######
