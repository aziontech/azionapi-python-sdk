# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from services.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from services.model.create_resource_request import CreateResourceRequest
from services.model.create_service_request import CreateServiceRequest
from services.model.resource_detail import ResourceDetail
from services.model.resource_response import ResourceResponse
from services.model.resource_response_with_total import ResourceResponseWithTotal
from services.model.service_response import ServiceResponse
from services.model.service_response_with_totals import ServiceResponseWithTotals
from services.model.update_resource_request import UpdateResourceRequest
from services.model.update_service_request import UpdateServiceRequest
from services.model.variable import Variable
