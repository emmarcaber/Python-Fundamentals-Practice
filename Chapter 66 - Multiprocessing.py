# CHAPTER 66
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for i/o bound tasks (waiting around)

# NOTE: multiprocessing applies parrallelism, whereas multithreading applies concurrency

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1   

def main():

    # NOTE: the number of process you can create depends on the number of cores your cpu have
    #       if you create more processes than the number of cores you have,
    #       instead of speeding up the processes, it will slow you down
    print(cpu_count())

    # create a process
    a = Process(target = counter, args = (25000000, ))
    b = Process(target = counter, args = (25000000, ))
    c = Process(target = counter, args = (25000000, ))
    d = Process(target = counter, args = (25000000, ))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()
    
    print(f"finished in {time.process_time()} seconds")
    
if __name__ == '__main__':
    main()