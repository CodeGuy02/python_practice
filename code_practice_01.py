import os
import json

from PIL import Image

from numpy import *
from numpy import random

import urllib, urlparse


Image.open('image_01.jpg').convert('L')

url = 'http://www.-----'
c = urllib.urlopen(url)
j = json.loads(c.read())

