#!/usr/bin/env python

import os
import sys


root_dir = os.path.normpath(
    os.path.join(
        os.path.abspath(sys.argv[0]),
        os.pardir,
        os.pardir,
    )
)
sys.path.insert(0, root_dir)

from pythonwarrior import runner


runner = runner.Runner(sys.argv, sys.stdin, sys.stdout)
runner.run()
