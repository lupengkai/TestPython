from PIL import Image, ImageFilter

im = Image.open('test.png')

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
