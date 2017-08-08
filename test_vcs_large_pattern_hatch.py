#!/usr/bin/env python
import vcs

canvas = vcs.init(geometry={"width": 100, "height": 100})
canvas.setantialiasing(0)
fillarea = vcs.createfillarea()
# fillarea.x = [[0, .33, .33, 0], [.33, .67, .67, .33], [.67, 1, 1, .67]]
fillarea.x = [0, 1, 1, 0]
fillarea.y = [0, 0, 1, 1]
# fillarea.y = [[0, 0, 1, 1]] * 3
# fillarea.style = ["solid", "pattern", "hatch"]
fillarea.style = ["hatch"]
fillarea.index = [8]
fillarea.pixelspacing = [20, 20]
fillarea.pixelscale = 10.0
# fillarea.color = [50, 50, 50]
fillarea.color = [50]
canvas.plot(fillarea, bg=False)
canvas.pdf("large_pattern_hatch_100x100")
canvas.png("large_pattern_hatch_100x100")
canvas.interact()
