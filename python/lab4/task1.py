from moviepy.editor import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('movie')
parser.add_argument('start')
parser.add_argument('finish')
parser.add_argument('new_movie')
clip = VideoFileClip(parser.parse_args().movie)
clip = clip.subclip(parser.parse_args().start, parser.parse_args().finish)
clip.write_videofile(parser.parse_args().new_movie)