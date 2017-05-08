#init_db.py

import sqlite3
import tweepy

conn = sqlite3.connect('tweets.db')
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Tweets")
cur.execute("CREATE TABLE Tweets (author_id INTEGER, time_stamp TEXT, tweet_id INTEGER, tweet_text TEXT)")

cur.execute("DROP TABLE IF EXISTS Authors")
cur.execute("CREATE TABLE Authors (author_id INTEGER, username TEXT, mentioned_time)")

cur.execute("DROP TABLE IF EXISTS Mentions")
cur.execute("CREATE TABLE Mentions (tweet_id INTEGER, author_id INTEGER)")




CONSUMER_KEY = "Ow25HRKngxKQHbveQnvOmpESJ"
CONSUMER_SECRET = "j4nFQQoSjaiEbv3VuiQIGHZiqwWIfuEgY5P56p1i2VuKPvDzEF"
ACCESS_TOKEN = "841811770138349568-377H70dCjVeRh4P16eSwP9RKkqYUOVm"
ACCESS_TOKEN_SECRET = "R7Mo1d9YogBAPX4Xl4SPK09QxHTGVwTFIOqn8Vp0308Uc"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

conn = sqlite3.connect("tweets.db")
cur = conn.cursor()
cur.execute("DELETE FROM Tweets")
cur.execute("DELETE FROM Authors")
cur.execute("DELETE FROM Mentions")


def monthnum(shortMonth):
    return {'Jan' : "1", 'Feb' : "2", 'Mar' : "3", 'Apr' : "4", 'May' : "5", 'Jun' : "6", 'Jul' : "7", 'Aug' : "8",
            'Sep' : "9", 'Oct' : "10", 'Nov' : "11", 'Dec' : "12"}[shortMonth]


def pick():
    page = 1
    author=[]
    while True:
        tweets = api.user_timeline(id="umsi",count=200,page=page)
        if tweets:
            for tweet in tweets:
                json_tweet = tweet._json
                date=str(json_tweet["created_at"]).split(" ")
                if date[1]=="Aug" and date[5]=="2016":
                    return author
                if json_tweet['entities']['user_mentions']:
                    for item in json_tweet['entities']['user_mentions']:
                        cur.execute("INSERT INTO Mentions VALUES (?,?)", (json_tweet["id"], item['id']))
                        if item['screen_name'] not in author:
                            author.append(item["screen_name"])
                            cur.execute("INSERT INTO Authors VALUES (?,?,?)", (item['id'], item['screen_name'], 1))
                        else:
                            cur.execute("SELECT mentioned_time FROM Authors WHERE username="+'"'+
                                        item["screen_name"]+'"')
                            time=cur.fetchone()[0]
                            cur.execute("UPDATE Authors SET mentioned_time="+str(time+1)+" WHERE username="+'"'+
                                        item["screen_name"]+'"')
                timestamp=date[5]+"-"+monthnum(date[1])+"-"+date[2]+" "+date[3]
                record=(json_tweet['user']['id'],timestamp,json_tweet["id"], json_tweet["text"])
                cur.execute("INSERT INTO Tweets VALUES (?,?,?,?)", record)
        else:
            break
        page += 1

nbs=pick()
conn.commit()

num=cur.execute("SELECT COUNT(*) FROM Tweets").fetchone()[0]

def picknb(nb):
    counter=0
    cur.execute("SELECT username FROM Authors WHERE username!=\"umsi\" ORDER BY mentioned_time DESC")
    tt=[]
    for i in cur:
        tt.append(i[0])
    for name in tt:
        tweets = api.user_timeline(id=name, count=20, page=1)
        if tweets:
            for tweet in tweets:
                json_tweet = tweet._json
                date = str(json_tweet["created_at"]).split(" ")
                if date[1] == "Aug" and date[5] == "2016":
                    break
                if json_tweet['entities']['user_mentions']:
                    for item in json_tweet['entities']['user_mentions']:
                        cur.execute("SELECT username FROM Authors")
                        cur.execute("INSERT INTO Mentions VALUES (?,?)", (json_tweet["id"], item['id']))
                        if item['screen_name'] not in nb:
                            nb.append(item["screen_name"])
                            cur.execute("INSERT INTO Authors VALUES (?,?,?)", (item['id'], item['screen_name'], 1))
                        else:
                            cur.execute("SELECT mentioned_time FROM Authors WHERE username=" + '"' +
                                        item["screen_name"] + '"')
                            time = cur.fetchone()[0]
                            cur.execute("UPDATE Authors SET mentioned_time=" + str(time + 1) + " WHERE username=" + '"' +
                                        item["screen_name"] + '"')
                counter+=1
                timestamp = date[5] + "-" + monthnum(date[1]) + "-" + date[2] + " " + date[3]
                record = (json_tweet['user']['id'], timestamp, json_tweet["id"], json_tweet["text"])
                cur.execute("INSERT INTO Tweets VALUES (?,?,?,?)", record)
            if counter > num:
                return


picknb(nbs)
conn.commit()

conn.close()
