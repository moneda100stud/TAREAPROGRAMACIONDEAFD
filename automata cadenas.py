# automata cadenas de ejercio1_perro guardian 
aaf={
    'estado': {'p','q','R'},
    'alfabeto' : { '0' , '1'},
   'transicion': { 

    # p: Estado inicial. Aún no se ha visto el inicio de la subcadena '01'.
    #    - Si lee '1', permanece en 'p'.
    #    - Si lee '0', pasa a 'q', habiendo encontrado el posible inicio de '01'.
    'p' : {'0': 'q', '1': 'p'},

    # q: Se ha leído un '0'.
    #    - Si lee '0', permanece en 'q', esperando un '1'.
    #    - Si lee '1', pasa a 'R', completando la subcadena '01'.
    'q' : {'0':'q','1' : 'R' },

    # R: Estado de aceptación. La subcadena '01' ya ha sido encontrada.
    #    - Una vez en este estado, cualquier símbolo mantiene el estado de aceptación.
    'R' : {'0' : 'R' , '1': 'R'} 
   },

'estado_inicial' : 'p',
'estados_finales': {'R'}
}


# Define una función para simular el comportamiento de un AFD.
def foo (adf, palabra) :
    # Establece el estado de inicio según la definición del autómata.
    estado_actual = adf['estado_inicial']
    # Itera sobre cada símbolo (carácter) en la cadena de entrada.
    for simbolo in palabra : 
        # Comprueba si el símbolo actual es parte del alfabeto definido del autómata.
        if simbolo not in adf['alfabeto'] :
            print (f"ERROR, el símbolo {simbolo} no pertenece al alfabeto") 
            return False # Si el símbolo no es válido, detiene la simulación y rechaza la cadena.
        
        # Actualiza el estado actual buscando en la tabla de transición.
        # Usa el estado actual y el símbolo leído para encontrar el siguiente estado.
        estado_actual= adf ['transicion'][estado_actual][simbolo]
        # Imprime la transición realizada para seguir el proceso.
        print (f"{simbolo}-> {estado_actual}")
    
    # Una vez que se han procesado todos los símbolos, verifica si el estado final
    # se encuentra dentro del conjunto de estados de aceptación.
    return estado_actual in adf['estados_finales'] 


cadena="110100";
print(f"Analizando la cadena: {cadena}")
resultado=foo (aaf,cadena)
print( f"¿se acepto? {resultado}");
