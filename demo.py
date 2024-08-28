from hate.logger import logging
from hate.exception import HateSpeechException
import sys

try:
    a = 2/0
except Exception as e:
    raise HateSpeechException(e, sys)