#!/usr/bin/env python

import vcs
import cdms2

f = cdms2.open(vcs.sample_data + "/clt.nc")
s = f("clt")
x = vcs.init(geometry=[1200, 1200])
isoline = x.createisoline()
# isoline.linetypes = ["dash-dot"]
# isoline.linecolors = [25]
isoline.linewidths = [0.5]

v = [0.5, 1.0]
for i in v:
    isoline.linewidths = [i]
    x.plot(s, isoline, bg=True)
    x.png("isoline_width_" + str(i) + ".png")
