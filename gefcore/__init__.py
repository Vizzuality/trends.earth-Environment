"""The GEF CORE Module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import logging
import base64
import json

from gefcore.runner import run

params = {}
if len(sys.argv) > 1:
    query = sys.argv[1][1:]
    params = base64.b64decode(query)
    params = params.decode('utf-8')
    params = json.loads(params)

run(params)
