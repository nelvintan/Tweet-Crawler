# Importing everything that is required
import csv
import tweepy
import argparse
import requests

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

parser = argparse.ArgumentParser(description="stream news tweets from Twitter in real time and stores them to a csv file")
parser.add_argument("storage_file", help="csv file to store tweets streamed from Twitter")
parser.add_argument("publishers_file", help="csv file that contains user_id of news publishers to stream from, each row of the file should be of the form: 1) Name 2) Twitter user name 3) Twitter user id")
args = parser.parse_args()

# Authentication and connecting to Twitter API
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# To filter out tweets that are not from the publisher, 
# used in the class MyStreamListener below
def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True
    
# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def __init__(self, fileName):
        super().__init__()
        self.fileName = fileName
        self.f = open(self.fileName, 'a')
        
    def closeFile(self):
        self.f.close()
        print("File has been closed.")
    
    # Using csv
    def on_status(self, status):
        # Only allow tweets from the original creator to be saved
        # tweets with more than 140 characters will contain attribute 'extended_tweet' & has to be read differently
        if from_creator(status) and hasattr(status, 'extended_tweet'):
            # print to confirm everything is working
            print (status.user.name,status.created_at,status.extended_tweet['full_text'],)
            # Writing status data to csv file
            writer = csv.writer(self.f)
            try:
                # Format of csv file per row: 1) Source - Twitter/Others 2) Author 3) Date 4) Text
                writer.writerow(["Twitter",status.user.name,status.created_at,status.extended_tweet['full_text']])
                # not much point getting retweet count/number of comments as tweet has just been posted
            except:
                print("error writing to file")
                raise
        elif from_creator(status) and not hasattr(status, 'extended_tweet'):
            # print to confirm everything is working
            print (status.user.name,status.created_at,status.text,)
            # Writing status data to csv file
            writer = csv.writer(self.f)
            try:
                # Format of csv file per row: 1) Source - Twitter/Others 2) Author 3) Date 4) Text
                writer.writerow(["Twitter",status.user.name,status.created_at,status.text])
                # not much point getting retweet count/number of comments as tweet has just been posted
            except:
                print("error writing to file")
                raise

    def on_error(self, status_code):
        if status_code == 420:
            print("Error 420, please wait a while before trying again...")
            # returning False in on_error disconnects the stream
            return False

# Reading in the name of csv file of publishers
publisher_id_list = []
try:
    with open(args.publishers_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            publisher_id_list.append(row[2])
except IOError:
    print("An error occurred trying to read the file: "+args.publishers_file+".")
    raise

# Start listening
# No catching of exception as a new csv file will be created in current 
# directory if it is not present
myStreamListener = MyStreamListener(args.storage_file)
    
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

try:
    myStream.filter(follow=publisher_id_list)
except KeyboardInterrupt:
    print("You cancelled the operation.")
finally:
    # Closing the file
    myStreamListener.closeFile()