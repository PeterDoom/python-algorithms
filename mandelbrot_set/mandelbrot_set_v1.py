from PIL import Image
from numpy import complex, array
import colorsys
# import time
import argparse
import progressbar

WIDTH = 1024


def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 500):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c * c + c0
    return 0, 0, 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Argument for Mandelbrot Set script')
    parser.add_argument("-res", "--resolution", required=True, nargs=1,
                        help="Resolution for final image")

    args = parser.parse_args()
    WIDTH = int(args.resolution[0])

    # start_time = time.time()

    img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
    pixels = img.load()

    with progressbar.ProgressBar(max_value=progressbar.UnknownLength) as bar:
        for x in range(img.size[0]):

            # print("%.2f %%" % (x / WIDTH * 100.0))
            for y in range(img.size[1]):
                pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4),
                                          (y - (WIDTH / 4)) / (WIDTH / 4))
            bar.update(+1)

    # print("--- %s seconds ---" % (time.time() - start_time))
    img.show()
