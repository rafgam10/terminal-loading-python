from sys import prefix
from time import sleep

def loadbar(iteration, total, prefix='', suffix='', decimals=1, lengh=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(lengh * iteration // total)
    bar = fill * filledLength + '-' * (lengh - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', lengh=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix='Progress:', suffix='Complete', lengh=l)