#=============================
# GUI/VENTANA
#=============================
# Aquí vive el bucle principal de pygame y la "máquina de estados" la cual dice q se esta mostrando

import pygame

from app import config, db
from app.gui import menu as pantalla_menu
from app.games import ruleta, caballos, blackjack


def iniciar():
    # Nos aseguramos de que la tabla de cuentas existe
    db.crear_tablas()

    pygame.init()
    ventana = pygame.display.set_mode((config.ANCHO, config.ALTO))
    pygame.display.set_caption(config.TITULO)
    reloj = pygame.time.Clock()  # controla los FPS, ver reloj.tick() más abajo

    estado = "menu"  # posibles valores: "menu", "ruleta", "caballos", "blackjack"
    corriendo = True

    while corriendo:
        # Leer eventos (clicks, teclas, cerrar ventana...) una vez por frame
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                corriendo = False

        # Limpiar la pantalla en cada frame antes de volver a dibujar
        ventana.fill(config.COLOR_FONDO)

        # Delegar el dibujo y la lógica a la pantalla activa.
        #    Cada rama de aquí abajo llama a la función actualizar() del
        #    módulo correspondiente y actualiza "estado" con lo que
        #    devuelva (para poder cambiar de pantalla).
        if estado == "menu":
            estado = pantalla_menu.actualizar(ventana, eventos)
        elif estado == "ruleta":
            estado = ruleta.actualizar(ventana, eventos)
        elif estado == "caballos":
            estado = caballos.actualizar(ventana, eventos)
        elif estado == "blackjack":
            estado = blackjack.actualizar(ventana, eventos)

        # Mostrar en pantalla todo lo dibujado en este frame
        pygame.display.flip()

        # Esperar lo necesario para no pasar de los FPS marcados en config.py
        reloj.tick(config.FPS)

    pygame.quit()