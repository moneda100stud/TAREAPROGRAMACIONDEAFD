# EJERCICIO 3: El Loro que Contaba 'a's Pares (Número Par de 'a's)
# Este AFD debe rastrear la paridad del número de 'a's vistas hasta el momento.

afd_loro = {
    'estado': {'Qpar', 'Qimpar'},
    'alfabeto': {'a', 'b'},
    'transicion': {
        # Qpar: número par de 'a's.
        # Si leo 'a', el conteo se vuelve impar. Si leo 'b', se mantiene par.
        'Qpar': {'a': 'Qimpar', 'b': 'Qpar'},
        # Qimpar: número impar de 'a's.
        # Si leo 'a', el conteo se vuelve par. Si leo 'b', se mantiene impar.
        'Qimpar': {'a': 'Qpar', 'b': 'Qimpar'}
    },
    'estado_inicial': 'Qpar',
    'estados_finales': {'Qpar'}
}

def foo(adf, palabra):
    """
    Simula el comportamiento de un AFD con una cadena de entrada.
    """
    estado_actual = adf['estado_inicial']
    for simbolo in palabra:
        if simbolo not in adf['alfabeto']:
            print(f"ERROR, el símbolo {simbolo} no pertenece al alfabeto")
            return False
        
        estado_actual = adf['transicion'][estado_actual][simbolo]
        print(f"{simbolo}-> {estado_actual}")
        
    return estado_actual in adf['estados_finales']

# --- Pruebas ---
cadena = "ababa" # 3 'a's (impar). Debería ser rechazada.
print(f"Analizando la cadena: '{cadena}'")
resultado = foo(afd_loro, cadena)
print(f"¿se acepto? {resultado}")