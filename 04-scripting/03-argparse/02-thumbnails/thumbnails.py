import argparse
from pathlib import Path
import sys


def derive_output_name(pattern, input):
    path = Path(input)
    

parser = argparse.ArgumentParser(prog='thumbnail')
parser.add_argument('files', help='Files', nargs='+')
parser.add_argument('--size', help='Size of the thumbnail', default='64x64')
parser.add_argument('--pattern', help='Pattern for output files', default='%b-thumbnail.%x')

args = parser.parse_args()

