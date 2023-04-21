# pipe_guard.py
# -------------
# A decorator to protect against broken pipe errors.
# Utilities like `head` will close their stdin before a stream
# ends, because they only want so much input. This causes a BrokenPipeError
# when a Python process keeps trying to send data.
# See https://docs.python.org/3/library/signal.html#note-on-sigpipe, 

import os
import sys
from functools import wraps

def guard_pipe(fn):
    """A decorator to prevent BrokenPipeErrors.
    """
    @wraps(fn)
    def safe_fn(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
            sys.stdout.flush()
        except BrokenPipeError:
            devnull = os.open(os.devnull, os.O_WRONLY)
            os.dup2(devnull, sys.stdout.fileno())
            sys.exit(1)
    return safe_fn



