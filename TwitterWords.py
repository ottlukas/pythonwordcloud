import tweepy, json, random
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
from wordcloud.wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

consumer_key = 'ApnxFhhjoz8eZL7ofISqD8M7k'
consumer_secret = 'cVZE2imOv0ct2lmA8Y4ZbXPn5yIs6fGeczwsizGB09xC9y889s'
access_token = '1288030992-20LasXUuy0aT4Bn4qkLfuuymht3hD2ia7DFgadQ'
access_secret = 'N3dmYIb0ymRfDTMz36miLSMYtsB37G249PUtemlbiDC47'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
  
api = tweepy.API(auth)

f = open('tweets', 'w')
for status in api.user_timeline():
	f.write(api.get_status(status.id).text)
	#print(api.get_status(status.id).text.encode('utf8'))
f.close()

words=' '
count =0
f = open('tweets', 'r')
for line in f:
    words= words + line
f.close

stopwords = {'will', 'youtube', 'YouTube'}
logomask = imread('twitter_mask.png')

wordcloud = WordCloud(
    font_path='Voyager Grotesque(regular).ttf',
    stopwords=STOPWORDS.union(stopwords),
    background_color='black',
    mask = logomask,
    max_words=2000,
    width=2400,
    height=1400
).generate(words)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('./tweetcloud3.png', dpi=300)
plt.show()
