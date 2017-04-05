#!/usr/bin/python

import netifaces
import json
import socket
import fcntl
import struct
import psutil
import logging
import os
import platform
import dmidecode
import subprocess
import datetime
from pprint import pprint

# Getting the disk_information of the current system

def kb_to_gb(val_in_kb):

  val_in_gb = round((float(val_in_kb) / float(1024*1024*1024)),2)
  
  return str(val_in_gb) + 'GB'






# partions = psutil.disk_partitions()
# dev_to_mnt_point_dict = {}
# dev_to_disk_space = {}
# devices = []
# mount_points = []
# output = {}

# for partion in partions:
#   #print partion.device
#   dev_to_mnt_point_dict[partion.device] = partion.mountpoint

# for dev, mnt_point in dev_to_mnt_point_dict.iteritems():
#   usage = psutil.disk_usage(mnt_point)
#   total_disk = usage.total
#   usage_percent = usage.percent
#   mnt_point_dict = {}
#   disk_dict = {}
#   used_per_dict = {}
#   mnt_point_dict['mount_point'] = mnt_point  
#   disk_dict['Total_disk'] = kb_to_gb(total_disk)
#   used_per_dict['Percent_used'] = usage_percent
#   disk_stats = [mnt_point_dict,disk_dict,used_per_dict]
#   dev_to_disk_space['DeviceID: '+dev] = disk_stats



def get_disks_info():
  partions = psutil.disk_partitions()
  dev_to_mnt_point_dict = {}
  dev_to_disk_space = {}
  devices = []
  mount_points = []
  output = {}
  for partion in partions:
    dev_to_mnt_point_dict[partion.device] = partion.mountpoint
  for dev, mnt_point in dev_to_mnt_point_dict.iteritems():
    usage = psutil.disk_usage(mnt_point)
    total_disk = usage.total
    usage_percent = usage.percent
    mnt_point_dict = {}
    disk_dict = {}
    used_per_dict = {}
    mnt_point_dict['mount_point'] = mnt_point  
    disk_dict['Total_disk'] = kb_to_gb(total_disk)
    used_per_dict['Percent_used'] = usage_percent
    disk_stats = [mnt_point_dict,disk_dict,used_per_dict]
    dev_to_disk_space['DeviceID: '+dev] = disk_stats
  return dev_to_disk_space


#1) for getting DNS Domain Name 


def get_dna():
    name = subprocess.check_output("hostname | cut -d'.' -f1", shell=True)
    return name
#var1 = get_dna()





#2) for getting DNS Host Name 
def get_dom():
    nam = subprocess.check_output("hostname | cut -d'.' -f2", shell=True)
    return nam
#va1 = get_dom()


# 3)For getting manufacture details of the current running system

def get_mani():
      manuf = subprocess.check_output("dmidecode | grep Manufacturer | sed -n '1p'| awk '{print$2,$3}'", shell=True)
      return manuf
#var2 = get_mani()



# 5)For getting model of the current running system

def get_mod():
       model = subprocess.check_output("dmidecode | grep UUID",shell=True)
       return model
#var3 = get_mod()



# 5) For getting the number of logical processors

def get_proc1():
       totl = psutil.cpu_count()
       return totl
#var4 = get_proc1()



# 6) For getting the Number of processers in system

def get_proc2():
       physical = psutil.cpu_count(logical=False)
       return physical
#var5 = get_proc2()



#7) For getting operating system description

def get_des():
       dis = platform.platform()
       return dis
#var6 = get_des()



# 8) For getting productname

def get_pro():
       a = subprocess.check_output("dmidecode | grep Product | head -1 | awk '{print$3}'", shell=True)
       return a
#var7 = get_pro()



# 9) For getting Vendor of the system

def get_vend():
      b = subprocess.check_output("dmidecode | grep Vendor", shell=True)
      return b
#var8 = get_vend()




# 10) for getting Version

def get_ver():
       c = subprocess.check_output("dmidecode | grep Version | sed -n '2p'", shell=True)
       return c
#var9 = get_ver()

# 11) For getting processor

def get_pr():
      d = platform.processor()
      return d
#var10 = get_pr()


#12) For getting description

def get_desc_nic():
       a = subprocess.check_output("lshw -class network | grep description| awk '{print$2,$3}'", shell=True)
       return a
#var102 = get_desc_nic()




#13)For getting systemos

def get_os():
      Description = platform.platform()
      Machine = platform.machine()
      Processor = platform.processor()
      SystemOS = platform.system()
      Release = platform.release()
      Version = platform.version()
      x = platform.linux_distribution()
      y = x[0]
      full = [{'Description':Description, 'ProductName':y, 'Machine':Machine, 'Processor':Processor, 'System OS':SystemOS, 'Release':Release}]
      #sys = platform.system()
      return full
#var11 = get_os() 



#14) For getting name

def get_name():
      a = subprocess.check_output("lshw -class network | grep name| awk '{print$3}'", shell=True)
      return a
#var103 = get_name()



#15)For getting ip address 

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

#ip_Address = get_ip_address('eth0')



def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]



#16) For getting the dhcp-server ip address
def get_dhc():
  aa = subprocess.check_output("cat /var/lib/dhclient/dhclient.leases | grep server-identifier | awk '{print$3}'", shell=True)
  return aa
#vari = get_dhc()


#17) For getting netmask from nics

def get_netmask(ifname):
  #  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    addrs = netifaces.ifaddresses(ifname)
    ipinfo = addrs[socket.AF_INET][0]
#    print ipinfo
    netmask = ipinfo['netmask']
    return netmask


#18) For getting FQDN

def get_fqdn():
    fqdn = socket.getfqdn()
    return fqdn
# FQD_name = get_fqdn() 
# #print "Fully Qualified Domain Name:", FQD_name
# netmask_Addr=get_netmask('eth0')
# ip_mac_Address = getHwAddr('eth0')
# val=netifaces.interfaces()
# value=netifaces.ifaddresses(val[0])


def get_softwares_info():
  cmd = "yum list installed | sed -e '1,/Installed/d'"
  list_of_sw = subprocess.check_output(cmd,shell=True)
  software_to_version = {}
  software_to_vendor = {}
  software_to_description = {}
  software_to_version_vendor = {}
  softwares = []
  return_software_list = []
  for i in list_of_sw.split('\n'):
    tmp_list = i.split()
    if len(tmp_list) == 3:
      softwares.append(tmp_list[0])
      software_to_vendor[tmp_list[0]] = tmp_list[2]
      software_to_version[tmp_list[0]] = tmp_list[1]
  for software in softwares:
           version_vendor_list = []
           software_details_dict = {}
           # version_vendor_list = [{'version':software_to_version[software]},{'vendor':software_to_vendor[software]}]
           # software_to_version_vendor['product_name: ' +  software]=version_vendor_list
           software_details_dict['ProductName:'] = software
           software_details_dict['Version:'] = software_to_version[software]
           software_details_dict['Vendor'] = software_to_vendor[software]
           return_software_list.append(software_details_dict)
  return return_software_list



# #19)getting softwares that are installed on the system list

# cmd = "yum list installed | sed -e '1,/Installed/d'"

# list_of_sw = subprocess.check_output(cmd,shell=True)
# software_to_version = {}
# software_to_vendor = {}
# software_to_description = {}
# software_to_version_vendor = {}
# softwares = []
# for i in list_of_sw.split('\n'):
#         tmp_list = i.split()
#         if len(tmp_list) == 3:
#                 softwares.append(tmp_list[0])
#                 software_to_vendor[tmp_list[0]] = tmp_list[2]
#                 software_to_version[tmp_list[0]] = tmp_list[1]

# for software in softwares:
#         version_vendor_list = []
#         version_vendor_list = [{'version':software_to_version[software]},{'vendor':software_to_vendor[software]}]
#         software_to_version_vendor['product_name: ' +  software]=version_vendor_list


# 20)Getting date and time

def get_tm():
       a = datetime.datetime.now()
       return str(a)
var100 = get_tm()


#21) For getiing family-type of the system
def get_fami():
       a = subprocess.check_output("dmidecode | grep Family", shell=True)
       return a
#var101 = get_fami()




# allcontent= {'SystemType':var10,'ReportDateTime':var100,'DomainName':va1,'Disks':dev_to_disk_space,'SystemFamily':var101,'DNSHostName':var1,'Manufacturer':var2,'Model': var3,'NumberOfLogicalProcessors':var4,'NumberOfProcessors': var5,'OperatingSystem':[{'Description':var6,'ProductName':var7,'Vendor':var8,'Version':var9,'System OS':var11}], 'Nics':[{'IPAddress':ip_Address,'Description':var102,'DHCPServerIPAddress':vari,'DNSDomain':FQD_name,'MACAddress':ip_mac_Address,'Name':var103,'SubnetMask':netmask_Addr}]}

# keylist = allcontent.keys()
# keylist.sort()
# for key in keylist:
# 	print "%s: %s" "\n"% (key, allcontent[key])
# #print \n
# #print json.dumps(keylist, indent=4)


# all = {'Softwares':software_to_version_vendor}
# print json.dumps(all, indent=4)

