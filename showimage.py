from PIL import Image, ImageDraw, ImageFont
from time import sleep as s
import requests



def font_size(name : str):
    return int(40 - len(name))

def create_image(av, rep, username):
    size1 = (500, 100)
    size2 = (92,92)

    back = Image.new('RGBA', size1, (44, 47, 51))
    avatar = Image.open(requests.get(av, stream=True).raw)

    font = ImageFont.truetype("arial.ttf", font_size(username))
    avatar = avatar.resize(size2)

    t = ImageDraw.Draw(back)
    t.text((150, (50 - (font_size(username) / 2))),
    str(username) + ": " + str(rep), fill=(255, 255, 255), font=font)

    back.paste(avatar, (4,4))
    back.save('result.png')
    s(0.9)