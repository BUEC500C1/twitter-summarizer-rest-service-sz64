from multiprocessing import Process, Event
import threading
import tweets2video as t
import queue

def check_queue():
    print('Thread Started')
    while True:
        if q.empty() == False:
            for n in range(len(p)):
                if p[n] == 0:
                    if n == 0:
                        try: 
                            t0 = q.get()
                            p[n] = 1;
                            print(t0);
                        except:
                            break
                    elif n == 1:
                        try: 
                            t1 = q.get()
                            p[n] = 1;
                            print(t1);
                        except:
                            break
                    elif n == 2: 
                        try: 
                            t2 = q.get()
                            p[n] = 1;
                            print(t2);
                        except:
                            break
                    elif n == 3:
                        try: 
                            t3 = q.get()
                            p[n] = 1;
                            print(t3);
                        except:
                            break
                    elif n == 4:
                        try: 
                            t4 = q.get()
                            p[n] = 1;
                            print(t4);
                        except:
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