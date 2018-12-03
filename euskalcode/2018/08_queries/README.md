# Queries

En esta ocasión vamos a realizar consultas entre arrays.
Recibiremos dos arrays de números enteros positivos (integers), y para cada elemento del segundo array
tendremos que determinar la cantidad total de elementos del primer array que son menores o iguales
a ese elemento. El resultado de estos cálculos lo iremos almacenando en otro array.

Por ejemplo, si el primer array es `[1, 2, 3]` y el segundo es `[2, 4]`, entonces
hay 2 elementos en el primer array menores o iguales a 2.
Por otro lado, hay 3 elementos en el primer array que son menores o iguales a 4.
Por lo tanto, el array que almacenará nuestros cálculos sería el siguiente: `[2, 3]`.


## Descripción de la función

Tendrás que completar la función llamada `calcula` en el editor de código disponible a continuación.
La función debe devolver un array de `m` números enteros positivos.
Cada elemento de este array indicará el número de elementos del primer array que son menores
o iguales al elemento de esa posición del segundo array.

`calcula` tiene los siguientes parámetros:

* `nums[nums[0],...nums[n-1]]`:  el primer array de números enteros (integers) positivos.
* `maxes[maxes[0],...maxes[n-1]]`: el segundo array de números enteros (integers) positivos.


## Restricciones

* 2 ≤ n, m ≤ 105
* 1 ≤ nums[j] ≤ 109, donde  0 ≤ j < n.
* 1 ≤ maxes[i] ≤ 109, donde  0 ≤ i < m.