# Fundamentos de Python

## Control de flujo

En la sección anterior, exploramos conceptos fundamentales del lenguaje Python, como las variables, los tipos de datos y las operaciones básicas. Ahora profundizaremos en herramientas esenciales para el control del flujo de un programa: las estructuras condicionales y los ciclos.

## Estructuras condicionales

Las estructuras condicionales permiten tomar decisiones en función de ciertas condiciones. En Python, las estructuras condicionales más comunes son `if`, `else` y `elif`. A continuación se presentan algunos ejemplos prácticos:

```python
# Estructura if
x = 10

if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")
```

En este caso, se imprimirá `"x es mayor que 5"` porque la condición `x > 5` se evalúa como verdadera.

```python
# Estructura if-elif-else
x = 10

if x > 10:
    print("x es mayor que 10")
elif x == 10:
    print("x es igual a 10")
else:
    print("x es menor que 10")
```

Aquí se imprimirá `"x es igual a 10"` ya que la condición `x == 10` es verdadera. Esta estructura permite evaluar múltiples condiciones de forma secuencial.

## Ciclos

Los ciclos (o bucles) permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o al recorrer una secuencia. En Python, los ciclos más utilizados son `for` y `while`.

```python
# Ciclo for
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

    1
    2
    3
    4
    5

Este ciclo `for` recorre cada elemento de la lista numeros e imprime su valor uno por uno.

```python
# Ciclo while
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

    0
    1
    2
    3
    4

El ciclo `while` ejecuta el bloque de código mientras la condición contador < 5 sea verdadera. En cada iteración, se incrementa el valor de contador.

El uso adecuado de estructuras condicionales y ciclos permite construir programas que se adaptan dinámicamente a diferentes situaciones y repiten tareas.
