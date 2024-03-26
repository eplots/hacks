#!/usr/bin/env python3
from captcha.image import ImageCaptcha
import random

amount = 99999
count = 10000

while count <= amount:
    image = ImageCaptcha(width = 160, height = 60)
    text = str(count)
    count += 1
    data = image.generate(text)
    image.write(text, (text) + ".png")
