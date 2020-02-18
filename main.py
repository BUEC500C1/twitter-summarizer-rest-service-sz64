from multiprocessing import Process, Event
import threading
import tweets2video as t
import queue
	
def start_process(n_p):
	try:
		t0 = q.get()
		p[n_p] = 1;
		event = Event()
		p0 = Process(target=t.tweet2video, args=(t0,event));
		p0.start();
		event.wait();
		event.clear();
		p[n_p] = 0; 
		q.task_done();
	except:
		print('error starting process');

def check_queue():
	while True:
		if ((q.empty() == False) and not ((sum(p) == 5) and q.full())):
			for n in range(len(p)):
				if p[n] == 0:
					if n == 0:
						try: 
							ts0 = threading.Thread(target=start_process, args=(n,));
							ts0.daemon = True;
							ts0.start();
						except:
							print('error starting thread')
							break
					elif n == 1:
						try: 
							ts1 = threading.Thread(target=start_process, args=(n,));
							ts1.daemon = True;
							ts1.start();
						except:
							print('error starting thread')
							break
					elif n == 2: 
						try: 
							ts2 = threading.Thread(target=start_process, args=(n,));
							ts2.daemon = True;
							ts2.start();
						except:
							print('error starting thread')
							break
					elif n == 3:
						try: 
							ts3 = threading.Thread(target=start_process, args=(n,));
							ts3.daemon = True;
							ts3.start();
						except:
							print('error starting thread')
							break
					elif n == 4:
						try: 
							ts4 = threading.Thread(target=start_process, args=(n,));
							ts4.daemon = True;
							ts4.start();
						except:
							print('error starting thread')
							break
					else: 
						print('Error with queueing and processes');

if __name__ == "__main__":
	q = queue.Queue(5) # Five items can be in queue at once. 
	p = [0, 0, 0, 0, 0];
	main_thread = threading.Thread(target=check_queue);
	main_thread.daemon = True;
	main_thread.start();
	while True:
		choice = input('To start a new video type "1" or type "2" to check status: ');
		if choice == '1':
			if q.full() == False:
				scr_name = input('Please enter a screen name here: ');
				q.put(scr_name);
			else:
				print('Queue is currently full, please try again later.')
		elif choice == '2':
			status = 'There are currently ' + str(sum(p)) + ' out of 5 processes running.';
			print(status)
		else:
			print('Please enter a valid input');