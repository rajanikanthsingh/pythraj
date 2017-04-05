#!/usr/bin/python
import json
file_handler = open('agentconfig.json','w+')
file_data = file_handler.read()
new_data = {
  "Inventory_fetch":"50",
  "Network_functions":"50",
  "remoteconnections":"50",
  "all_total_disks_memory_available":"50",
  "all_total_disks_memory_used_perc":"50",
  "all_total_disks_memory_used":"50",
  "avg_cpu_usage_percent":"50",
  "avg_disk_Bytes_Read":"50",
  "avg_disk_Bytes_Write":"50",
  "avg_disk_ReadBytes_sec":"50",
  "avg_disk_reads_sec":"50",
  "avg_disk_WriteBytes_sec":"50",
  "avg_disk_write_sec":"50",
  "avg_IoTime":"50",
  "avg_MergedReadCount":"50",
  "avg_MergedWriteCount":"50",
  "avg_nics_packets_recive":"50",
  "avg_nics_packets_sent":"50",
  "avg_nics_recive_bytes":"50",
  "avg_nics_sent_bytes":"50"

}
file_handler.truncate()
json.dump(new_data,file_handler)
file_handler.close()

