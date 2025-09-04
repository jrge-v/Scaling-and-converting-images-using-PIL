from PIL import Image

im = Image.open("images/white_dog192x192x90CCW.tiff")

print(im.format, im.size, im.mode)
