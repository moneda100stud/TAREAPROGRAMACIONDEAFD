# TAREAPROGRAMACIONDEAFD
# Reporte de Implementación: Autómatas Finitos Deterministas
**Fecha:** 28/10/2025

## 1. Introducción

Este documento detalla el diseño y la implementación de cuatro Autómatas Finitos Deterministas (AFD) utilizando Python. El objetivo es demostrar cómo los modelos teóricos de computación pueden ser traducidos a código funcional para reconocer patrones específicos en cadenas de texto.

## 2. Estructura y Simulación en Python

Para todos los ejercicios, se utilizó una estructura de datos y una función de simulación comunes.

### Estructura del AFD

Cada autómata se representa mediante un diccionario de Python que contiene los 5 elementos formales de un AFD: estados, alfabeto, función de transición, estado inicial y estados finales.

```python
afd_generico = {
    'estado': {'q0', 'q1', ...},
    'alfabeto': {'a', 'b', ...},
    'transicion': {
        'q0': {'a': 'q1', 'b': 'q0'},
        ...
    },
    'estado_inicial': 'q0',
    'estados_finales': {'q1'}
}
```

### Función de Simulación `foo`

Una función genérica `foo` procesa una cadena de entrada (`palabra`) según las reglas de un autómata (`adf`) dado.

```python
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
        estado_actual= adf ['transicion'][estado_actual][simbolo]
    
    # Verifica si el estado final se encuentra dentro del conjunto de estados de aceptación.
    return estado_actual in adf['estados_finales'] 
```

---

## 3. Descripción de los Ejercicios

### Ejercicio 1: Perro Guardián (Contiene "01")

-   **Objetivo**: Aceptar cadenas que contengan la subcadena "01".
-   **Lógica**: El autómata busca la secuencia '0' seguida de '1'. Una vez encontrada, permanece en un estado de aceptación (`R`).
-   **Implementación**:
    ```python
    aaf={
        'estado': {'p','q','R'},
        'alfabeto' : { '0' , '1'},
        'transicion': { 
            'p' : {'0': 'q', '1': 'p'},
            'q' : {'0':'q','1' : 'R' },
            'R' : {'0' : 'R' , '1': 'R'} 
        },
        'estado_inicial' : 'p',
        'estados_finales': {'R'}
    }
    ```

### Ejercicio 2: El Gatito de los Tres Pasos (Longitud Múltiplo de 3)

-   **Objetivo**: Aceptar cadenas cuya longitud sea un múltiplo de 3.
-   **Lógica**: Utiliza tres estados para contar la longitud de la cadena módulo 3. El estado `q0` (resto 0) es el inicial y el de aceptación.
-   **Implementación**:
    ```python
    afd_gatito = {
        'estado': {'q0', 'q1', 'q2'},
        'alfabeto': {'0', '1'},
        'transicion': {
            'q0': {'0': 'q1', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q2'},
            'q2': {'0': 'q0', '1': 'q0'}
        },
        'estado_inicial': 'q0',
        'estados_finales': {'q0'}
    }
    ```

### Ejercicio 3: El Loro que Contaba 'a's Pares

-   **Objetivo**: Aceptar cadenas con un número par de símbolos 'a'.
-   **Lógica**: Alterna entre un estado `Qpar` y `Qimpar` cada vez que lee una 'a'. La lectura de cualquier otro símbolo no cambia el estado de paridad.
-   **Implementación**:
    ```python
    afd_loro = {
        'estado': {'Qpar', 'Qimpar'},
        'alfabeto': {'a', 'b'},
        'transicion': {
            'Qpar': {'a': 'Qimpar', 'b': 'Qpar'},
            'Qimpar': {'a': 'Qpar', 'b': 'Qimpar'}
        },
        'estado_inicial': 'Qpar',
        'estados_finales': {'Qpar'}
    }
    ```

### Ejercicio 4: El Conejo que Termina en 'bb'

-   **Objetivo**: Aceptar cadenas que terminan exactamente con el sufijo "bb".
-   **Lógica**: El autómata recuerda los dos últimos símbolos. `Q0` es el estado base, `Q1` recuerda que el último símbolo fue 'b', y `Q2` (aceptación) confirma que los dos últimos fueron "bb".
-   **Implementación**:
    ```python
    afd_conejo = {
        'estado': {'Q0', 'Q1', 'Q2'},
        'alfabeto': {'a', 'b'},
        'transicion': {
            'Q0': {'a': 'Q0', 'b': 'Q1'},
            'Q1': {'a': 'Q0', 'b': 'Q2'},
            'Q2': {'a': 'Q0', 'b': 'Q2'}
        },
        'estado_inicial': 'Q0',
        'estados_finales': {'Q2'}
    }
    ```

