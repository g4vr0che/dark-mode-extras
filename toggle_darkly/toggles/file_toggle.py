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

A toggle for flipping between two config files
"""
from pathlib import Path

from .toggle import Toggle

class FileToggle(Toggle):
    """ A simple toggle that flips between two different config files.

    When dark mode is enabled, installs one version of a config file. When it is
    disabled, replace that config file with a new one. Config files need to be
    set up externally.

    Parameters:
        :str path: The directory where the config files are stored.
        :str main: The main filename for the config file
        :str light: The name of the light-mode configuration file
        :str dark: The name of the dark-mode configuration file
    """

    def __init__(self, path: str, main: str, light: str, dark:str):
        super().__init__()
        self.path = path
        self.main = self.path / main
        self.light = light
        self.dark = dark

    def light_mode(self):
        """ Replace the current main config with the light mode config"""

        try:
            self.main = self.main.rename(self.light)

        except FileNotFoundError:
            return False

        return True

    def dark_mode(self):
        """ Replace the current main config with the dark mode config"""

        try:
            self.main = self.main.rename(self.dark)

        except FileNotFoundError:
            return False

        return True


    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path: str):
        self._path = Path(self._path) / path

    @property
    def main(self) -> Path:
        return self._main

    @main.setter
    def main(self, main: Path):
        self._main = main

    @property
    def light(self) -> Path:
        return self._light

    @light.setter
    def light(self, light: str):
        self._light = Path(self._path) / light

    @property
    def dark(self) -> Path:
        return self._dark

    @dark.setter
    def dark(self, dark: str):
        self._dark = Path(self._path) / dark

