#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Part of the PsychoPy library
# Copyright (C) 2002-2018 Jonathan Peirce (C) 2019-2022 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

"""To connect to serial ports, e.g. to send/receive trigger pulses

This is really just a subclass of the Serial class from the pyserial lib, with
added functions for the purpose of detecting triggers.

Also note that to interact with serial port *devices* with APIs such as
photometers etc then you might be better using the psychopy.hardware.SerialDevice
base class.
"""

import time
import serial

"""
Note that py serial.Serial has announced deprecating camelCase for 
snake_case as of version 3.0 but not clear when this will actually 
be removed. We're currently sticking with camelCase since that meets
our own style guide.  
"""


class SerialPort(serial.Serial):
    """
    """
    def waitTriggers(self, triggers=None, maxWait=None):
        """Waits for one of the trigger characters to be detected

        If none of the characters are detected within the maxWait
        then None is returned. Otherwise the value of the detected
        trigger is returned.

        Params
        ------

        """
        if type(triggers) in [bytes, str]:
            triggers = {triggers}
        t0 = time.time()
        # can't just use serial port timeout because check for char
        while maxWait is None or (time.time()-t0 < maxWait):
            chars = self.read(self.inWaiting())
            for thisTrigger in triggers:
                if thisTrigger in chars:
                   return thisTrigger
