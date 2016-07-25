#!/usr/bin/python

import os
from PIL import Image, ImageDraw, ImageFont
from datetime import date
from shutil import copyfile

cache_path = os.path.expanduser("~/.cache/today.txt/")
text_path = os.path.expanduser("~/Dropbox/today.txt/")

font = ImageFont.truetype("/usr/share/fonts/OTF/FiraSans-UltraLight.otf", size=30)

black = (0,0,0,0)
space_cadet = (29, 41, 81, 255)
eerie_black = (27, 27, 27, 255)

dutch_white = (243, 229, 171, 255)
cardinal_red = (196, 30, 58, 255)
crimson = (220, 20, 60, 255)
ash_grey = (178, 190, 181, 255)

background_color = eerie_black
text_color = ash_grey

def render_image(text):
    img = Image.new(mode='RGBA', size=(1,1), color=background_color)
    draw = ImageDraw.Draw(img)
    size = draw.textsize(text,font=font)
    img = img.resize(size)
    draw = ImageDraw.Draw(img)
    draw.text((0,0), text, font=font, fill=text_color)
    img.save(cache_path + "image.png")

def set_wallpaper():
    os.system("setroot --bg-color '#1B1B1B' -c " + cache_path + "image.png")

def rgba2hex(rgba_tuple):
    return('#%02x%02x%02x' % rgba_tuple[0:3])

def today_file():
    filename = date.today().isoformat() + ".txt"
    if not os.path.exists(text_path + filename):
        copyfile(cache_path + "template.txt", text_path + filename)
    return(text_path + filename)

def main():
    path = today_file()
    with open(path) as f:
        text = f.read()
    render_image(text)
    set_wallpaper()

if __name__ == "__main__":
    main()
