import random
from math import sqrt
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
lines=[0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400]
for i in lines:
    draw.line(((i,360),(i,830)), fill='green', width=50)

draw.ellipse((width//3,height//3,width//1.5,height//1.3), fill=(237,118,14))
 
image.show()
del draw