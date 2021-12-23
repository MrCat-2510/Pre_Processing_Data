from clean import *
from readfile import *
import threading
from queue import Queue
text_array = []

class CleanTextThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            ori_string = self.queue.get()
            try:
                clean_text = pre_processing(ori_string)
                text_array.append(clean_text)
            except:
                text_array.append(None)
            finally:
                self.queue.task_done()
            

def MultiThreading_main(size):
    wn.ensure_loaded() 
    citationStringAnnotated = []
    if size == True:
        print('Preprocessing whole columns')
        citationStringAnnotated = df['citationStringAnnotated']
    else:
        print('Preprocessing {} rows'.format(size))
        citationStringAnnotated = df['citationStringAnnotated'].head(size)
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    for x in range(8):
        worker = CleanTextThread(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon=True
        worker.start()
    for i in citationStringAnnotated:
        queue.put(i)
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    print('Completely Done!')
    df_text = pd.DataFrame(text_array)
    df_text.to_csv('multithread_data.csv',index=False,header=False)