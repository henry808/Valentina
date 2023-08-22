# ValentinaCrowArt.py

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops

class ArtGenerator:
    def __init__(self, canvas_size=1000):
        self.canvas_size = canvas_size
        self.crow_silhouette = Image.open("crow_silhouette.png").convert('RGBA')  # Assuming you have a crow silhouette PNG image

    def generate_mysterious_art(self, num_layers=6):
        canvas = self._generate_dark_background()
        for _ in range(num_layers):
            color = self._generate_mystic_color()
            canvas = self._generate_layer(canvas, color)
        canvas = Image.fromarray(canvas).filter(ImageFilter.GaussianBlur(3))
        return np.array(canvas)

    def _generate_mystic_color(self):
        mystic_palette = [(np.random.randint(0, 50), np.random.randint(0, 50), np.random.randint(100, 150)),   # deep blues
                          (np.random.randint(0, 40), np.random.randint(0, 40), np.random.randint(0, 40)),       # blacks
                          (np.random.randint(180, 220), np.random.randint(180, 220), np.random.randint(180, 220))]  # silvers
        return np.array(mystic_palette[np.random.choice(len(mystic_palette))], dtype=np.uint8)

    def _generate_dark_background(self):
        dark_shades = np.random.randint(10, 70, size=(self.canvas_size, self.canvas_size, 3), dtype=np.uint8)
        return dark_shades

    def _generate_layer(self, canvas, color):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        num_shapes = np.random.randint(2, 6)
        for _ in range(num_shapes):
            shape_type = np.random.choice(["fog", "crow"], p=[0.6, 0.4])
            shape_size = np.random.randint(100, 500)
            shape_x = np.random.randint(0, self.canvas_size - shape_size)
            shape_y = np.random.randint(0, self.canvas_size - shape_size)
            self._draw_shape(draw, shape_type, (shape_x, shape_y, shape_x + shape_size, shape_y + shape_size), color, image)
        return np.array(image)

    def _draw_shape(self, draw, shape_type, position, color, base_image):
        if shape_type == "fog":
            for i in range(3):  # Multiple swirls for the foggy effect
                offset = i * 30
                draw.arc([position[0] + offset, position[1] + offset, position[2] - offset, position[3] - offset], 
                         start=np.random.randint(0, 360), end=np.random.randint(0, 360), fill=tuple(color), width=np.random.randint(10, 50))
        else:  # "crow"
            crow = self.crow_silhouette.resize((position[2]-position[0], position[3]-position[1]))
            base_image.paste(crow, (position[0], position[1]), crow)

    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1000
    num_layers = 5

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_mysterious_art(num_layers)
    art_generator.display_artwork(artwork)
