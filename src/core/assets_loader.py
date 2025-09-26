# Carregamento centralizado de fontes, imagens e sons. Fallback caso o recurso não exista.
import os
import pygame

ASSET_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Imagens
def load_image(name, fallback_color=(255, 0, 255), size=(64, 64)):
    # Carrega imagem de assets. Se não existir, retorna Surface colorida
    path = os.path.join(ASSET_DIR, "images", name)
    if os.path.exists(path):
        return pygame.image.load(path).convert_alpha()
    else:
        surf = pygame.Surface(size)
        surf.fill(fallback_color)
        return surf

# Fontes
def load_font(name="arial", size=24):
    # Carrega fonte do sistema ou fallback padrão
    try:
        return pygame.font.SysFont(name, size)
    except Exception:
        return pygame.font.Font(None, size)

# Sons
def load_sound(name):
    # Carrega som. Se não existir, retorna objeto 'dummy' que ignora play()
    path = os.path.join(ASSET_DIR, "sounds", name)
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    else:
        class DummySound:
            def play(self): pass
        return DummySound()