from PIL import Image, ImageDraw
import random
import os
from datetime import datetime

# Dimensions
width, height = 800, 800

# Create blank canvas
canvas = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(canvas)

# Gradient sky from black to blood red
for j in range(height // 2):
    r = int(139 * (j / (height // 2)))
    draw.line([(0, j), (width, j)], fill=(r, 0, 0))

# Cold gray desert
for j in range(height // 2, height):
    draw.line([(0, j), (width, j)], fill=(169, 169, 169))

# Creeping shadows
for i in range(width):
    length = random.randint(0, height // 6)
    start = height - length
    draw.line([(i, start), (i, height)], fill=(0, 0, 139))

# Lone twisted silver tree
trunk_start = (width // 2 - 10, height // 2 + 50)
trunk_end = (width // 2 + 10, height // 2 + 150)
draw.rectangle([trunk_start, trunk_end], fill=(192, 192, 192))

branches = [
    ((width // 2, height // 2 + 100), (width // 2 - 50, height // 2 + 50)),
    ((width // 2, height // 2 + 100), (width // 2 + 50, height // 2 + 50)),
    ((width // 2, height // 2 + 80), (width // 2 - 70, height // 2 + 20)),
    ((width // 2, height // 2 + 80), (width // 2 + 70, height // 2 + 20))
]
for branch in branches:
    draw.line(branch, fill=(192, 192, 192), width=5)

# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"DestinysDesolation_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
