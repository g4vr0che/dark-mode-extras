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

The base toggle class
"""

class BaseToggle:
    """ A toggle item which can be subclassed to support different toggles

    Allows different types of toggles to run each time dark mode is enabled or
    disabled.
    """

    def __init__(self):
        self._name: str = None
    
    def light_mode(self) -> bool:
        """ Runs each time dark mode is disabled (light mode is enabled)
        
        Returns:
            :bool: Whether the toggle was successful.
        """
        return True
    
    def dark_mode(self) -> bool:
        """ Runs each time dark mode is enabled (light mode is disabled)
        
        Returns:
            :bool: Whether the toggle was successful.
        """
        return True
    
    @property
    def mode(self) -> str:
        return type(self).__name__
    
    @property
    def name(self) -> str:
        """ :str: The name of this toggle."""
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name