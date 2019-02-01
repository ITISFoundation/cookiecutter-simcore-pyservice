#!/bin/python

import os
import sys

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

SUCCESS, FAILURE = 0, 1

if os.environ.get("BOOT_MODE") == "debug":
    # Healthcheck disabled with service is boot with a debugger
    print(SUCCESS)
else:
    print(SUCCESS if urlopen("{host}{baseurl}".format(
        host=sys.argv[1],
        baseurl=os.environ.get("SIMCORE_NODE_BASEPATH", ""))
        ).getcode() == 200
        else FAILURE)
