#!/usr/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/logic.braiiin.com/logic")
sys.path.insert(0,"/var/www/logic.braiiin.com")

from run import app as application
