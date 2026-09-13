import re
import sys

time_period = sys.argv[1]  
start_hour, end_hour = map(int, time_period.split('-'))

pat = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

for line in sys.stdin:
    match = pat.search(line)
    if match:
        hour = int(match.group('hour'))
        ip = match.group('ip')

        if start_hour <= hour < end_hour:
            print(f"{hour}\t{ip}\t1")
