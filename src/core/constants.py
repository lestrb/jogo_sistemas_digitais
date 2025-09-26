# Define constantes globais de configuração do jogo.

# Resolução base do jogo (pode ser escalada depois)
RESOLUTION = (1280, 720)

# Paleta de cores 
PALETTE = {
    "background": (30, 30, 30),
    "primary": (52, 152, 219),   # Azul
    "secondary": (231, 76, 60),  # Vermelho
    "positive": (46, 204, 113),  # Verde (sucesso, progresso, destaques positivos)
    "error": (192, 57, 43),      # Vermelho escuro (erros, falhas)
    "warning": (241, 196, 15),   # Amarelo vibrante (avisos, atenção)
    "text": (236, 240, 241),     # Branco sujo
}

# Fontes principais (nomes genéricos do sistema ou caminhos em assets)
FONTS = {
    "title": "arialblack",
    "ui": "arial",
    "mono": "consolas" # Fonte monoespaçada para textos tipo código
}

# Grade lógica (alinhamento no gameplay)
GRID_SIZE = 64 # Tamanho de cada célula da grade em pixels