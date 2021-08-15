import sys

for line in sys.stdin:
    line = line.strip()  # remove white space at each end
    data = line.split(',')  # split the string into list by comma separator
    # the mapper output key should be vin_number, and the value should be the incident type, make, and year
    print(f'{data[2]}\t{data[1]}\t{data[3]}\t{data[5]}')



