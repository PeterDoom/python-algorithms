import argparse
import threading
from PIL import Image

w = 1024
h = 1024
image = Image.new("RGB", (w, h))
wh = w * h
maxIt = 500  # max number of iterations allowed
# drawing region (xa < xb & ya < yb)
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
xd = xb - xa
yd = yb - ya
numThr = 100


class ManFrThread(threading.Thread):
    def __init__(self, k):
        # k is number of thread
        self.k = k
        threading.Thread.__init__(self)

    def run(self):
        # each thread only calculates its own share of pixels
        for i in range(k, wh, numThr):
            kx = i % w
            ky = int(i / w)
            a = xa + xd * kx / (w - 1.0)
            b = ya + yd * ky / (h - 1.0)
            x = a
            y = b
            for kc in range(maxIt):
                x0 = x * x - y * y + a
                y = 2.0 * x * y + b
                x = x0
                if x * x + y * y > 4:
                    # various color palettes can be created here
                    red = (kc % 8) * 32
                    green = (16 - kc % 16) * 16
                    blue = (kc % 16) * 16
                    # lock.acquire()
                    global image
                    image.putpixel((kx, ky), (red, green, blue))
                    # lock.release()
                    break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Argument for Mandelbrot Set script')
    parser.add_argument("-res", "--resolution", required=True, nargs=1,
                    help="Resolution for final image")

    args = parser.parse_args()
    # w = int(args.resolution[0])
    # h = int(args.resolution[0])

    tArr = []
    for k in range(numThr):  # create all threads
        tArr.append(ManFrThread(k))
    for k in range(numThr):  # start all threads
        tArr[k].start()
    for k in range(numThr):  # wait until all threads finished
        tArr[k].join()
    image.save("MandelbrotFractal.png", "PNG")
    
    # TODO Implement better multithreading logic
