# Shortest stick

En esta prueba recibirás una serie de números que representarán la longitud en centímetros
de una serie de palitos. Al comienzo de cada turno, debes contar la cantidad de palos que tienes.
A continuación, debes mirar la longitud del palito más corto y desechar cualquier palito de esa longitud.
Una vez hecho esto, deberás recortar esa misma longitud a cada uno de los palos.
Repetirás esta acción hasta que no queden palitos. La salida de tu programa devolverá un array
donde los elementos del array indican el número de palitos que tenías al comienzo de cada turno.

Por ejemplo, imagina que tenemos un array que representa las longitudes de cuatro palitos: `[1, 1, 2, 3]`.
Los dos primeros son los palos más cortos y tienen 1 centímetro de longitud. Deséchalos.
A continuación recorta 1 centímetro a los otros dos palitos.
Ahora te quedan dos palitos con una longitud de 1 y 2 centímetros, es decir, un array `[1, 2]`.
En este nuevo turno, el palito más corto es el de 1 centímetro.
Haz lo mismo otra vez (deshéchalo y recorta su longitud al palito restante)
y tendrás un palito de 1 centímetro de longitud `[1]`.
Para terminar tíralo y devuelve un array con la cantidad de palitos que tenías al comienzo de cada turno,
es decir: `[4, 2, 1]`.

| longitud | longitud corte | número de palitos |
| -------- | -------------- | ----------------- |
| 1 1 2 3  |        1       |         4         |
| _ _ 1 2  |        1       |         2         |
| _ _ _ 1  |        1       |         1         |
| _ _ _ _  |      DONE      |        DONE       |


## Descripción de la función

Completa la función `juegoPalitos` en el editor de código disponible a continuación.
La función deberá devolver un array de números enteros (integers) representando el número de palos
al comienzo de cada turno.

`juegoPalitos` tiene los siguientes parámentros:

* `lengths[lengths[0],...lengths[n-1]]`:  un array de integers representando
las longitudes de los palos al inicio del juego.


## Restricciones

* 1 ≤ n ≤ 103
* 1 ≤ lengths[i] ≤ 103, donde 0 ≤ i < n
