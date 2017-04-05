import subprocess
import datetime
import json
import socket
import fcntl
import struct
import psutil


def get_dna():
    name = subprocess.check_output("hostname | cut -d'.' -f1", shell=True)
    return name
var1 = get_dna()

def get_tm():
       a = datetime.datetime.now()
       return str(a)
var100 = get_tm()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip_Address = get_ip_address('eth0')


def get_readbytes():
        a = psutil.disk_io_counters()
        b = a.read_bytes
        c = a.read_time
        d = (b/c)
        return d
var10 = get_readbytes()

l = [1, 2, 3, 4]

x = (sum(l) / float(len(l)))
y = max(l)
z = min(l)
RecordCount = len(l)
aa = "Disk"
bb = "LogicalName"
cc = "avg_disk_bytes_read"
dd = "Avg.Disk Bytes/Read"
all = {'PerformanceCounterInstanceName':bb,'PerformanceCounterCategory':aa,'PerformanceCounterLabel':cc,'PerformanceCounterName':dd,'AverageValue':x,'MaxValue':y,'MinValue':z,'RecordCount':RecordCount,'HostName':var1,'ReportDateTime':var100,'IPAddress':ip_Address,'Values':[{'DateTime':var100,'Value':var10}]}

print json.dumps(all, indent=4)
