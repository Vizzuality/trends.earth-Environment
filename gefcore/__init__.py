"""The GEF CORE Module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import logging

from gefcore.runner import run

logging.basicConfig(
    level='DEBUG',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)
params = None
if len(sys.argv) > 1:
    params = sys.argv[1]
run(params)
