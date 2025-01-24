from PIL import Image
from pathlib import Path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-ftype')
files = list(Path('.').glob('*.' + parser.parse_args().ftype))
for file in files:
    img=Image.open(file.name).resize((50,50))
    img.show()