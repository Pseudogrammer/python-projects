import json
import sqlite3
fhand=open("tweets.json")
conn = sqlite3.connect('tweets.db')
cur = conn.cursor()
hashdic={}
cur.execute("DELETE FROM Tweets")
cur.execute("DELETE FROM Hashtags")
for line in fhand:
    js=json.loads(line.strip())
    hashs=js["entities"]["hashtags"]
    if hashs:
        for hash in hashs:
            if hash["text"] not in hashdic:
                hashdic[hash["text"]]=1
            else:
                hashdic[hash["text"]]+=1
for item in hashdic.items():
    item=tuple([None]+list(item))
    cur.execute("INSERT INTO Hashtags VALUES (?,?,?)",item)
conn.commit()
fhand.seek(0)
for line in fhand:
    js=json.loads(line.strip())
    cur.execute("INSERT INTO Tweets VALUES (?,?,?)", (js["id"],js["text"],js["favorite_count"]))
    hashs = js["entities"]["hashtags"]
    if hashs:
        for hash in hashs:
            cur.execute("SELECT hashtag_id FROM Hashtags WHERE hashtag_text=\""+hash["text"]+"\"")
            id0=cur.fetchone()[0]
            cur.execute("INSERT INTO Tweetsdetail VALUES (?,?)", (js["id"], id0))
conn.commit()
conn.close()
fhand.close()






