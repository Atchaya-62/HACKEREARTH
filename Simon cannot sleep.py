import sys

time = sys.stdin.readline().strip()
hrs = time[0:2]
min = time[3:5]
hr = int(hrs)
mi = int(min)
totalmin = (hr * 60) + mi
times =int((totalmin * 11) / 720 + 1)
print(times)
