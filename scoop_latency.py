from scoop import futures
import time
import json

def main():
    repeatNum = 5
    maxStrLen = 8
    tasksNum = 4
    for j in range(maxStrLen):
        for repeat in range(repeatNum):
            strToTest = 'H'*(10**j)
            n1 = time.time()
            # tasks = [futures.submit(sleepOneSec) for i in range(1)]
            tasks = [futures.submit(sleepOneSecWithString, strToTest) for i in range(tasksNum)]
            results = [task.result() for task in tasks]
            n2 = time.time()
            t_sleep = (n2 - n1)*10**3
            output = {'stringSize': j, 't_sleep/ms': t_sleep}
            with open('output.json', 'a') as outputFile:
                json.dump(output, outputFile)
                outputFile.write('\n')

def sleepOneSec():
    time.sleep(1)
    return 1

def sleepOneSecWithString(string):
    time.sleep(1)
    return 1

if __name__ == '__main__':
    main()
