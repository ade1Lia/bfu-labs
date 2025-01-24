from moviepy.editor import *
from PIL import Image
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('movie')
parser.add_argument('start')
parser.add_argument('finish')
parser.add_argument('frames')
parser.add_argument('-step', default=10)
args = parser.parse_args()
if not os.path.exists(args.frames):
    os.makedirs(args.frames)
clip = VideoFileClip(args.movie)
clip = clip.subclip(args.start, args.finish)
frames = int(clip.fps * clip.duration)
for i in range(0, frames, int(args.step)):
    frame = clip.get_frame(i * (clip.duration / frames))
    image = Image.fromarray(frame)
    image_new = image.resize((250, 250))
    image_new.save(os.path.join(args.frames, f'{i}.jpg'))
print(f'Extracted frames saved to: {args.frames}')
