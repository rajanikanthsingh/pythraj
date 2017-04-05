import psutil
from pprint import pprint
partions = psutil.disk_partitions()
dev_to_mnt_point_dict = {}
dev_to_disk_space = {}
devices = []
mount_points = []
output = {}

for partion in partions:
  #print partion.device
  dev_to_mnt_point_dict[partion.device] = partion.mountpoint

for dev, mnt_point in dev_to_mnt_point_dict.iteritems():
  usage = psutil.disk_usage(mnt_point)
  total_disk = usage.total
  usage_percent = usage.percent
  mnt_point_dict = {}
  disk_dict = {}
  used_per_dict = {}
  mnt_point_dict['mount_point'] = mnt_point  
  disk_dict['Total_disk'] = total_disk
  used_per_dict['Percent_used'] = usage_percent
  disk_stats = [mnt_point_dict,disk_dict,used_per_dict]
  dev_to_disk_space['DeviceID: '+dev] = disk_stats

#pprint(dev_to_disk_space)
return dev_to_disk_space
