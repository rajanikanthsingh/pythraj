#!/usr/bin/python

# Copyright 2015 Apple.

"""
One time only Programmatic tagging of all L3 networks belonging to GNS LAN support group
"""
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'nia_web.settings'
django.setup()
import time
import logging
import re
from nia_client.device_inventory_client import DeviceInventoryClient
from nia_web_app.models import IpInterface, Network, Device, NetworkAttribute
from nia_utils import network_utility, utility
from django import db
from niings
from django.core.exceptia_web import settons import ObjectDoesNotExist
from location.unlocode import unlocode_manager
from nia_utils.constants import Constants

logger = logging.getLogger('gns_lan_primer')
headers = {'Content-Type': 'application/json'}
dev_inv_client = DeviceInventoryClient(base_url=settings.INVENTORY_BASE_URL, headers=headers, logger=logger)


def __get_networks_for_device(device):
    """
    get networks associated with the device
    :param device:
    :return:
    """
    ip_interfaces = IpInterface.objects.filter(device=device)
    networks_for_device = set()
    for ip_interface in ip_interfaces:
        networks_for_device.add(ip_interface.network)
    return networks_for_device


def __get_devices():
    """
    get all devices where support group contains the name *LAN*
    :return:
    """
    devices = Device.objects.filter(support_group__contains='LAN')
    db.reset_queries()
    return devices


def __process_devices(devices):
    """
    process the devices
    :param devices:
    :return:
    """
    for device in devices:
        # tag un location code
        __add_attribute_unlocode(device)
        # tag site
        __add_attribute_site(device)
        # tag business unit
        __add_attribute_business_unit(device)
        # tag security zone
        __add_attribute_security_zone(device)
        # reset queries when application debug is turned on
        db.reset_queries()


def __add_attribute_unlocode(device):
    """
    tag un location code
    :param device:
    :return:
    """
    network_ids = __get_networks_for_device(device)
    snmp_location = device.snmp_location
    unlocode = None
    # get the first token from the snmp location and use it as the UN location code. Ensure that it is a valid code
    # and exists in the database
    if snmp_location is not None:
        temp_unlocode = snmp_location.split(':')[0].upper()
        unlocode_dto = unlocode_manager.get_un_location_code_by_code(temp_unlocode)
        if unlocode_dto is not None:
            unlocode = unlocode_dto.code
    attribute_dict = {Constants.ATTRIBUTE_ENUM_UNLOCODE: [unlocode]}
    for network_id in network_ids:
        if unlocode is not None:
            logger.info(
                '__add_attribute_unlocode: device %s, network: %s, unlocode: %s' % (device.fqdn, network_id, unlocode))
            __add_attributes_to_network(network_id, attribute_dict)


def __add_attribute_site(device):
    """
    tag site
    :param device:
    :return:
    """
    network_ids = __get_networks_for_device(device)
    snmp_location = device.snmp_location
    site = None
    # get the second token from the snmp location and use it as the site attribute. Ensure that it is a valid site.
    # Use regular expressions to ensure validity. Examples : MR01, MR1, R100, USPAO1 are valid matches
    if snmp_location is not None:
        split_tokens = snmp_location.split(':')
        if len(split_tokens) > 1:
            temp_site = split_tokens[1]
            if re.match('^(([a-zA-Z]{2}\d{2})|([a-zA-Z]{2}\d{1}))$', temp_site) is not None or re.match(
                    '^[a-zA-Z]{1}\d{3}$',
                    temp_site) or re.match(
                '^[a-zA-Z]{5}\d{1}', temp_site):
                site = temp_site

    attribute_dict = {Constants.ATTRIBUTE_ENUM_SITE: [site]}
    for network_id in network_ids:
        if site is not None:
            logger.info('__add_attribute_site: device %s, network: %s, site: %s' % (device.fqdn, network_id, site))
            __add_attributes_to_network(network_id, attribute_dict)


def __add_attribute_business_unit(device):
    """
    tag business unit
    :param device:
    :return:
    """
    network_ids = __get_networks_for_device(device)
    # bail out if the fqdn does not contain ecs or seo.
    if 'ecs' or 'seo' not in device.fqdn:
        return
    # tag business unit with ecs if the device fqdn contains that name
    attribute_dict = {Constants.ATTRIBUTE_ENUM_BUSINESS_UNIT: ['ECS']}
    if 'ecs' in device.fqdn:
        for network_id in network_ids:
            logger.info('__add_attribute_business_unit: device %s, network: %s, business unit: %s' % (
                device.fqdn, network_id, 'ECS'))
            __add_attributes_to_network(network_id, attribute_dict)


def __add_attribute_security_zone(device):
    """
    tag security zone, layer 2 type and application environment
    :param device:
    :return:
    """
    network_ids = __get_networks_for_device(device)

    network_dict = {}
    for network_id in network_ids:
        is_guest_network = False
        is_lab_network = False
        is_security_zone_set = False
        network = Network.objects.get(pk=network_id)

        # tag security zone with wifi if the network comment or device fqdn contains wifi
        if (network.comment is not None and 'wifi' in network.comment.lower()) or ('wifi' in device.fqdn):
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_SECURITY_ZONE, 'Guest')
            is_guest_network = True
            is_security_zone_set = True

        # tag security zone with lab if the network comment or device fqdn contains lab
        if (network.comment is not None and 'lab' in network.comment.lower()) or ('lab' in device.fqdn):
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_SECURITY_ZONE, 'Lab')
            is_lab_network = True
            is_security_zone_set = True

        # tag security zone with ThirdParty if the network comment or device fqdn contains bms
        if (network.comment is not None and 'bms' in network.comment.lower()) or ('bms' in device.fqdn):
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_SECURITY_ZONE,
                                          'ThirdParty')
            is_security_zone_set = True

        # tag security zone with Routing if the prefix length >=30
        if network.prefix_length >= 30:
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_SECURITY_ZONE,
                                          'Routing')
            is_security_zone_set = True

        # tag layer 2 type with wifi if security zone = guest, else Ethernet
        if is_guest_network:
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_LAYER2_TYPE,
                                          '802.11 (WiFi)')
        else:
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_LAYER2_TYPE,
                                          '802.3 (Ethernet)')
        # tag application environment with Development if security zone = lab, else Production
        if is_lab_network:
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_APPLICATION_ENVIRONMENT,
                                          'Development')
        else:
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_APPLICATION_ENVIRONMENT,
                                          'Production')
        # by default tag network as desktop
        if not is_security_zone_set:
            __add_or_append_value_to_dict(network_dict, network_id, Constants.ATTRIBUTE_ENUM_SECURITY_ZONE, 'Desktop')

    for network_id, attribute_dict in network_dict.items():
        logger.info(
            '__add_attribute_security_zone: device %s network %s, attribute_dict %s' % (device.fqdn, network_id, attribute_dict))
        __add_attributes_to_network(network_id, attribute_dict)


def __add_or_append_value_to_dict(network_dict, network_id, attribute_key, attribute_value):
    """
    helper method for populating network dictionary
    :param network_dict:
    :param network_id:
    :param attribute_key:
    :param attribute_value:
    :return:
    """
    if network_id in network_dict:
        network = network_dict[network_id]
        if attribute_key in network:
            network[attribute_key].append(attribute_value)
        else:
            network[attribute_key] = [attribute_value]
    else:
        network_dict[network_id] = {attribute_key: [attribute_value]}


def __add_attributes_to_network(network_id, attribute_dict):
    """
    add attributes to the network
    :return:
    """
    try:
        network = Network.objects.get(pk=network_id)
        if attribute_dict is not None:
            network_attribute_from_db_list = []
            for attribute_key, attribute_values in attribute_dict.items():
                try:
                    network_attribute_from_db = NetworkAttribute.objects.get(network=network, key=attribute_key)

                    # new attribute value is defined. So delete all existing values for this attribute and
                    # recreate the list of values with this new value. Also track the attribute being changed
                    network_attribute_from_db.attribute_values.all().delete()
                    for attribute_value in attribute_values:
                        network_attribute_from_db.attribute_values.create(value=attribute_value)

                    network_attribute_from_db_list.append(network_attribute_from_db)

                    # if source is not defined then edit it
                    if network_attribute_from_db.source is None:
                        network_attribute_from_db.source = Constants.SOURCE_GROOT
                        network_attribute_from_db.save()

                    # ensure override flag
                    if not network_attribute_from_db.override:
                        network_attribute_from_db.override = True
                        network_attribute_from_db.save()

                except ObjectDoesNotExist:
                    # attribute does not exist. Hence create attribute and its value
                    network_attribute_from_db = NetworkAttribute.objects.create(network=network, key=attribute_key,
                                                                                source=Constants.SOURCE_GROOT,
                                                                                override=True)
                    for attribute_value in attribute_values:
                        network_attribute_from_db.attribute_values.create(value=attribute_value)

                    network_attribute_from_db_list.append(network_attribute_from_db)

            # propagate the new value down the hierarchy. Only propagate if the tracked attribute list size is > 0
            if len(network_attribute_from_db_list) > 0:
                network_utility.add_attributes_to_inherited_networks(network, async=False)
    except ObjectDoesNotExist:
        logger.warn("Network %s does not exist" % network_id)


def main():
    """
    :return:
    """
    main_start_time = time.time()
    devices = __get_devices()
    __process_devices(devices)
    logger.info('total time for execution: %s' % (time.time() - main_start_time))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.exception('Failure in gns lan primer')
