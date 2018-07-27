# Tweet Crawler

Goal is to stream tweets from specific users and store them in a csv file.

## Getting Started

Please follow this [tutorial](https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/) to obtain your authentication keys that will be used later. There are a total of 4 keys that you will need.

**4 keys:**
- consumer_key
- consumer_secret 
- access_token 
- access_secret

### Prerequisites

These are the 4 libraries that are required for this script.

```
import csv
import tweepy
import argparse
import requests
```

### Installing

Download the code ```crawler.py```

Create 2 other csv files, 1 for the details of publishers and the other for the storage of tweets. Publisher.csv is the input file for the script to read in the user_ids of the publishers. Key in user_name of publisher to this [link](https://tweeterid.com/) to obtain the user_id. Format example is shown below (heading is added for readability, actual csv file does not contain it).

e.g. Publishers.csv

|name |twitter user name |twitter user_id|
| ------------- |:-------------:| -----:|
|The Straits Times|@STcom|37874853|
|One Asia|@sphasiaone|19013879|
|Channel NewsAsia|@ChannelNewsAsia|38400130|
|Makaysiakini|@malaysiakini|18040230|
|BBC|@BBCNews|612473|
|The Independent|@Independent|16973333|
|CNN|@CNN|759251|
|Wall Street Journal|@WSJ|3108351|
|Bloomberg|@business|34713362|
|The Guardian|@guardian|87818409|
|Reuters|@Reuters|1652541|
|National Geographic|@NatGeo|17471979
The Business Times|@BusinessTimes|1181472344
The New Paper|@thenewpaper|34565395
TODAY|@TODAYonline|41085467

e.g. Tweets.csv

|source|publisher name|date & time|tweet|
|:---:|:---:|:---:|:---:|
|Twitter|BBC News (UK)|2018-06-05 01:40:47|Swimmer Ben Lecomte begins record Pacific crossing attempt https://t.co/lAFNYQjsHb|
|Twitter|BBC News (UK)|2018-06-05 01:40:47|Heathrow Airport: Cabinet set for new runway decision https://t.co/C8EShhmhJU|
|Twitter|BBC News (UK)|2018-06-05 01:40:47|Ron Rockwell Hansen: US arrests man for trying to spy for China https://t.co/D6YEOYDev2|

## Running the script

Fill in this part of the code shown below in ```crawler.py``` with your authentication keys.

```
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
```

Simply run ```python crawler.py Tweets.csv Publishers.csv```

For more info on how to run, type ```python crawler.py -h```
