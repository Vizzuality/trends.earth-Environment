"""The GEF CORE Module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import logging

from gefcore.runner import run

params = {}
if len(sys.argv) > 1:
    query = sys.argv[1]
    for item in query.rsplit('&'):
        parts = item.rsplit('=')
        params[parts[0]] = parts[1]
run(params)
