#!/usr/bin/python
from netaddr import IPNetwork

def next_subnet(subnet, index):
    return IPNetwork(subnet).next(index)
