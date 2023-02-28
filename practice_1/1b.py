import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки
image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                draw.point((x,y),(a,b,c))
                
for x in range(480):
        for y in range(height):
            a = pix[x, y][0]
            b = pix[x, y][1]
            draw.point((x,y),(a,b,0))
for x in range(480,960):
        for y in range(height):
            a = pix[x, y][0]
            draw.point((x,y),(a,0,0))
for x in range(960,1440):
        for y in range(height):
            b = pix[x, y][1]
            draw.point((x,y),(0,b,0))


image.show()
del draw
