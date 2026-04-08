from PIL import Image, ImageFilter

img= Image.open('/Users/sruthy/Downloads/bulbasaur.jpg')
filtered_img= img.filter(ImageFilter.SHARPEN)
filtered_img2= img.convert('L')

filtered_img.save('/Users/sruthy/PyCharmProjects/Test/Images/bulbasaurFilter.jpg')
filtered_img2.save('/Users/sruthy/PyCharmProjects/Test/Images/bulbasaurConvert.png','png')
filtered_img.show()

#print(img.mode)
