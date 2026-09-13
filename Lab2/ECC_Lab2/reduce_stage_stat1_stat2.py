import sys
from collections import defaultdict
from operator import itemgetter

top_k_flag = False
K = 10

if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        K = int(sys.argv[1])
        top_k_flag = True
    else:
        time_period = sys.argv[1]

hourly_ip_count = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    parts = line.split('\t')
    
    if len(parts) != 3:
        continue 
    
    key, ip, count = parts
    
    try:
        count = int(count)
        if top_k_flag:
            hourly_ip_count[key][ip] += count
        else:
            hourly_ip_count[key][ip] += count
    except ValueError:
        continue

if top_k_flag:
    for hour, ip_count in hourly_ip_count.items():
        sorted_ips = sorted(ip_count.items(), key=itemgetter(1), reverse=True)[:K]
        
        for ip, count in sorted_ips:
            print(f"{ip}\t{count}")

else:
    for hour, ip_count in hourly_ip_count.items():
        sorted_ips = sorted(ip_count.items(), key=itemgetter(0), reverse=True)[:K]
        
        for ip, count in sorted_ips:
            print(f"{hour}\t{ip}\t{count}")
