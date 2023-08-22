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
for _ in range(10):
    x = random.randint(0, width - 50)
    y = random.randint(height // 2, height - 50)

    # A tormented silhouette form with colors fading from red to ghostly gray
    gradient_color = (
        random.randint(100, 255),
        random.randint(0, 50),
        random.randint(0, 50)
    )
    draw.ellipse([(x, y), (x + 20, y + 40)], fill=gradient_color, outline=(0, 0, 0))

    # Creepy eyes
    eye_color = (random.randint(200, 255), 0, 0)
    draw.ellipse([(x + 5, y + 10), (x + 10, y + 15)], fill=eye_color)
    draw.ellipse([(x + 10, y + 10), (x + 15, y + 15)], fill=eye_color)

    # Dripping shadows beneath the eyes, a mark of their haunting existence
    for drop in range(3):
        start = y + 15 + drop * 5
        end = start + random.randint(5, 10)
        draw.line([(x + 7 + drop * 3, start), (x + 7 + drop * 3, end)], fill=(0, 0, 0), width=2)

    # Shimmering aura around them
    aura_color = (
        random.randint(150, 255),
        random.randint(150, 255),
        random.randint(150, 255)
    )
    draw.arc([(x-5, y-5), (x + 25, y + 45)], 0, 360, fill=aura_color)


# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"Disintegration_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
