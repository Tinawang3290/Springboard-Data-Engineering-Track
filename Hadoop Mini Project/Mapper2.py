import sys

for line in sys.stdin:
    # parse the input we got from Reducer1.py
    line = line.strip()
    line = line.split('\t')
    make = line[1]
    year = line[2]
    print(f'({make}, {year})\t 1')
