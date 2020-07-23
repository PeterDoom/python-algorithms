from PIL import Image
from numpy import complex, array
import colorsys
import argparse
import progressbar

WIDTH = 500
IMAGE_ARRAY = []

img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))


def calculate_set(x, y):
    pass


def create_pxl(i):
    pass

# TODO FOR EVERY ROW OF THE IMAGE CALCULATE THE MANDLEBROT FORMULA, MAKE IT CONCURRENT/MULTITHREADED
