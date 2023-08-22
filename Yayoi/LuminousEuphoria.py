from PIL import Image, ImageDraw
import random
import os
from datetime import datetime

# Dimensions
width, height = 800, 800

# Create blank canvas
canvas = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(canvas)

# Draw diagonal waves of colors
for i in range(0, width, 40):
    draw.line([(i, 0), (0, i)], fill=(255, 165, 0), width=20)  # orange
    draw.line([(i, height), (0, height - i)], fill=(0, 191, 255), width=20)  # deepskyblue
    draw.line([(width, i), (width - i, 0)], fill=(255, 165, 0), width=20)  # orange
    draw.line([(width - i, height), (width, height - i)], fill=(0, 191, 255), width=20)  # deepskyblue

# Draw floating orbs
for _ in range(100):
    x, y = random.randint(0, width), random.randint(0, height)
    orb_radius = random.randint(10, 30)
    orb_color = random.choice([(0, 255, 0), (255, 105, 180)])
    draw.ellipse((x - orb_radius, y - orb_radius, x + orb_radius, y + orb_radius), fill=orb_color)

# Draw the golden heart with purple and teal swirls
heart_size = 150
heart_img = Image.new('RGB', (heart_size, heart_size), (255, 223, 0))
heart_draw = ImageDraw.Draw(heart_img)
heart_draw.ellipse((0, 0, heart_size, heart_size), fill=(255, 223, 0))
canvas.paste(heart_img, (int(width / 2 - heart_size / 2), int(height / 2 - heart_size / 2)))

swirl_radius = 200
draw.arc((width / 2 - swirl_radius, height / 2 - swirl_radius, width / 2 + swirl_radius, height / 2 + swirl_radius),
         start=0, end=180, fill=(128, 0, 128), width=15)  # purple swirl
draw.arc((width / 2 - swirl_radius, height / 2 - swirl_radius, width / 2 + swirl_radius, height / 2 + swirl_radius),
         start=180, end=360, fill=(0, 128, 128), width=15)  # teal swirl

# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"LuminousEuphoria_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
