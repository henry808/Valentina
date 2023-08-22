from PIL import Image, ImageDraw
import random
import os
from datetime import datetime

# Dimensions
width, height = 800, 800

# Create blank canvas
canvas = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(canvas)

# Chaotic half with blacks, greys, and bursts of red
for i in range(0, width // 2):
    for j in range(height):
        color = random.choice([(0, 0, 0), (50, 50, 50), (100, 100, 100), (150, 0, 0)])
        draw.point((i, j), fill=color)

# Structured half with golds and silvers
for i in range(width // 2, width):
    for j in range(height):
        color = random.choice([(255, 223, 0), (192, 192, 192), (218, 165, 32)])
        draw.point((i, j), fill=color)

# Drawing the coin at the center
coin_radius = 150
draw.ellipse((width // 2 - coin_radius, height // 2 - coin_radius, width // 2 + coin_radius, height // 2 + coin_radius), fill=(218, 165, 32))

# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"CoinTossOfDestiny_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
