from PIL import Image, ImageDraw
with Image.open('test.jpg') as img:
    draw = ImageDraw.Draw(img)
    draw.text((113,123),'THINK')
    img2=Image.open('test1.jpg').resize((321,313))
    img.paste(img2,(121,331))
    img.show()