# Casino
---
## Explicación del PROYECTO
| Este programa es una imitación a un casino virtual el cual funciona con puntos no relaccionados al dinero real y cuentas, en este hasta la fecha de publicación → [27/9/26] solo constara con tres juegos: <br>
→ Ruleta: Apuesta a un numero o color con el cual podras aumentar los puntos obtenisdos o perderlos <br>
→ Caballos: Unos caballos los cuales harán una carrera, apostarás a un color y si gana te llevaras recompensas <br>
→ BlackJack: Juegas contra la máquina, en este, tendras que acercarte a 21 puntos sin pasarte con las cartas, si te pasas o estas mas lejos q la máquina pierdes <br>
 
---
## Trayectoria
| Este sera un proyecto para aprender SQLite y alguna interfaz grafica, tendra varios minijuegos los cuales poco a poco se iran comentando y actualizando [24/9/26] <br> <br>

| La interfaz será pygame con el objetivo de que sea interactuable y con movimientos de buena calidad, me pondre a avanzar en los objetivos principales [27/9/26] <br> <br>

---
| La estructura seguida en el proyecto seria: <br> <br>

casino/<br>
├── pyproject.toml<br>
├── uv.lock<br>
├── main.py<br>
└── app/<br>
    ├── __init__.py<br>
    ├── config.py<br>
    ├── db.py<br>
    ├── admin_tools.py<br>
    ├── assets/<br>
    ├── gui/<br>
    │   ├── __init__.py<br>
    │   ├── ventana.py<br>
    │   └── menu.py<br>
    └── games/<br>
        ├── __init__.py<br>
        ├── ruleta.py<br>
        ├── caballos.py<br>
        └── blackjack.py<br>