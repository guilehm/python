from PIL import Image

frederico = Image.open('dog.jpg')
print(frederico)
print(frederico.height)
print(frederico.width)
print(dir(frederico))
print(frederico.filename)
print(frederico.format)
print(frederico.format_description)
