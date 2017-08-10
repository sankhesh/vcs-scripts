#!/usr/bin/env python

import cdat_info
import cdms2
import os
import vcs

smpl_prfx = cdat_info.get_sampledata_path()
fnm = os.path.join(smpl_prfx, 'clt.nc')
f = cdms2.open(fnm)
s = f("clt")
x = vcs.init()
x.plot(s, "default", "isoline", bg=True)
x.png("iso", width=1200, height=1090, units="pixels")
