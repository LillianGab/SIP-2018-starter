'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

def avg(lst):
    return sum(lst)/len(lst)

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetstring = ""  #addedafterhisto
for tweet in tweetData:
    tweetstring += tweet['text'] #addafter
    blob = TextBlob(tweet["text"]) #(uncomment to work histogram and avgs)
    tweettext.append(blob) #(uncomment to work histogram and avgs)
#print(tweettext)
#print(tweetstring) #addafter

tweetBlob = TextBlob(tweetstring)
print(tweetBlob.translate(to='es')) #translates to Spanish

#EXAMPLE OF HOW TO FIND AVG
#my_list = [0, 102]
#print(sum(my_list)/len(my_list))

blob_polarity = []
for blob in tweettext:
    blob_polarity.append(blob.polarity)
#print(blob_polarity)
average_polarity = avg(blob_polarity)
print(average_polarity)

blob_subjectivity = []
for blob in tweettext:
    blob_subjectivity.append(blob.subjectivity)
#print(blob_subjectivity)
average_subjectivity = avg(blob_subjectivity)
print(average_subjectivity)

#PART4
word_dict= {}
generic_words = ['and', 'a', 'the', 'or', 'i']
for word in tweetBlob.words:
    if len(word) < 3:
        continue 
    if word.lower() in generic_words:
        continue 
    if not word.isalpha():
        continue
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]
print(word_dict)


#HISTOGRAM
import matplotlib.pyplot as plt

#blob_polarity = [] (don't uncommnet)
plt.hist(blob_polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Polarity Histogram')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

#blob_subjectivity = [] (don't uncomment)
plt.hist(blob_subjectivity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Subjectivity')
plt.ylabel('Number of Tweets')
plt.title('Subjectivity Histogram')
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()





# Textblob sample:
#tb = TextBlob("You are a horrible computer scientist.")
#print(tb.sentiment)