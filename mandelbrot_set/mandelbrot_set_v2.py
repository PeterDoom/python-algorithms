from PIL import Image
from numpy import complex, array
import colorsys
import argparse
import progressbar

WIDTH = 500
img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))

# TODO FOR EVERY ROW OF THE IMAGE CALCULATE THE MANDLEBROT FORMULA, MAKE IT CONCURRENT/MULTITHREADED
