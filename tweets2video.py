import datetime
import tweepy
import os
from PIL import Image, ImageDraw, ImageFont
import urllib.request

global n_tweets;
global progress;
n_tweets = 20;
progress = 0;

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
    
def tweets2images(tweets, types, f_name = 'Temp'):
    for t in range(len(tweets)):
        if types[t] == '0':
            im = Image.open('Video\Image Processing\default.jpg');
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
        
def images2video(f_name = 'Temp'):
    print(f_name);
    ffmpeg_line = 'ffmpeg -framerate 1/3 -i Video/' + f_name + '/img%03d.jpg Video/' + f_name + '.mp4';
    os.system(ffmpeg_line);
    
def tweet2video(scr_name):
    # This will be the overarching program that handles the queue and processes.
    f_name = str(datetime.datetime.now());
    f_name = f_name.replace(':','-');
    f_name = f_name.replace(' ','--');
    try:
        os.mkdir('Video/' + f_name)
    except FileExistsError:
        print('Error creating directory for screen name: ' + scr_name);
        event.set()
    tweets, types = tweet_pull(scr_name);
    completed = tweets2images(tweets, types, f_name);
    if completed: 
        images2video(f_name);
    else: 
        print('Error creating tweets from images for screen name: ' + scr_name);