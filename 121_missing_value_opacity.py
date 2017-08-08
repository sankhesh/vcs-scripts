#!/usr/bin/env python

import vcs
import cdms2

f = cdms2.open(vcs.sample_data + "/clt.nc")
s = f("clt")
x = vcs.init()
x.plot(s)
s2 = cdms2.MV2.masked_greater(s, 50.)
gm = x.createboxfill()
gm.missing = [50, 50, 50, 50]
x.plot(s2, gm)
x.png('121_boxfill_mask_opacity_' + str(gm.missing[3]))
