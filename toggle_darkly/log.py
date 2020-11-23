#!/usr/bin/env python3

"""
Copyright (c) 2020, Gaven Royer
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Core logging utilities for A Toggle Darkly
"""

import logging
from pathlib import Path
from typing import Dict, Any

SYSTEMD_SUPPORT: bool = False
try:
    from systemd.journal import JournalHandler
    SYSTEMD_SUPPORT = True

except ImportError:
    pass

from logging import handlers

LOG_FILE_PATH = Path.home() / '.var' / 'log' / 'toggle-darkly'

VERBOSITY_LEVELS = {
    0: logging.WARNING,
    1: logging.INFO,
    2: logging.DEBUG
}

def get_main_logger():
    """ Returns a main logger object for use by the Gtk.Application.

    Should not be used by normal applications.

    Returns:
        :logging.Logger: The logger for the main application
    """

    # Use verbose debug logging for now.
    console_loglevel = VERBOSITY_LEVELS[2]
    file_loglevel = VERBOSITY_LEVELS[2]

    console_fmt = logging.Formatter(
        '%(name)s: %(levelname)s %(message)s')
    file_fmt = logging.Formatter(
        '%(asctime)s - %(name)s: %(levelname)s %(message)s')

    log = logging.getLogger('toggledarkly')

    console_log = logging.StreamHandler()
    console_log.setFormatter(console_fmt)
    console_log.setLevel(console_loglevel)
    log.addHandler(console_log)

    file_log = handlers.RotatingFileHandler(
        LOG_FILE_PATH, maxBytes=(1048576*5), backupCount=5
    )
    file_log.setFormatter(file_fmt)
    file_log.setLevel(file_loglevel)
    log.addHandler(file_log)

    if SYSTEMD_SUPPORT:
        journald_log = JournalHandler()
        journald_log.setLevel(file_loglevel)
        journald_log.setFormatter(console_fmt)
        log.addHandler(journald_log)
    
    log.setLevel(VERBOSITY_LEVELS[2])

    return log
