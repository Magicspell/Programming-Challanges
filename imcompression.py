import pygame
from PIL import Image, ImageFilter
import colorsys
import zlib
import thorpy
import pytesseract




pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

im = Image.open(input('Which image? '))
print(pytesseract.image_to_string(im))

data = pytesseract.image_to_data(im, output_type=pytesseract.Output.DICT)
boxes = len(data['level'])
for i in range(boxes ):
    (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    print(x, y, w, h)

pix = im.load()
width, height = im.size
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Image Compression')
pygame.init()
mainclock = pygame.time.Clock()

hues = []
values = []

def get_2x2(i):
    for w in range(width):
        for h in range(height):
            if w == i and h == i:
                pixel1 = pix[w,h]
            if w == i+1 and h == i:
                pixel2 = pix[w,h]
            if w == i and h == i+1:
                pixel3 = pix[w,h]
            if w == i+1 and h == i+1:
                pixel4 = pix[w,h]
    return pixel1, pixel2, pixel3, pixel4

def avg_2x2(coords):
    pixels = get_2x2(coords)
    hsv1 = colorsys.rgb_to_hsv(pixels[0][0], pixels[0][1], pixels[0][2])
    hsv2 = colorsys.rgb_to_hsv(pixels[1][0], pixels[1][1], pixels[1][2])
    hsv3 = colorsys.rgb_to_hsv(pixels[2][0], pixels[2][1], pixels[2][2])
    hsv4 = colorsys.rgb_to_hsv(pixels[3][0], pixels[3][1], pixels[3][2])
    newhue = (hsv1[0]+hsv2[0]+hsv3[0]+hsv4[0])/4
    rgb1 = colorsys.hsv_to_rgb(newhue,hsv1[1],hsv1[2])
    rgb2 = colorsys.hsv_to_rgb(newhue,hsv2[1],hsv2[2])
    rgb3 = colorsys.hsv_to_rgb(newhue,hsv3[1],hsv3[2])
    rgb4 = colorsys.hsv_to_rgb(newhue,hsv4[1],hsv4[2])
    print(hsv1, hsv2, hsv3, hsv4)
    return rgb1, rgb2, rgb3, rgb4

def grayscale():
    for w in range(width):
        for h in range(height):
            hsv1 = colorsys.rgb_to_hsv(pix[w,h][0], pix[w,h][1], pix[w,h][2])
            rgb1 = colorsys.hsv_to_rgb(0,0,hsv1[2])
            screen.set_at((w, h), rgb1)

# def save():
    

def compress(size, pixalated, round_value):
    hues = []
    values = []
    blurImage = im.filter(ImageFilter.BoxBlur(size))
    blurpix = blurImage.load()
    for w in range(width):
        for h in range(height):
            temp_w = w
            temp_h = h
            temp_w -= w % size
            temp_h -= h % size
            temp_w %= width
            temp_h %= height
            if w % size == 0 and h % size == 0:
                hues.append(blurpix[w,h])

    f = open('bytes.txt','wb')
    pix_bytes = bytearray(0)
    for w in range(width):
        for h in range(height):
            temp_w = w
            temp_h = h
            temp_w -= w % pixalated
            temp_h -= h % pixalated
            temp_w %= width
            temp_h %= height
            hsv1 = colorsys.rgb_to_hsv(pix[temp_w,temp_h][0], pix[temp_w,temp_h][1], pix[temp_w,temp_h][2])
            blurhsv = colorsys.rgb_to_hsv(blurpix[w,h][0], blurpix[w,h][1], blurpix[w,h][2])
            rgb1 = colorsys.hsv_to_rgb(round(blurhsv[0], round_value), round(blurhsv[1], round_value), round(hsv1[2], round_value))
            if round_value >= 0:
                r = round(rgb1[0], round_value)
                g = round(rgb1[1], round_value)
                b = round(rgb1[2], round_value)
            else:
                r = (round(rgb1[0]/(-10*round_value))*10)%255
                g = (round(rgb1[1]/(-10*round_value))*10)%255
                b = (round(rgb1[2]/(-10*round_value))*10)%255
            rgb1 = (r,g,b)
            if not w % width:
                print(r)
            if w % pixalated == 0 and h % pixalated == 0:
                values.append(round(hsv1[2], round_value))
            # hues.append((round(blurhsv[0], round_value), round(blurhsv[1], round_value)))
            # pix_byte = hsv1[2].to_bytes(2, byteorder='little')
            pix_bytes.append(hsv1[2])
            # pix_bytes = zlib.compress(pix_bytes)
            # print(pix_bytes)
            # print(int.from_bytes(pix_bytes, 'little'))
            screen.set_at((w, h), rgb1)
    print(len(hues))
    print(len(values))
    f.write(zlib.compress(pix_bytes))
    # f.write(pix_bytes)
    f.close()

# i = 0
# for pixel in get_2x2(0):
#     print(pixel)
#     rect = pygame.Rect((i*30,0), (30,40))
#     pygame.draw.rect(screen, pixel, rect)
#     i += 1
# i = 0
# for pixel in avg_2x2(0):
#     rect = pygame.Rect((i*30,40), (30,40))
#     pygame.draw.rect(screen, pixel, rect)
#     i += 1


size = 1
pixalated = 1
round_value = 5
compress(size, pixalated, round_value)
print(size)
pygame.display.flip()

prev_blur = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 4:
                size += 10
                compress(size, pixalated, round_value)
                print(size)
                pygame.display.flip()
            if event.button == 5:
                size -= 10
                if size <0:
                    size = 0
                compress(size, pixalated, round_value)
                print(size)
                pygame.display.flip()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pixalated += 1
                compress(size, pixalated, round_value)
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                if pixalated > 1:
                    pixalated -= 1
                    compress(size, pixalated, round_value)
                    pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                compress(size, pixalated, round_value)
                print(f'Round Value: {round_value}')
                round_value -= 1
            if event.key == pygame.K_LEFT:
                compress(size, pixalated, round_value)
                round_value += 1
    mainclock.tick(60)
