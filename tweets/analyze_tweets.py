#analyze_tweets.py

import sqlite3
import nltk

conn = sqlite3.connect('tweets.db')
cur=conn.cursor()



print('***** MOST FREQUENTLY MENTIONED AUTHORS *****')

cur.execute("SELECT username, mentioned_time FROM Authors ORDER BY mentioned_time DESC")
counter=0

for item in cur:
    print(item[0], "is mentioned", item[1], "times")
    counter+=1
    if counter==10:
        break

# Print the 5 most frequently mentioned authors itn the entire corpus
print('*' * 20, '\n\n') # dividing line for readable output



print('***** TWEETS MENTIONING AADL *****')

cur.execute("SELECT tweet_text, time_stamp FROM Tweets JOIN Mentions ON Tweets.tweet_id=Mentions.tweet_id JOIN Authors "
            "ON Mentions.author_id=Authors.author_id WHERE username=\"aadl\"")
for item in cur:
    print(item[0], "( on", item[1], ")")

# Print all tweets that mention the twitter user 'aadl' (the Ann Arbor District Library)
print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger) 
# that appear in tweets from the umsi account

tags=[]
cur.execute("SELECT tweet_text FROM Tweets WHERE author_id=\"18033550\"")
for item in cur:
    tokens=nltk.word_tokenize(item[0])
    tag=nltk.pos_tag(tokens)
    tags+=tag
verbs=[]
for tag in tags:
    if tag[1]=="VB":
        verbs.append(tag[0])
counter={}
for verb in verbs:
    if verb in ['@', '-', '_', b'\xe2\x80\xa6'.decode(), 'umsi', 'umsiasb17', 'umich', 'https']:
        continue
    if verb not in counter:
        counter[verb]=1
    else:
        counter[verb]+=1
counter=dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
n=0
for item in counter:
    print(item,"(",counter[item],"times)")
    n+=1
    if n==10:
        break
print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI "NEIGHBOR" TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger) 
# that appear in tweets from umsi's "neighbors", giving preference to tweets from
# umsi's most "mentioned" accounts
tags=[]
cur.execute("SELECT tweet_text FROM Tweets WHERE author_id!=\"18033550\"")
for item in cur:
    tokens=nltk.word_tokenize(item[0])
    tag=nltk.pos_tag(tokens)
    tags+=tag
verbs=[]
for tag in tags:
    if tag[1]=="VB":
        verbs.append(tag[0])
counter={}
for verb in verbs:
    if verb in ['@', '-', '_', b'\xe2\x80\xa6'.decode(), 'umsi', 'umsiasb17', 'umich', 'https']:
        continue
    if verb not in counter:
        counter[verb]=1
    else:
        counter[verb]+=1
counter=dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
n=0
for item in counter:
    print(item,"(",counter[item],"times)")
    n+=1
    if n==10:
        break
print('*' * 20, '\n\n')


conn.close()