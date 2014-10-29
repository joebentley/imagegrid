#!/usr/local/bin/python

import argparse, os
from PIL import Image

"""
grid.py [-h] [-t filetype] [-o output_file] path_to_image number_of_lines

Takes an image specified in path_to_image, and outputs a new copy of the
image with a black square grid overlayed on top of it. The file will be
saved with the same format as the input file by default, unless specified
with -t. The output file will be the input filepath with '_grid' appended
unless specified with -o.

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
    parser.add_argument('-o', nargs=1, metavar='output_filename', default='',
                        help='Name to save output image as')
    return parser.parse_args()

def main():
    args = parseArgs()
    im = Image.open(args.path)

    nVert = args.ylines # No. vert lines

    # Sample up the size of the image for even devisions, maintaining ratio
    # If we didn't do this, then some squares would be bigger than others due
    # to due to uneven numbers of pixels between squares
    ratio = im.size[0] / im.size[1]
    im = im.resize((im.size[0] * nVert / 10, im.size[1] * nVert / 10))

    pix = im.load() # Load image pixels for editing

    w = im.size[0] / nVert # Space between each line
    nHoriz = im.size[1] / w # No. horizontal lines

    # Draw vertical lines by drawing pixels at every y value at each
    # x value that is a multiple of the width of a single square
    for x in range(1, nVert):
        for y in range(0, im.size[1]):
            pix[x * w - 1, y] = (0, 0, 0)

    # Now draw the horizontal lines across the screen...
    for y in range(1, nHoriz + 1):
        for x in range(0, im.size[0]):
            pix[x, y * w] = (0, 0, 0)

    path, extension = os.path.splitext(args.path)

    # Save with user-specified output name
    if args.o and not args.t:
        im.save(args.o[0] + extension)
        return
    elif args.o and args.t:
        im.save(args.o[0] + '.' + args.t[0])
        return

    if not args.t:
        im.save(path + '_grid' + extension)
    else:
        im.save(path + '_grid.' + args.t[0])

if __name__ == "__main__":
    main()
