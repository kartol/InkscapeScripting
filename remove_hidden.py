# The following imports are provided for user convenience.
from math import *
from random import *
from inkex.paths import Arc, Curve, Horz, Line, Move, Quadratic, Smooth, TepidQuadratic, Vert, ZoneClose
from simpinkscr import *

for layer in all_layers():
    if 'style' in layer._inkscape_obj.attrib and 'display:none' in layer._inkscape_obj.attrib['style']:
        layer.remove()
