#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import TickerManager
from TickerManager import generatePoint
import string

a = [{"name":1}, {"name":2}, {"name":3}]
print time.strftime('[%Y-%m-%d %H:%M:%S]')

a = "%s了，幅度 %s" % ('下', 3.1)
print generatePoint(3.1, 'up')
print (2 - 1) / 2.0
print string.atof('18.2') - string.atof('17.2')