from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys

#logging.info('welcome to the project')

try:
    a = 7/'3'

except Exception as e:
    raise SignException(e, sys) from e 