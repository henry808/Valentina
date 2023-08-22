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
for i in range(100):
    start_x = random.randint(0, width)
    start_y = random.randint(0, height)
    end_x = start_x + random.randint(-100, 100)
    end_y = start_y + random.randint(-100, 100)
    line_color = (random.randint(50, 255), random.randint(0, 100), random.randint(100, 255))
    draw.line([(start_x, start_y), (end_x, end_y)], fill=line_color, width=2)

# Faces emerging from the web
for i in range(10):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    size = random.randint(20, 50)
    opacity = random.randint(50, 200)
    face_color = (random.randint(150, 255), opacity, opacity)
    draw.ellipse([(x, y), (x + size, y + size)], fill=face_color)
    
    # Eyes and mouth, echoing the ambiguity of recognition
    eye_size = size // 5
    draw.ellipse([(x + eye_size, y + eye_size), (x + 2*eye_size, y + 2*eye_size)], fill=(0, 0, 0))
    draw.ellipse([(x + 3*eye_size, y + eye_size), (x + 4*eye_size, y + 2*eye_size)], fill=(0, 0, 0))
    draw.arc([(x + eye_size, y + 3*eye_size), (x + 4*eye_size, y + 4*eye_size)], 0, 180, fill=(0, 0, 0))

# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"WebsOfDeception_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
