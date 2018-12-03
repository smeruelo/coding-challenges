# Winning pairs

En esta prueba recibiremos un array de números (de tipo integer) y un valor que será nuestro objetivo
(también de tipo integer). Tendréis que ser capaces de determinar el número parejas diferentes que
contiene el array que cumplen lo siguiente: sumando los dos números de la pareja el resultado es
el valor objetivo. Dos parejas (a, b) y (c, d) se consideran diferentes si y solo si los números que
componen la pareja no coinciden, es decir: `(1, 9)` y `(9, 1)` se consideran como una única pareja,
ya que están compuestas por los mismos números. Sin embargo, `(1 , 9)` y `(9, 2)` serían dos parejas distintas.

Por ejemplo, dado el array `[1, 2, 3, 6, 7, 8, 9, 1]`, y el valor objetivo de 10, las 7 parejas
`(1,9)`, `(2,8)`, `(3,7 )`, `(8, 2)`, `(9, 1)`, `(9, 1)` y `(1, 9)` cumplen la condición de sumar 10,
pero solamente hay tres parejas diferentes: `(1, 9)`, `(2, 8)` y `(3, 7)`.


## Descripción de la función

Completa la función `numeroDeParejas` en el editor de código disponible a continuación.
La función debe devolver un número entero que indicará la cantidad total de parejas distintas
que contiene el array las cuales logran el valor objetivo sumando sus elementos.

`numeroDeParejas` tiene los siguientes parámetros:

* `a[a[0],...a[n-1]]`: un array de integers que utilizaremos para formar parejas
* `k`: el valor objetivo que deben sumar las parejas


## Restricciones

* 1 ≤ n ≤ 5 × 105
* 0 ≤ a[i] ≤ 109
* 0 ≤ k ≤ 5 × 109
