# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from edgefirewall.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from edgefirewall.model.create_edge_firewall_request import CreateEdgeFirewallRequest
from edgefirewall.model.edge_firewall import EdgeFirewall
from edgefirewall.model.edge_firewall_response import EdgeFirewallResponse
from edgefirewall.model.links import Links
from edgefirewall.model.list_edge_firewall_response import ListEdgeFirewallResponse
from edgefirewall.model.update_edge_firewall_request import UpdateEdgeFirewallRequest
