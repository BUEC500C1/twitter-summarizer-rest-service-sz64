import tweepy
import datetime

global n_tweets;
n_tweets = 20;

def tweet_pull(scr_name):

	keys = open("TKey.txt").read().split();
	consumer_key = keys[0];
	consumer_secret = keys[1];

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	api = tweepy.API(auth)
	
	tweets = [];
	types = [];
	for tweet in tweepy.Cursor(api.user_timeline, screen_name=scr_name, result_type = 'recent', count = n_tweets, tweet_mode='extended').items(n_tweets):
		if tweet.created_at.date() == datetime.datetime.now().date():
			im = tweet.entities.get('media', []);
			tweets.append(tweet.full_text);
			types.append('0');
			if (len(im) > 0):
				tweets.append(im[0]['media_url']);
				types.append('1');
		
	return tweets, types;
	
def tweets2video(tweets, types, f_name):
	
	for t in range(len(tweets)):
		if types(t) == '0':
			print(t);
		elif types(t) == '1':
			print(t);
		else:
			print('Error');