# import sys
# from collections import defaultdict
# from operator import itemgetter

# # Check if the first argument is a number for top K or a time period argument
# top_k_flag = False
# K = 10
# time_period = None

# if len(sys.argv) > 1:
#     if sys.argv[1].isdigit():  # If the first argument is a number, it means it's top K
#         K = int(sys.argv[1])
#         top_k_flag = True
#     else:
#         # If a non-numeric argument is passed, it's assumed to be a TimePeriod (e.g., '00-01')
#         time_period = sys.argv[1]

# # Dictionary to store counts of IPs for each hour
# hourly_ip_count = defaultdict(lambda: defaultdict(int))

# # Process the input from stdin
# for line in sys.stdin:
#     line = line.strip()
#     if not line:
#         continue
    
#     # Split the line into hour, IP, and count
#     parts = line.split('\t')
#     if len(parts) != 3:
#         continue  # Skip malformed lines

#     hour_ip = parts[0]  # e.g., '00:00' or '01:00'
#     ip = parts[1]
#     count = int(parts[2])

#     if top_k_flag:
#         hourly_ip_count[hour_ip][ip] += count
#     else:
#         hourly_ip_count[hour_ip][ip] += count

# # If top K flag is set, output the top K IPs for each hour
# if top_k_flag:
#     for hour, ip_count in hourly_ip_count.items():
#         sorted_ips = sorted(ip_count.items(), key=itemgetter(1), reverse=True)[:K]
#         for ip, count in sorted_ips:
#             print(f"{ip}\t{count}")

# # If it's time period-based, output hour and IP
# else:
#     for hour, ip_count in hourly_ip_count.items():
#         sorted_ips = sorted(ip_count.items(), key=itemgetter(0))
#         for ip, count in sorted_ips:
#             print(f"{hour}\t{ip}")


import sys
from collections import defaultdict
from operator import itemgetter

if len(sys.argv) != 3:
    print("Usage: python reduce_stage.py <time_period> <K>")
    sys.exit(1)

time_period = sys.argv[1]
K = int(sys.argv[2])

start_hour, end_hour = map(int, time_period.split('-'))

hourly_ip_count = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split('\t')
    if len(parts) != 3:
        continue

    hour, ip, count = parts
    try:
        hour = int(hour)
        count = int(count)
        
        if start_hour <= hour < end_hour:
            hourly_ip_count[hour][ip] += count
    except ValueError:
        continue  

for hour in sorted(hourly_ip_count.keys()):
    sorted_ips = sorted(hourly_ip_count[hour].items(), key=itemgetter(1), reverse=True)[:K]
    
    for ip, count in sorted_ips:
        print(f"{hour}:00\t{ip}\t{count}")
