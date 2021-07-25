#!/usr/bin/python3.6
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = '969caca4707f9950d6bc40c2e8373148bd264e385ed9cf07'