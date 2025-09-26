from core.game_manager import GameState
from core import constants, assets_loader

class TitleScreen(GameState):
    def on_enter(self):
        self.font = assets_loader.load_font(constants.FONTS["title"], 48)
        self.text = self.font.render("Tela Inicial", True, constants.PALETTE["text"])

    def update(self, dt): pass

    def draw(self, surface):
        surface.fill(constants.PALETTE["background"])
        surface.blit(self.text, (100, 100))

class DummyScreen(GameState):
    def on_enter(self):
        self.font = assets_loader.load_font(constants.FONTS["ui"], 32)
        self.text = self.font.render("Outra Tela", True, constants.PALETTE["secondary"])

    def update(self, dt): pass

    def draw(self, surface):
        surface.fill(constants.PALETTE["background"])
        surface.blit(self.text, (100, 200))