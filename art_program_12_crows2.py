# ValentinaCrowArtBright.py

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

class ArtGenerator:
    def __init__(self, canvas_size=1000):
        self.canvas_size = canvas_size
        self.crow_silhouette = Image.open("crow_silhouette.png").convert('RGBA')  # Assuming you have a crow silhouette PNG image

    def generate_mysterious_art(self, num_crows=50):
        canvas = self._generate_light_background()
        for _ in range(num_crows):
            canvas = self._add_crow(canvas)
        canvas = Image.fromarray(canvas).filter(ImageFilter.GaussianBlur(1))
        return np.array(canvas)

    def _generate_light_background(self):
        soft_palette = [(np.random.randint(180, 240), np.random.randint(180, 240), np.random.randint(180, 240)),    # soft grays
                        (np.random.randint(190, 240), np.random.randint(210, 240), np.random.randint(240, 255)),    # light blues
                        (np.random.randint(240, 255), np.random.randint(220, 235), np.random.randint(180, 200))]   # muted golds
        color = np.array(soft_palette[np.random.choice(len(soft_palette))], dtype=np.uint8)
        return np.full((self.canvas_size, self.canvas_size, 3), color, dtype=np.uint8)

    def _add_crow(self, canvas):
        image = Image.fromarray(canvas)
        crow_size = np.random.randint(20, 100)
        crow = self.crow_silhouette.resize((crow_size, int(crow_size * self.crow_silhouette.height / self.crow_silhouette.width)))
        if np.random.rand() > 0.5:
            crow = ImageOps.mirror(crow)
        position = (np.random.randint(0, self.canvas_size - crow.width), np.random.randint(0, self.canvas_size - crow.height))
        image.paste(crow, position, crow)
        return np.array(image)

    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1000
    num_crows = 60

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_mysterious_art(num_crows)
    art_generator.display_artwork(artwork)
