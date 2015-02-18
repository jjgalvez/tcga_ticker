__author__ = 'jc'

from pyramid.paster import get_app, setup_logging
import os

here = os.getcwd()
ini = os.path.join(here, 'production.ini')

setup_logging(ini)
application = get_app(ini)