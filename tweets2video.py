import configparser
import datetime
import json
import threading
import tweepy
from multiprocessing import Process, Event
import os
from PIL import Image, ImageDraw, ImageFont
import queue
import shutil
import urllib.request

global n_tweets;
global progress; # not incorporated yet
global initialized;
global q;
global p;
global queued;
n_tweets = 20;
progress = 0;
q = queue.Queue(5) # Five items can be in queue at once. 
p = [0, 0, 0, 0, 0];
queued = {};

class twittervideo():
	def __init__(self):
		main_thread = threading.Thread(target=self.check_queue);
		main_thread.daemon = True;
		main_thread.start();

	def tweet_pull(self, scr_name):
		global n_tweets;
		
		config = configparser.ConfigParser()
		config.read('keys')
		auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),
					   config.get('auth', 'consumer_secret').strip())
		auth.set_access_token(config.get('auth', 'access_token').strip(),
					  config.get('auth', 'access_secret').strip())
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
	
	def tweets2images(self, tweets, types, f_name = 'Temp'):
		for t in range(len(tweets)):
			if types[t] == '0':
				im = Image.open('Video/Image Processing/default.jpg');
				draw = ImageDraw.Draw(im);
				font = ImageFont.truetype("arial.ttf", 50)
				draw.text((100, 100), tweets[t], fill = 'rgb(255, 255, 255)', font = font);
				out_name = 'Video/' + f_name + '/' + 'img' + str(t).zfill(3) + '.jpg';
				im.save(out_name);
			elif types[t] == '1':
				out_name = 'Video/' + f_name + '/' + 'img' + str(t).zfill(3) + '.jpg';
				urllib.request.urlretrieve(tweets[t], out_name)
			else:
				return False
		return True
			
	def images2video(self, f_name = 'Temp', scr_name = 'scr_name'):
		try:
			ffmpeg_line = 'ffmpeg -framerate 1/3 -i Video/' + f_name + '/img%03d.jpg Video/' + f_name + '-' + scr_name + '.mp4';
			os.system(ffmpeg_line);
			return True;
		except:
			return False;
		
	def tweet2video(self, scr_name, event):
		global queued;
		# This will be the overarching program that handles the queue and processes.
		f_name = str(datetime.datetime.now()); # Using the date and time for each process guarentees unique folder names
		f_name = f_name.replace(':','-'); # Windows can't name folders with colons
		f_name = f_name.replace(' ','--'); # The space confuses ffmpeg
		try:
			os.mkdir('Video/' + f_name)
		except FileExistsError:
			print('Error creating directory for screen name: ' + scr_name);
			event.set()
		tweets, types = self.tweet_pull(scr_name);
		completed = self.tweets2images(tweets, types, f_name);
		if completed: 
			if self.images2video(f_name, scr_name):
				shutil.rmtree('Video/' + f_name) # Deletes the image files used to create the video. 
				try:
					with open('links.json', 'r') as links:
						queued = json.load(links);
						links.close();
				except:
					print('Error links.json missing')
				queued[scr_name] = f_name + '-' + scr_name + '.mp4';
				try: 
					with open('links.json', 'w') as links:
						json.dump(queued,links)
						links.close();
				except:
					print('Error links.json missing')
				event.set()
			else:
				queued[scr_name] = 'Error';
				event.set()
		else: 
			print('Error creating tweets from images for screen name: ' + scr_name);
			queued[scr_name] = 'Error';
			
	def start_process(self, n_p):
		global q;
		global p;
		try:
			t0 = q.get()
			p[n_p] = 1;
			event = Event()
			p0 = Process(target=self.tweet2video, args=(t0,event));
			p0.start();
			event.wait();
			event.clear();
			p[n_p] = 0; 
			q.task_done();
		except:
			print('error starting process');

	def check_queue(self):
		global q;
		global p;
		while True:
			if ((q.empty() == False) and not ((sum(p) == 5) and q.full())):
				for n in range(len(p)):
					if p[n] == 0:
						if n == 0:
							try: 
								ts0 = threading.Thread(target=self.start_process, args=(n,));
								ts0.daemon = True;
								ts0.start();
							except:
								print('error starting thread')
								break
						elif n == 1:
							try: 
								ts1 = threading.Thread(target=self.start_process, args=(n,));
								ts1.daemon = True;
								ts1.start();
							except:
								print('error starting thread')
								break
						elif n == 2: 
							try: 
								ts2 = threading.Thread(target=self.start_process, args=(n,));
								ts2.daemon = True;
								ts2.start();
							except:
								print('error starting thread')
								break
						elif n == 3:
							try: 
								ts3 = threading.Thread(target=self.start_process, args=(n,));
								ts3.daemon = True;
								ts3.start();
							except:
								print('error starting thread')
								break
						elif n == 4:
							try: 
								ts4 = threading.Thread(target=self.start_process, args=(n,));
								ts4.daemon = True;
								ts4.start();
							except:
								print('error starting thread')
								break
						else: 
							print('Error with queueing and processes');

	def tweet2vid(self, scr_name, choice = 1):
		if choice == 1:
			if q.full() == False:
				q.put(scr_name);
			else:
				return 'Queue is currently full, please try again later.';
		elif choice == 2:
			status = 'There are currently ' + str(sum(p)) + ' out of 5 processes running.';
			return status
		else:
			return 'Please enter a valid input';
	
	def get_link(self, scr_name):
		global queued;
		try:
			with open('links.json', 'r') as links:
				queued = json.load(links);
				links.close();
		except:
			print('Error links.json missing')
		try:
			link = queued[scr_name];
		except:
			link = 'Error: Video for this user has not been created yet';
		return link;
		
	
def tweet_pull_test_stub(scr_name = "test"):
	tweets = [];
	types = [];
	with open('tweet_test.json') as tweet_test:
		tweet_test = json.load(tweet_test);
		for t in tweet_test:
			tweets.append(t['tweet']);
			types.append(t['type']);
	return tweets, types;