# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from waf.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from waf.model.waf_domains200 import WAFDomains200
from waf.model.waf_events200 import WAFEvents200
from waf.model.waf_events400 import WAFEvents400
from waf.model.waf_events401 import WAFEvents401
from waf.model.waf_events404 import WAFEvents404
