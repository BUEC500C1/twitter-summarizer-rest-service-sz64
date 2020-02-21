import os;
import urllib.request

# Unable to test a lot of the functions without the API key. 
def test_tweets2images():
	tweets = ['https://i.imgur.com/MvAk804.jpg'];
	out_name = 'Video/test-images/' + 'img' + str(0).zfill(3) + '.jpg';
	urllib.request.urlretrieve(tweets[0], out_name);
	assert os.path.exists(out_name);
	
def images2videos():
	f_name = 'test';
	scr_name = 'scr_name';
	ffmpeg_line = 'ffmpeg -framerate 1/3 -i Video/' + f_name + '/img%03d.jpg Video/' + f_name + '-' + scr_name + '.mp4';
	os.system(ffmpeg_line);
	assert os.path.exists('Video/test-images/test-scr_name');
	
def check_keys():
	assert os.path.exists('keys');
