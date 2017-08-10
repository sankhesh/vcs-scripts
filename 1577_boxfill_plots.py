#!/usr/bin/env python

import vcs
import cdms2

x = vcs.init()

f = cdms2.open(vcs.sample_data + "/clt.nc")
s = f("clt")

box = x.createboxfill()
box.fillareastyle = "hatch"
box.fillareacolors = [20, 50, 75]
box.fillareaindices = [5, 10, 15]
box.levels = [10, 50, 75, 100]
# box.boxfill_type = "custom"

x.plot(s, box, bg=1)
x.png("boxfill_patterns.png")
