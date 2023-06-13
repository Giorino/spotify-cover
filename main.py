from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



path = "image.jpg" #the image that you choose
color = (251, 234, 211) #color of the text
text = "text" #the text

try: 
    img = Image.open(path)
    width, height = img.size
    if img.size[0] != img.size[1]:
        if width < height:
            area = (0, 0, width, width)
            img = img.crop(area)
            width, height = img.size
            myFont = ImageFont.truetype('Montserrat-Bold.ttf', int(width / 7.5))
            I1 = ImageDraw.Draw(img)
            I1.text((width / 15, height - 2.2 * (height / 10)), text, font = myFont, fill = color)
            img.show()
        if width > height:
            area = (0, 0, height, height)
            img = img.crop(area)
            width, height = img.size
            myFont = ImageFont.truetype('Montserrat-Bold.ttf', int(width / 7.5))
            I1 = ImageDraw.Draw(img)
            I1.text((width / 15, height - 2.2 * (height / 10)), text, font = myFont, fill = color)
            img.show()
    else:
        myFont = ImageFont.truetype('Montserrat-Bold.ttf', int(width / 7.5))
        I1 = ImageDraw.Draw(img)
        I1.text((width / 15, height - 2.2 * (height / 10)), text, font = myFont, fill = color)
        img.show()

          
    #Saved in the same relative location
    img.save("cropped_picture.jpg") 

except IOError:
    pass