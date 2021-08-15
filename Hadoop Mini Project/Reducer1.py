import sys
# [Define group level master information]
current_vin = None
vin = None
make = None
year = None
def reset():
# [Logic to reset master info for every new group]
# Run for end of every group
    current_vin = None
    vin = None
    make = None
    year = None

def flush():
# [Write the output]
# input comes from STDIN
    print(f'{current_vin}\t{make}\t{year}')

# input comes from STDIN
for line in sys.stdin: # [parse the input we got from mapper and update the master info]
    line = line.strip()
    line = line.split("\t")

    vin = line[0]
    incident_type = line[1]
    if current_vin == vin and incident_type == 'I':
        make = line[2]
        year = line[3]
    if current_vin != vin:
        if current_vin != None:
            flush()
        reset()
    if incident_type == 'I':
        make = line[2]
        year = line[3]
    current_vin = vin

flush()


