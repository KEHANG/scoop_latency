from scoop import futures
import time

def main():
    strToTest = ''
    # strToTest = ''
    n1 = time.time()
    # sleepOneSec()
    # tasks = [futures.submit(sleepOneSec) for i in range(1)]
    tasks = [futures.submit(sleepOneSecWithString, strToTest) for i in range(1)]
    results = [task.result() for task in tasks]
    n2 = time.time()
    t_sleep = (n2 - n1)*10**3
    print('t_sleep/ms: {0:.3f}'.format(t_sleep))

def sleepOneSec():
    time.sleep(1)
    return

def sleepOneSecWithString(string):
    time.sleep(1)

if __name__ == '__main__':
    main()
