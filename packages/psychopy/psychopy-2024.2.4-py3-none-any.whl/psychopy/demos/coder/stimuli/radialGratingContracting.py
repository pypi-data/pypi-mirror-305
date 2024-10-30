#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo: Contracting radial grating
"""

from psychopy import visual, event, core

win = visual.Window([800, 800])
globalClock = core.Clock()

# Make two wedges (in opposite contrast) and alternate them for flashing
radialGrating = visual.RadialStim(win, tex='sinXsin', color=1, size=1,
    visibleWedge=[0, 360], radialCycles=4, angularCycles=0,
    autoLog=False)  # this stim changes too much for autologging to be useful

t = 0
contractRate = 0.01  # cycles per sec
while not event.getKeys():
    t = globalClock.getTime()
    radialGrating.radialPhase -= contractRate
    radialGrating.draw()
    win.flip()

win.close()
core.quit()

# The contents of this file are in the public domain.
