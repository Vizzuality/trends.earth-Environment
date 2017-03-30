from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
import logging

from gefcore.runner import run

logging.basicConfig(
    level='WARN',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)

run(sys.argv[1])
