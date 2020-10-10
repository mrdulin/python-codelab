from PIL import Image


class Img:
    def __init__(self):
        self.image = '123'

    def close(self):
        Image.Image.close(self.image)
