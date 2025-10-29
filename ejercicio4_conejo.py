# EJERCICIO 4: El Conejo que Termina en 'bb' (Termina en "bb")


afd_conejo = {
    'estado': {'Q0', 'Q1', 'Q2'},
    'alfabeto': {'a', 'b'},
    'transicion': {
        # Q0: Estado inicial, no se ha visto 'b' al final o lo último fue 'a'.
        # Si leo 'a', sigo sin tener un sufijo 'b'.
        # Si leo 'b', ahora tengo un sufijo 'b'.
        'Q0': {'a': 'Q0', 'b': 'Q1'},
        # Q1: El último símbolo fue 'b'.
        # Si leo 'a', el sufijo 'b' se rompe.
        # Si leo 'b', ahora tengo el sufijo 'bb'.
        'Q1': {'a': 'Q0', 'b': 'Q2'},
        # Q2: El sufijo es 'bb' (estado de aceptación).
        # Si leo 'a', el sufijo 'bb' se rompe.
        # Si leo 'b', el nuevo sufijo sigue siendo 'bb' (los dos últimos).
        'Q2': {'a': 'Q0', 'b': 'Q2'}
    },
    'estado_inicial': 'Q0',
    'estados_finales': {'Q2'}
}

def foo(adf, palabra):
    """
    Simula el comportamiento de un AFD con una cadena de entrada.
    """
    estado_actual = adf['estado_inicial']
    for simbolo in palabra:
        estado_actual = adf['transicion'][estado_actual][simbolo]
        print(f"{simbolo}-> {estado_actual}")
    return estado_actual in adf['estados_finales']

#Pruebas 
cadena = "ababb" 
print(f"Analizando la cadena: '{cadena}'")
resultado = foo(afd_conejo, cadena)
print(f"¿se acepto? {resultado}")