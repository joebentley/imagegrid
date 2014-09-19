#!/usr/local/bin/python

import argparse, os, fractions
from PIL import Image

"""
grid.py [-h] [-t filetype] path_to_image number_of_lines

requires Python Imaging Library (PIL) or Pillow
"""

# Parse command line args
def parseArgs():
    parser = argparse.ArgumentParser(description='Take an image and save ' + \
                                                 'a new one with a grid overlaid')
    parser.add_argument('path', metavar='path_to_image',
                        help='Relative path to image')
    parser.add_argument('ylines', type=int, metavar='number_of_lines',
                        help='Number of vertical lines we ' + \
                        'want to split the image into')
    parser.add_argument('-t', nargs=1, metavar='filetype', default='',
                        help='File type to save as, leave blank ' + \
                        'for same type as source file')
    return parser.parse_args()

def main():
    args = parseArgs()
    im = Image.open(args.path)

    nVert = args.ylines # No. vert lines

    # Sample up the size of the image for even devisions, maintaining ratio
    # If we didn't do this, then some squares would be bigger than others due
    # to non-even square widths in pixels
    ratio = im.size[0] / im.size[1]
    im = im.resize((im.size[0] * nVert / 10, im.size[1] * nVert / 10))

    pix = im.load() # Load image pixels for editing

    w = im.size[0] / nVert # Space between each line
    nHoriz = im.size[1] / w # No. horizontal lines

    # Cycle through each x value, cycle down every y value to draw line
    # at x = x * the number of lines on the image
    for x in range(1, nVert):
        for y in range(0, im.size[1]):
            pix[x * w - 1, y] = (0, 0, 0)

    # Now draw the horizontal lines across the screen...
    for y in range(1, nHoriz + 1):
        for x in range(0, im.size[0]):
            pix[x, y * w] = (0, 0, 0)

    path, extension = os.path.splitext(args.path)
    if not args.t:
        im.save('grid_' + path + extension)
    else:
        im.save('grid_' + path + '.' + args.t[0])

if __name__ == "__main__":
    main()