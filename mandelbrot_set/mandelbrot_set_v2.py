from PIL import Image
from numpy import complex, array
import colorsys
import argparse
import progressbar
from multiprocessing import Pool

WIDTH = 500
IMAGE_ARRAY = []

img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()
p = Pool(processes=10)


def calculate_set(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 500):
        if abs(c) > 2:
            return create_pxl(i)
        c = c * c + c0
    return 0, 0, 0


def create_pxl(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


def build_image(image_size_x, image_size_y):
    for x in range(image_size_x):
        pixels[x, image_size_y] = calculate_set((x - (0.75 * WIDTH)) / (WIDTH / 4),
                                                (image_size_y - (WIDTH / 4)) / (WIDTH / 4))


for height in range(img.size[1]):
    IMAGE_ARRAY.append(height)

result = p.map(build_image())

