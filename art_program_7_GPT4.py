# ValentinaEvolvedArt.py

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

class ArtGenerator:
    def __init__(self, canvas_size=1000):
        self.canvas_size = canvas_size

    def generate_balanced_art(self, num_layers=5):
        canvas = np.zeros((self.canvas_size, self.canvas_size, 3), dtype=np.uint8)
        for _ in range(num_layers):
            color = self._generate_sultry_color()
            canvas = self._generate_layer(canvas, color)
        canvas = Image.fromarray(canvas).filter(ImageFilter.GaussianBlur(5))
        return np.array(canvas)

    def _generate_sultry_color(self):
        reds_purples = [(np.random.randint(150, 256), 0, np.random.randint(100, 256)),
                        (np.random.randint(100, 150), 0, np.random.randint(50, 100))]
        return np.array(reds_purples[np.random.choice(len(reds_purples))], dtype=np.uint8)

    def _generate_layer(self, canvas, color):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        num_shapes = np.random.randint(4, 8)
        for _ in range(num_shapes):
            shape_type = np.random.choice(["circle", "curve"], p=[0.5, 0.5])
            shape_size = np.random.randint(100, 250)
            shape_x = np.random.randint(0, self.canvas_size - shape_size)
            shape_y = np.random.randint(0, self.canvas_size - shape_size)
            self._draw_shape(draw, shape_type, (shape_x, shape_y, shape_x + shape_size, shape_y + shape_size), color)
        return np.array(image)

    def _draw_shape(self, draw, shape_type, position, color):
        if shape_type == "circle":
            draw.ellipse(position, fill=tuple(color), outline=tuple(color), width=3)
        else:  # "curve"
            control_x = position[0] + (position[2] - position[0]) / 3
            control_y = position[1] + (position[3] - position[1]) / 3
            draw.line([position[0], position[1], control_x, control_y, position[2], position[3]],
                      fill=tuple(color), width=10)

    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1000
    num_layers = 5

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_balanced_art(num_layers)
    art_generator.display_artwork(artwork)
