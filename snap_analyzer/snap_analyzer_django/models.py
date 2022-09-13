from django.db import models


class GeneralCluster(models.Model):
    serial_number_cluster = models.CharField(max_length=10)
    date_timestamp = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    code_level = models.CharField(max_length=40)
    number_of_enclosure = models.IntegerField()


class EnclosureModel(models.Model):
    serial_number_cluster = models.CharField(max_length=10)
    date_timestamp = models.CharField(max_length=40)
    id_enclosure = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    temperature = models.CharField(max_length=40)
    total_PSUs = models.CharField(max_length=40)
    online_batteries = models.IntegerField()
    product_MTM_enclosure = models.CharField(max_length=40)
    serial_number_enclosure = models.CharField(max_length=40)
    status_enclosure = models.CharField(max_length=40)
    online_PSUs = models.CharField(max_length=40)
    drive_slots = models.CharField(max_length=40)
    fault_LED = models.CharField(max_length=40)
    identify_LED = models.CharField(max_length=40)
    total_canisters = models.CharField(max_length=40)
    online_canisters = models.CharField(max_length=40)
    id_node_left = models.CharField(max_length=40)
    id_node_right = models.CharField(max_length=40)


class NodeModel(models.Model):
    serial_number_cluster = models.CharField(max_length=10)
    date_timestamp = models.CharField(max_length=40)
    serial_number_enclosure = models.CharField(max_length=40)
    id_node = models.CharField(max_length=40)
    name_node = models.CharField(max_length=40)
    status_node = models.CharField(max_length=40)
    service_IP_address = models.CharField(max_length=40)
    IO_group_id_node = models.CharField(max_length=40)

class DriveModel(models.Model):
    serial_number_cluster = models.CharField(max_length=10)
    serial_number_enclosure = models.CharField(max_length=10)
    date_timestamp = models.CharField(max_length=40)
    drive_id = models.CharField(max_length=40)
    drive_status = models.CharField(max_length=40)
    drive_use = models.CharField(max_length=40)
    capacity = models.CharField(max_length=40)
    drive_slot_id = models.IntegerField()
    id_enclosure = models.CharField(max_length=40)
    vendor_id = models.CharField(max_length=40)
    product_id = models.CharField(max_length=40)
    transport_protocol = models.CharField(max_length=40)
    FRU_part_number = models.CharField(max_length=40)
    FRU_identity = models.CharField(max_length=40)
    mdisk_id = models.CharField(max_length=40)
    mdisk_name = models.CharField(max_length=40)
    firmware_level = models.CharField(max_length=40)