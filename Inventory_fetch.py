import Inventory_functions
import Network_Usage
from pprint import pprint
Inventory_list = ['Disks','DNSHostName','Domain','ReportDateTime','Manufacturer','Model','NumberOfLogicalProcessors','NumberOfProcessors','Softwares','OperatingSystem','NICs']
Inventory_list.sort()
value_set = {}
return_dict_all_values = {}

value_set['Disks'] = Inventory_functions.get_disks_info()
value_set['Softwares'] = Inventory_functions.get_softwares_info()
value_set['ReportDateTime'] = Inventory_functions.get_tm()
value_set['Domain'] = Inventory_functions.get_dna()
value_set['Manufacturer'] = Inventory_functions.get_mani()
value_set['Model'] = Inventory_functions.get_mod()
value_set['NumberOfLogicalProcessors'] = Inventory_functions.get_proc1()
value_set['NumberOfProcessors'] = Inventory_functions.get_proc2()
#value_set['SystemFamily'] = Inventory_functions.get_fami()
value_set['DNSHostName'] = Inventory_functions.get_dom()
value_set['OperatingSystem'] = Inventory_functions.get_os()
value_set['NICs'] = Network_Usage.nics_report()
for value in Inventory_list:
        Disks = Inventory_functions.get_disks_info()
	return_dict_all_values[value] = value_set[value]
pprint(return_dict_all_values)
