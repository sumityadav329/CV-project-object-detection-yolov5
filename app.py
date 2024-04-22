import sys
from signLanguage.logger import logging
from signLanguage.exception import SignException
logging.info("Welcome to the project")

try:
    a = 7/'0'
except Exception as e:
    raise SignException(e, sys) from e