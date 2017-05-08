import sqlite3

reset = True

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

if reset:
    cur.execute("DROP TABLE IF EXISTS Tweets")
    cur.execute("CREATE TABLE Tweets (tweet_id INTEGER, tweet_text TEXT, likes INTEGER)")
    cur.execute("DROP TABLE IF EXISTS Hashtags")
    cur.execute("CREATE TABLE Hashtags (hashtag_id INTEGER PRIMARY KEY AUTOINCREMENT, hashtag_text TEXT, "
                "num_occurrences INTEGER)")
    cur.execute("DROP TABLE IF EXISTS Tweetsdetail")
    cur.execute("CREATE TABLE Tweetsdetail (tweet_id INTEGER, hashtag_id INTEGER)")

conn.close()

