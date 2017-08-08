#!/usr/bin/env python

# J-Y Peterschmitt - LSCE - 09/2011 - pmip2web@lsce.ipsl.fr

# Test the use of hatches and patterns in the isofill
# and fill area graphics methods

# Import some standard modules
from os import path

# Import what we need from CDAT
import cdms2
import vcs

# Some data we can plot from the 'sample_data' directory
# supplied with CDAT
data_file = 'tas_ccsr-95a_1979.01-1979.12.nc'
var_name = 'tas'
# data_file = 'clt.nc'
# var_name = 'clt'

# Zone that we want to plot
#
# NOTE: the (latmin, latmax, lonmin, lonmax) information HAS TO be the
# same in the variable, the 'isof' isofill method and the 2 'cont_*'
# continents plotting methods! Otherwise, the data will not match the
# continents that are plotted over it...
(latmin, latmax, lonmin, lonmax) = (-90, 90, -180, 180)

# Use black on white continents (nicer with black and white plots) i.e
# we plot a 'large' white continent outline over the data, and then a
# smaller 'black' continent outline
bw_cont = False
# bw_cont = True

# Read one time step (the first one) from the data file
# and explicitely specify the lat/lon range we need. cdms2
# will retrieve the data in the order we want, regardless of the way
# it is stored in the data file
f = cdms2.open(path.join(vcs.sample_data, data_file))
v = f(var_name, time=slice(0, 1), latitude=(latmin, latmax),
      longitude=(lonmin, lonmax, 'co'), squeeze=1)
# v = f(var_name)
f.close()

# Initialize the graphics canvas
x = vcs.init()
x.setantialiasing(0)

x.setcolormap("rainbow")

# Create the isofill method
isof = x.createboxfill('test_hatch')
isof.boxfill_type = "custom"
# isof.datawc(latmin, latmax, lonmin, lonmax)
# isof.levels = [220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320]
isof.levels = [290, 300]
isof.fillareastyle = 'hatch'
# isof.fillareacolors = [241, 241, 241, 241, 241]  # All black
isof.fillareacolors = [10, 20, 30, 40, 50, 60, 70, 80, 90, 99, 45]  # Colors
# isof.fillareacolors = [50]  # Colors
# isof.fillareacolors = [242, 242, 242, 242]  # Colors
# isof.fillareaindices = [1, 2, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12]
isof.fillareaindices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# isof.fillareaindices = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# isof.fillareaindices = [4]
# isof.fillareaindices = [16, 19, 3, 4, 1, 2, 3, 4]
isof.fillareaopacity = [60, 30, 55, 63, 100, 20, 40, 50, 80, 60]
# isof.fillareapixelspacing = [10, 10]
# isof.fillareapixelscale = 10.0

boxf = x.createboxfill('test_solid')
boxf.boxfill_type = "custom"
boxf.levels = [220, 230]
boxf.fillareastyle = "solid"
boxf.fillareacolors = [99]

# Define some graphics methods for plotting black on white continents
if bw_cont:
    cont_black = x.createcontinents('black')
    cont_black.datawc(latmin, latmax, lonmin, lonmax)
    cont_black.linecolor = 241
    cont_black.linewidth = 2
    cont_white = x.createcontinents('white')
    cont_white.datawc(latmin, latmax, lonmin, lonmax)
    cont_white.linecolor = 240
    cont_white.linewidth = 6

    cont_type = 0  # Do not plot the default continents
else:
    cont_type = 1

# Plot the test data
#
# We have to make sure the data and the continents are plotted at the
# same place ('data' area) on the canvas, by using the same template!
# It's even better if we can use for the continents a template that
# will only plot the data area (the priority of the other elements of
# the canvas is set to zero)
tpl = x.createtemplate('tpl', 'default')
# x.plot(v, boxf, tpl, continents=cont_type)
x.plot(tpl, isof, v, continents=cont_type)
if bw_cont:
    tpl_data = x.createtemplate('tpl_data', 'default_dud')  # plots only data area
    x.plot(tpl_data, cont_white)
    x.plot(tpl_data, cont_black)

# Create a test plot for listing all the hatches and patterns
style_list = []
index_list = []
col_cycle = [243, 248, 254, 252, 255]
nb_cols = len(col_cycle)
color_list = []
x_list = []
y_list = []
txt_x_list = []
txt_y_list = []
txt_str_list = []

# shear_x = .05
shear_x = .0
# for j, style in enumerate(['hatch']):
for j, style in enumerate(['hatch', 'pattern']):
    slide_y = j * .4
    for i in range(20):
        slide_x = i * 0.04
        x1, y1 = (.05 + slide_x, .25 + slide_y)
        x2, y2 = (.08 + slide_x, .45 + slide_y)

        # Add (sheared) rectangles to the list of positions
        # NOTE: no need to close the fill area. Giving 4 vertices
        #       for getting a filled rectangle is enough
        x_list.append([x1, x2, x2 + shear_x, x1 + shear_x])
        y_list.append([y1, y1, y2, y2])

        style_list.append(style)
        # Hatches/Patterns indices have to be in 1-20 range
        index_list.append(i % 20 + 1)
        col_idx = col_cycle[i % nb_cols]
        color_list.append(20 + i * 10)

        # Annotations
        txt_x_list.append(x1 + 0.015)
        txt_y_list.append(y1 - 0.015)
        txt_str_list.append('%s = %i  -  Color = %i' %
                            (style, i + 1, col_idx))

# Create the fill area and the text annotations
fill_test = x.createfillarea('fill_test')
fill_test.style = style_list
fill_test.index = index_list
fill_test.color = color_list
fill_test.x = x_list
fill_test.y = y_list
fill_test.pixelspacing = [10, 10]
fill_test.pixelscale = 10

fill_info = x.createtext('fill_info')
fill_info.angle = 45
fill_info.height = 12
fill_info.color = 241  # Black
fill_info.string = txt_str_list
fill_info.x = txt_x_list
fill_info.y = txt_y_list

# Create a title
plot_title = x.createtext('plot_title')
plot_title.height = 40
plot_title.string = ['Testing hatches and patterns in VCS/CDAT']
plot_title.x = [.01]
plot_title.y = [.9]

# # Initialize and use a second graphics canvas
# y = vcs.init()
# y.setcolormap("rainbow")
# y.plot(plot_title)
# y.plot(fill_test)
# y.plot(fill_info)

# Save the plots
x.interact()
x.pdf('test_fillarea', textAsPaths=False)
x.png('test_fillarea')
# y.pdf('test_fillarea_list', textAsPaths=False)
# y.png('test_fillarea_list')

# Note: depending on the version of CDAT, text may not resize
#       correctly when creating a bigger png
# x.png('test_fillarea_big', width=3*11, height=3*8)
# y.png('test_fillarea_list_big', width=3*11, height=3*8)

# The end
