from PIL import Image, ImageDraw
import random as rnd

for i in range(1,10):
    image = Image.open(f'1 ({i}).png')
    image = image.transpose(Image.FLIP_LEFT_RIGHT) #Отразил изображение
    (w, h) = image.size
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    pix = image.load()  # Выгружаем значения пикселей

    for x in range(w):
        for y in range(h):
           r = pix[x, y][0] #узнаём значение красного цвета пикселя
           g = pix[x, y][1] #зелёного
           b = pix[x, y][2] #синего
           sr = rnd.randrange(1,12,1) + r
           sg = rnd.randrange(1,12,1) + g
           sb = rnd.randrange(1,12,1) + b
           draw.point((x, y), (sr, sg, sb)) #рисуем пиксель
               
    idraw = ImageDraw.Draw(image)
    color1 = rnd.randrange(1,15000,1)
    idraw.rectangle((2, 2, w-2, h-2), outline=color1, width=4)

    image.save(f"111/result{i}.png")
    print(f"saved result{i}")
