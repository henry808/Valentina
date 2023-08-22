# ValentinaBalancedArt.py

import numpy as np
from PIL import Image, ImageDraw

class ArtGenerator:
    def __init__(self, canvas_size=1000):
        self.canvas_size = canvas_size

    def generate_balanced_art(self, num_layers=4):
        canvas = np.zeros((self.canvas_size, self.canvas_size, 3), dtype=np.uint8)
        for _ in range(num_layers):
            color = self._generate_random_color()
            canvas = self._generate_layer(canvas, color)
        return canvas

    def _generate_random_color(self):
        return np.random.randint(100, 256, size=3, dtype=np.uint8)

    def _generate_layer(self, canvas, color):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        num_shapes = np.random.randint(6, 14)
        for _ in range(num_shapes):
            shape_type = np.random.choice(["circle", "rectangle", "triangle"], p=[0.4, 0.4, 0.2])
            shape_size = np.random.randint(30, 150)
            shape_x = np.random.randint(0, self.canvas_size - shape_size)
            shape_y = np.random.randint(0, self.canvas_size - shape_size)
            self._draw_shape(draw, shape_type, (shape_x, shape_y, shape_x + shape_size, shape_y + shape_size), color)
        return np.array(image)

    def _draw_shape(self, draw, shape_type, position, color):
        if shape_type == "circle":
            draw.ellipse(position, fill=tuple(color))
        elif shape_type == "rectangle":
            draw.rectangle(position, fill=tuple(color))
        else:  # "triangle"
            shape_points = [(position[0] + position[2]) / 2, position[1], position[2], position[3], position[0], position[3]]
            draw.polygon(shape_points, fill=tuple(color))
            
    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1000
    num_layers = 5

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_balanced_art(num_layers)
    art_generator.display_artwork(artwork)
