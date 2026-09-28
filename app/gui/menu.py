#=============================
# GUI/MENU
#=============================
# Esta dibuja un botón por cada juego
#! Necesario de decorar en un futuro

import pygame

from app import config

_fuente = None  # se crea la primera vez que hace falta, ver más abajo

# Cada entrada: texto del botón → (estado al que salta, (x, y, ancho, alto))
_botones = {
    "Ruleta": ("ruleta", (100, 200, 220, 60)),
    "Carrera de caballos": ("caballos", (100, 300, 320, 60)),
    "Blackjack": ("blackjack", (100, 400, 220, 60)),
}


def actualizar(ventana, eventos):
    global _fuente

    # pygame.font solo se puede usar despues de pygame.init(), asi q la
    # fuente se crea la primera vez que se llama a esta función, no al
    # importar el archivo.
    if _fuente is None:
        _fuente = pygame.font.SysFont(None, 36)

    siguiente_estado = "menu"  # por defecto nos quedamos en el menú

    for texto, (destino, (x, y, w, h)) in _botones.items():
        rect = pygame.Rect(x, y, w, h)

        # Dibujar el botón (rectángulo + texto encima)
        pygame.draw.rect(ventana, config.COLOR_BOTON, rect, border_radius=8)
        etiqueta = _fuente.render(texto, True, config.COLOR_TEXTO)
        ventana.blit(etiqueta, (x + 15, y + 15))

        # Comprobar si el jugador ha hecho click dentro de este botón
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(evento.pos):
                siguiente_estado = destino

    return siguiente_estado