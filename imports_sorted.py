import collections
import functools
import os
import sys
from pathlib import Path
from uuid import (
    uuid1 as U1,
    uuid3 as U3,
    uuid4 as U4
)

import flake8
import mccabe
from autopep8 import (
    standard_deviation,
    token,
    warnings
)

import unsafe


def hello():
    pass
