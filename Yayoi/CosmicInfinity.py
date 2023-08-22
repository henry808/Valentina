from PIL import Image, ImageDraw, ImageFont
import random
import os
import time

# Create a blank canvas
width, height = 800, 800
canvas = Image.new('RGB', (width, height), (30, 20, 40))

draw = ImageDraw.Draw(canvas)

# Draw deep purple and blue background
for i in range(width):
    for j in range(height):
        r, g, b = canvas.getpixel((i, j))
        r += random.randint(5, 10)
        g += random.randint(0, 5)
        b += random.randint(10, 20)
        canvas.putpixel((i, j), (r, g, b))

# Draw scattered yellow dots
for _ in range(500):
    x, y = random.randint(0, width), random.randint(0, height)
    dot_radius = random.randint(1, 5)
    dot_color = (255, 255, random.randint(0, 100))
    draw.ellipse((x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius), fill=dot_color)

# Draw the golden infinity symbol at the center
font_path = r"C:\Windows\Fonts\GILLUBCD.TTF" # You'd need to specify path to a font on your machine
font_size = 200
font = ImageFont.truetype(font_path, font_size)
text_width, text_height = draw.textsize("∞", font=font)
draw.text(((width - text_width) / 2, (height - text_height) / 2), "∞", font=font, fill=(255, 223, 0))

# Save the image with a timestamp in the filename
timestamp = time.strftime("%Y%m%d%H%M%S")
filename = f"C:\\Users\\hgran\\Downloads\\CosmicInfinity_{timestamp}.png"
canvas.save(filename)



canvas.show()