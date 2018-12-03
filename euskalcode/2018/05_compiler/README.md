# Compiler

Estas creando un compilador para un programa en C ++ y necesitas verificar que los paréntesis,
las llaves y los corchetes están equilibrados y correctamente ubicados.

Las llaves, los paréntesis o los corchetes de una línea de código se consideran equilibrados
si se cumplen los siguientes criterios:

* Todas las parejas de elementos deben estar bien cerradas.
Es decir, vienen en pares de la forma (), {} y [].
Por ejemplo, en el caso de los corchetes, el corchete izquierdo abre el par, y el derecho lo cierra.
* En el caso en el que haya varios anidados, es decir, unos dentro de otros,
los de dentro deben estar correctamente cerrados.

Al fin y al cabo no deja de ser como en los lenguajes de programación que conocemos.
Por ejemplo, `[{}]` es una agrupación válida pero `[}] {}` no lo es.


## Descripción de la función

Completa la función llamada `compila` en el editor de código disponible a continuación.
La función recibe como parámetro un array de strings llamado `values` que contiene
en cada posición un string que representa una línea de código.
Tu función deberá devolver un array de strings donde cada string en la posición i
indique si las llaves/corchetes/paréntesis values[i] están de forma correcta o no.
Será por lo tanto un array de valores "YES" y "NO".

`compila` tiene los siguientes parámetros:

* `values[values0,...valuesn-1]`:  un array de strings (líneas) a analizar.
Cada línea contiene solo los símbolos de apertura y cierre de paréntesis, corchetes y llaves.


## Restricciones

* 1 ≤ n ≤ 15
* 1 ≤ longitud de valuesi ≤ 100
* Se garantiza que cada valor de valuesi está formado únicamente por los símbolos (, ), {, }, [, y ].
