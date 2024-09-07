import multiprocessing as mproc
import time

def worker(num):
    """thread worker function"""
    print(f'Worker: {num}. Start at {time.ctime()}')
    # Illusion of work
    time.sleep(2)
    print(f'Worker: {num}. End at {time.ctime()}')
    return num

if __name__ == '__main__':
    print(f'Main process start at {time.ctime()}')
    start_time = time.time()
    jobs: list[mproc.Process] = []
    for i in range(5):
        p = mproc.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    
    # Wait for all processes to finish
    for job in jobs:
        job.join()
    
    end_time = time.time()
    print(f'Main process end at {time.ctime()}')
    print(f'Total time: {end_time - start_time}')