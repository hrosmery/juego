def cargarPanel(coordenada_personaje, personaje, movimientos):
    # Colores (ANSI)
    rosa_claro = "\033[38;5;213m"
    rosa_fuerte = "\033[38;5;199m"
    blanco = "\033[97m"
    reset = "\033[0m"
    
    fila, columna = coordenada_personaje
    
    print("\n" + rosa_fuerte + "═" * 42 + reset)
    print((rosa_claro + "  P A N E L   D E   C O N T R O L  ").center(42))
    print(rosa_fuerte + "═" * 42 + reset)
    
    print(f"{blanco}📍 Posición:{rosa_claro}   Fila {fila} | Columna {columna}{reset}")
    print(f"{blanco}🧍 Dirección:{rosa_claro}  {personaje.strip()}{reset}")
    print(f"{blanco}🔢 Movimientos:{rosa_claro} {movimientos}{reset}")
    
    print(rosa_fuerte + "═" * 42 + reset + "\n")

