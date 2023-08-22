from PIL import Image, ImageDraw
import random
import os
from datetime import datetime

# Dimensions
width, height = 800, 800

# Create blank canvas
canvas = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(canvas)

# Background - abyss of nothingness
draw.rectangle([(0, 0), (width, height)], fill=(0, 0, 0))

# Weaving patterns representing the interconnectedness of life
points = [(random.randint(0, width), random.randint(0, height)) for _ in range(30)]
for start_point in points:
    for end_point in points:
        if start_point != end_point:
            chance = random.random()
            # Only draw 10% of the possible lines to keep it from being too dense
            if chance > 0.9:
                line_color = (random.randint(50, 255), random.randint(0, 100), random.randint(100, 255))
                draw.line([start_point, end_point], fill=line_color, width=2)


# Faces emerging from the web, enhanced for a more haunting ambiance
for i in range(10):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    size = random.randint(60, 100)  # Increased size for more prominence
    opacity = random.randint(50, 200)
    face_color = (random.randint(150, 255), opacity, opacity)
    draw.ellipse([(x, y), (x + size, y + size)], fill=face_color)
    
    # Distorted eyes, uneven in size, echoing the ambiguity of recognition
    eye_size_left = random.randint(size // 8, size // 6)
    eye_size_right = random.randint(size // 8, size // 6)
    draw.ellipse([(x + size//4 - eye_size_left, y + size//4 - eye_size_left), (x + size//4 + eye_size_left, y + size//4 + eye_size_left)], fill=(0, 0, 0))
    draw.ellipse([(x + 3*size//4 - eye_size_right, y + size//4 - eye_size_right), (x + 3*size//4 + eye_size_right, y + size//4 + eye_size_right)], fill=(0, 0, 0))
    
    # Distorted mouth, stretched and misshapen, embodying a silent scream
    mouth_size = random.randint(size // 4, size // 3)
    draw.arc([(x + size//4, y + 2*size//3), (x + 3*size//4, y + 2*size//3 + mouth_size)], 0, 180, fill=(0, 0, 0), width=3)


# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"WebsOfDeception_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
