import flake8
import unsafe
from pathlib import Path
import sys
from uuid import uuid1 as U1
import mccabe
from uuid import uuid3 as U3, uuid4 as U4

from autopep8 import token, standard_deviation, warnings
import os, functools, collections

def hello():
    pass
