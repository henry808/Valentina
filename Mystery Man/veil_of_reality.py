from PIL import Image, ImageDraw
import random
import os
from datetime import datetime

# Dimensions
width, height = 800, 800

# Create blank canvas
canvas = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(canvas)

# Mundane layer
for j in range(height // 4):
    color = random.choice([(255, 223, 0), (255, 165, 0), (238, 154, 0)])
    draw.line([(0, j), (width, j)], fill=color)

# Dream layer
for j in range(height // 4, height // 2):
    color = random.choice([(75, 0, 130), (138, 43, 226), (106, 90, 205)])
    draw.line([(0, j), (width, j)], fill=color)

# Subconscious layer with distorted faces
for j in range(height // 2, 3 * height // 4):
    color = random.choice([(139, 0, 0), (0, 0, 0)])
    draw.line([(0, j), (width, j)], fill=color)

    if j % 50 == 0:
        x = random.randint(0, width - 50)
        y = j
        draw.arc([(x, y), (x + 50, y + 50)], 0, 360, fill=(255, 255, 255))
        draw.point((x + 20, y + 20), fill=(0, 0, 0))
        draw.point((x + 30, y + 20), fill=(0, 0, 0))
        draw.arc([(x + 20, y + 30), (x + 30, y + 40)], 0, 180, fill=(0, 0, 0))

# Void layer
for j in range(3 * height // 4, height):
    draw.line([(0, j), (width, j)], fill=(0, 0, 0))

    if j % 30 == 0:
        x = random.randint(0, width - 30)
        y = j
        shape = random.choice(["ellipse", "rectangle", "polygon"])
        if shape == "ellipse":
            draw.ellipse([(x, y), (x + 30, y + 30)], outline=(255, 255, 255))
        elif shape == "rectangle":
            draw.rectangle([(x, y), (x + 30, y + 30)], outline=(255, 255, 255))
        else:
            draw.polygon([(x, y), (x + 15, y + 30), (x + 30, y)], outline=(255, 255, 255))

# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"VeilOfReality_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
