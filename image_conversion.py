from PIL import Image
import os
import glob

images = glob.glob('images/*.tiff')

if not os.path.isdir('fixed_images'):
    os.mkdir('fixed_images')

new_size = (128, 128)

for image in images:
    im = Image.open(image)
    reformat_im = im.convert("RGB").rotate(-90).resize(new_size)
    reformat_im.save(f'fixed_images/{file}.jpeg')

# NEED TO FIGURE OUT HOW TO KEEP THE OG NAME WHILE CHANGING IT TO JPEG
# I COULD ALSO JUST DO SOME ITERATIVE NAME LIKE i = 0 +1, AND JUST CHANGE IT TO Image1, Image2, ETC... BUT
# I LIKE THE FIRST OPTION BETTER AS IT IS CLEANER.
