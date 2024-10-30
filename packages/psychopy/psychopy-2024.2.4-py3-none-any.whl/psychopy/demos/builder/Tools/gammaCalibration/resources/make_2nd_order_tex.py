#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Determine screen gamma using motion-nulling method
of Ledgeway and Smith, 1994, Vision Research, 34, 2727-2740
A similar system had been used early for chromatic isoluminance:
Anstis SM, Cavanagh P. A minimum motion technique for judging equiluminance.
In: Sharpe MJD & LT Colour vision: Psychophysics and physiology. London: Academic Press; 1983. pp. 66-77.

Instructions: on each trial press the up/down cursor keys depending on
the apparent direction of motion of the bars.
"""

from psychopy import visual, core, event, gui, data
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import filters
import numpy as num
import time

"""
Create a single cycle of noise texture, suitable for checking the 
quality of screen linearisation
"""

pixels = 128
win = visual.Window((pixels, pixels), units='pix', allowGUI=True, bitsMode=None)
visual.TextStim(win, text='building stimuli').draw()

win.flip()

globalClock = core.Clock()

# for luminance modulated noise
noiseMatrix = num.random.randint(0, 2, [pixels, pixels])  # * noiseContrast
noiseMatrix = noiseMatrix * 2.0-1  # into range -1: 1
lumGrating = filters.makeGrating(pixels, 0, 1, phase=0)

second_order = visual.GratingStim(
    win, texRes=pixels, mask=None,
    size=2, units='norm',
    tex= (noiseMatrix * (lumGrating/2+0.5))
    )
second_order.draw()
win.flip()
win.getMovieFrame()
win.saveMovieFrames('second_order_tex.png')

low_contrast = visual.GratingStim(
    win, texRes=pixels, mask=None,
    size=2, units='norm',
    tex= lumGrating, contrast=0.2,
    )
low_contrast.draw()
win.flip()
win.getMovieFrame()
win.saveMovieFrames('low_contrast.png')

# The contents of this file are in the public domain.
