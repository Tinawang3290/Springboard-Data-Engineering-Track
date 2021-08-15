import sys
acc_info_count = {}

def flush():
    '''
    output the composite ket made up of the concatenation of vehicle make and year, the value should be the count of 1
    :return:
    '''
    for i in acc_info_count.keys():
        print(f'{i}\t{acc_info_count[i]}')

for line in sys.stdin:
    line = line.strip()
    make_year, acc_count = line.split('\t')
    acc_count = int(acc_count)
    if make_year not in acc_info_count.keys():
        acc_info_count[make_year] = 0
    acc_info_count[make_year] += acc_count

flush()
