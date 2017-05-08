import sqlite3
def most_common_hashtags():
    conn = sqlite3.connect('tweets.db')
    cur = conn.cursor()
    cur.execute("SELECT hashtag_text, num_occurrences FROM Hashtags ORDER BY num_occurrences DESC")
    counter=0
    for item in cur:
        print(item[0])
        counter+=1
        if counter==20:
            break
    conn.close()
most_common_hashtags()
def fifty_shades_darker():
    conn = sqlite3.connect('tweets.db')
    cur = conn.cursor()
    cur.execute("SELECT hashtag_id FROM Hashtags WHERE hashtag_text=\""+"fiftyshadesdarker"+"\"")
    id0=cur.fetchone()[0]
    cur.execute("SELECT Tweets.tweet_id, Tweets.tweet_text FROM Tweets JOIN Tweetsdetail ON "
                "Tweets.tweet_id=Tweetsdetail.tweet_id WHERE Tweetsdetail.hashtag_id="+str(id0))
    for item in cur:
        print(item[0],item[1])
    conn.close()
fifty_shades_darker()