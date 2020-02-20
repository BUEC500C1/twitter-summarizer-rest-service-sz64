import tweets2video as t
import threading
import time;


if __name__ == "__main__":
	tm = t.twittervideo()
	tm.tweet2vid('Google'); # Example of a call
	while True:
		time.sleep(1);
