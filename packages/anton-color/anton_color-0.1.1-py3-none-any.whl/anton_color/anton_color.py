from .warna import warna

class Clr:
    @staticmethod
    def colorize(text, color):
        color_code = warna.get(color, "")
        reset_code = warna["reset"]
        return f"{color_code}{text}{reset_code}"

    # Membuat metode untuk setiap warna
    @classmethod
    def generate_methods(cls):
        for color_name in warna:
            setattr(cls, color_name, staticmethod(lambda text, color=color_name: cls.colorize(text, color)))

# Panggil method untuk membuat metode warna secara otomatis
Clr.generate_methods()