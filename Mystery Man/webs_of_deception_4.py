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



# Further haunting faces emerging from the shadows
for i in range(10):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    size = random.randint(60, 100)  # Size for prominence
    opacity = random.randint(50, 200)
    face_color = (random.randint(150, 255), opacity, opacity)
    
    # Border around the face
    border_thickness = random.randint(3, 6)
    draw.ellipse([(x-border_thickness, y-border_thickness), 
                  (x + size + border_thickness, y + size + border_thickness)], outline=(0, 0, 0), width=border_thickness)
    
    draw.ellipse([(x, y), (x + size, y + size)], fill=face_color)
    
    # Distorted eyes
    eye_size_left = random.randint(size // 10, size // 6)
    eye_size_right = random.randint(size // 10, size // 6)
    draw.ellipse([(x + size//4 - eye_size_left, y + size//4 - eye_size_left), 
                  (x + size//4 + eye_size_left, y + size//4 + eye_size_left)], fill=(0, 0, 0))
    draw.ellipse([(x + 3*size//4 - eye_size_right, y + size//4 - eye_size_right), 
                  (x + 3*size//4 + eye_size_right, y + size//4 + eye_size_right)], fill=(0, 0, 0))
    
    # Mouth, now more ambiguous, neither a smile nor a frown
    mouth_start = (x + size//4, y + 2*size//3)
    mouth_end = (x + 3*size//4, y + 2*size//3)
    mouth_curve = random.randint(-10, 10)  # Slight curve
    draw.arc([mouth_start, mouth_end], mouth_curve, 180 + mouth_curve, fill=(0, 0, 0), width=2)


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


# Save with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
path = os.path.join("C:\\Users\\hgran\\Downloads", f"WebsOfDeception_{timestamp}.png")
canvas.save(path)

print(f"Art saved as {path}")
