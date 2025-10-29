# EJERCICIO 2: El Gatito de los Tres Pasos (Longitud Múltiplo de 3)


afd_gatito = {
    'estado': {'q0', 'q1', 'q2'},
    'alfabeto': {'0', '1'},
    'transicion': {
        # Desde q0 (longitud % 3 == 0), al leer un símbolo, la nueva longitud % 3 será 1.
        'q0': {'0': 'q1', '1': 'q1'},
        # Desde q1 (longitud % 3 == 1), al leer un símbolo, la nueva longitud % 3 será 2.
        'q1': {'0': 'q2', '1': 'q2'},
        # Desde q2 (longitud % 3 == 2), al leer un símbolo, la nueva longitud % 3 será 0.
        'q2': {'0': 'q0', '1': 'q0'}
    },
    'estado_inicial': 'q0',
    'estados_finales': {'q0'}
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
cadena = "101101" # Longitud 6, múltiplo de 3. Debería ser aceptada.
print(f"Analizando la cadena: {cadena}")
resultado = foo(afd_gatito, cadena)
print(f"¿se acepto? {resultado}")