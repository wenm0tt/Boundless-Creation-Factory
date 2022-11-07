from context import *

matplotlib.pyplot.style.use('dark_background')

frame_1 = matplotlib.pyplot.subplot()
cGraphics.plotNV(frame_1, resolution = 1000, expression="z**4-1",dynamic_rendering=True)

