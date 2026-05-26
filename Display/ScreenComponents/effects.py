from pygame import transform

class Effects:
    @staticmethod
    def blur_surface(surface, amount=8):
        w, h = surface.get_size()

        small = transform.smoothscale(surface,(max(1, w // amount), max(1, h // amount)))

        return transform.smoothscale(small,(w, h))