import os;
import urllib.request
import tweets2video as t

# Unable to test a lot of the functions without the API key. 
def test_tweets2images():
	tweets = ['https://i.imgur.com/MvAk804.jpg'];
	out_name = 'Video/test-images/' + 'img' + str(0).zfill(3) + '.jpg';
	urllib.request.urlretrieve(tweets[0], out_name);
	assert os.path.exists(out_name);
	
def test_images2videos():
	f_name = 'test';
	scr_name = 'scr_name';
	ffmpeg_line = 'ffmpeg -framerate 1/3 -i Video/' + f_name + '/img%03d.jpg Video/' + f_name + '-' + scr_name + '.mp4';
	os.system(ffmpeg_line);
	assert os.path.exists('Video/test-images/test-scr_name');

def test_tweet_pull
	if os.path.exists('keys'):
		tm = t.twittervideo();
		tweets, types = tm.tweet_pull('Google');
		assert ((type(tweets[0]) == str) & (type(types[0]) == int))
	else:
		tweets, types = t.tweet_pull_test_stub('Google');
		assert ((type(tweets[0]) == str) & (type(types[0]) == int))