import re
import sys

pat = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\[(?P<date_time>[^\]]+)\]')

for line in sys.stdin:
    match = pat.search(line)
    if match:
        ip = match.group('ip')
        date_time = match.group('date_time')
        
        hour = date_time.split(":")[1]
        
        print(f"{hour}\t{ip}\t1")
