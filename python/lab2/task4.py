from PIL import Image, ImageDraw
for i in range(3):
    img = Image.new('RGBA', (100, 100), 'white')
    draw = ImageDraw.Draw(img)
    draw.line((0, 0, 100, 0), fill='blue', width=5)
    draw.line((100, 0, 100, 100), fill='blue', width=5)
    draw.line((0, 0, 0, 100), fill='blue', width=5)
    draw.line((0, 100, 100, 100), fill='blue', width=5)
    draw.text((47,45),str(i+1),fill='red')
    img.show()