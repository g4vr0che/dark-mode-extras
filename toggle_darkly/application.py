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

The Application class
"""

from gi.repository import Gio, GLib, GObject, Gtk

from . import log

class Application(Gtk.Application):
    """ The main Application for A Toggle Darkly 

    Arguments:
        :str id: The application ID
    """

    def __init__(self, id='in.donotspellitgav.ToggleDarkly'):
        super().__init__(
            application_id=id,
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        GLib.set_application_name('A Toggle Darkly')
        GLib.set_prgname(id)

        self._window = None
        self._log = log.get_main_logger()
    
    # @GObject.Property(type=Window, flags=GObject.ParamFlags.READABLE)
    # def window(self):
    #     """:Window: Main Application Window."""
    #     return self._window

    @GObject.Property(
        type=log.logging.Logger, default=None, flags=GObject.ParamFlags.READABLE)
    def log(self):
        """:logging.Logger: Application-wide logging facility."""
        return self._log


