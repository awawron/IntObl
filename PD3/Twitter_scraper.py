import snscrape.modules.twitter as sn
import csv

tweets_list = []
max_tweets = 100

for i,tweet in enumerate(sn.TwitterSearchScraper("WarThunder lang:en").get_items()):
    if i > max_tweets:
        break

    tweetie = (tweet.id, tweet.date, tweet.rawContent, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.lang)
    tweets_list.append(tweetie)
    # print(i)
    # print(tweet.rawContent)
    # print()

with open("tweets.csv", "w") as stream:
    writer = csv.writer(stream)
    for tweet in tweets_list:
        print(tweet)
        writer.writerow(tweet)