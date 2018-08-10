import os

from PIL import Image, ImageDraw, ImageFont

frederico = Image.open("dog_rotate90.jpg")
print(frederico)
print(frederico.height)
print(frederico.width)
print(dir(frederico))
print(frederico.filename)
print(frederico.format)
print(frederico.format_description)

frederico.rotate(90).save("dog_rotate90.jpg")

im = Image.new("RGBA", (200, 200), "white")
draw = ImageDraw.Draw(im)
draw.text((20, 150), "Hello", fill="purple")
fonts_folder = "FONT_FOLDER"
arial_font = ImageFont.truetype(os.path.join(fonts_folder, "arial.ttf"), 32)
draw.text((100, 150), "Howdy", fill="gray", font=arial_font)
im.save("text.png")
