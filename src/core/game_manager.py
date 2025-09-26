# Gerenciamento de telas e estados do jogo (Menu, Seleção, Gameplay etc)

class StateManager:
    def __init__(self):
        self._stack = []  # pilha de estados (último = ativo)

    def push(self, state):
        # Adiciona uma nova tela no topo da pilha
        self._stack.append(state)
        state.on_enter()

    def pop(self):
        # Remove a tela atual e retorna para a anterior
        if self._stack:
            state = self._stack.pop()
            state.on_exit()

    def switch_to(self, new_state):
        # Troca a tela atual por outra, sem limpar toda a pilha
        if self._stack:
            old = self._stack.pop()
            old.on_exit()
        self._stack.append(new_state)
        new_state.on_enter()

    def update(self, dt):
        # Atualiza apenas a tela ativa
        if self._stack:
            self._stack[-1].update(dt)

    def draw(self, surface):
        # Desenha apenas a tela ativa
        if self._stack:
            self._stack[-1].draw(surface)

# Classe base para estados (telas) -- em aberto para ser definida quando chamada
class GameState:
    def on_enter(self): pass
    def on_exit(self): pass
    def update(self, dt): pass
    def draw(self, surface): pass