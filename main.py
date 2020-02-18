from multiprocessing import Process, Event
import threading
import tweets2video as t
import queue

def check_queue():
    print('Thread Started')
    while True:
        if q.empty() == False:
            test = q.get();
            print(test);

if __name__ == "__main__":
    q = queue.Queue(5) # Five items can be in queue at once. 
    p = [0, 0, 0, 0, 0];
    main_thread = threading.Thread(target=check_queue);
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
            status = 0;
            print(status)
        else:
            print('Please enter a valid input');