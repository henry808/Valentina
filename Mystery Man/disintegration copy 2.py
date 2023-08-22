from PIL import Image, ImageDraw
import random
import os
from datetime import datetime

# Dimensions
width, height = 800, 800

# Create blank canvas
canvas = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(canvas)

# Background - chaotic whirlwinds of color transitioning to black
for i in range(width):
    for j in range(height):
        color = (
            random.randint(0, 255) if j < height // 2 else 0,
            random.randint(0, 255) if j < height // 3 else 0,
            random.randint(0, 255) if j < height // 4 else 0
        )
        draw.point((i, j), fill=color)

# Floating mirror shards
for _ in range(50):
    x = random.randint(0, width - 50)
    y = random.randint(0, height - 50)
    vertices = [(x, y), (x + random.randint(-30, 30), y + random.randint(-30, 30)), (x + random.randint(-30, 30), y + random.randint(-30, 30))]
    draw.polygon(vertices, fill=(169, 169, 169), outline=(128, 128, 128))

# Ghostly silhouettes reaching out
for _ in range(15):
    x = random.randint(0, width - 30)
    y = random.randint(height // 2, height - 30)
    draw.ellipse([(x, y), (x + 30, y + 60)], fill=(105, 105, 105), outline=(0, 0, 0))

# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"Disintegration_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
