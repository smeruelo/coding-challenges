# Vowels

Este problema tienes que ayudar a Marta a encontrar la secuencia mágica más larga de un string.
Pero… ¿qué es una secuencia mágica? Definimos una secuencia mágica como una secuencia de letras
dentro de un string que contiene las cinco vocales en orden: a, e, i, o, u.
Puede haber cualquier cantidad de ocurrencias de cada vocal, pero deben estar presentes todas
las vocales y en orden alfabético (a,e,i,o,u). Por ejemplo, `aeeiooou` es una secuencia mágica,
pero `aeaiuoa` no lo es. A pesar de que tengamos otras letras por en medio, nosotros únicamente
nos fijaremos en las vocales para hacer la secuencia mágica más larga posible.
A continuación varios ejemplos:

* En la secuencia `aeeiou` la longitud de la secuencia mágica es de 6.
* En la secuencia `aeaioua` la longitud de la secuencia mágica es de 5.
* En la secuencia `aeiaaioooaau` la longitud de la secuencia mágica es de 8.

Marta tendrá un string, `s`, que estará formado por las letras: a, e, i, o, y u.
¿Le ayudas a encontrar la longitud de la secuencia mágica más larga en su string?


## Descripción de la función

Completa la función `longitudSecuenciaMagica` en el editor de código disponible a continuación.
La función deberá devolver un número entero indicando la longitud de la secuencia mágica más larga
dentro del string proporcionado. Si no hay ninguna secuencia mágica, devolverá 0.

`longitudSecuenciaMagica` tiene los siguientes parámetros:

* `s`:  el string que debe analizar


# Restricciones

* 5 < |s| < 5 × 105
* El string s estará compuesto por vocales (a, e, i, o, y u).