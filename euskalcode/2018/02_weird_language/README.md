# Weird language

Hace escasos días se ha descubierto una tribu con un idioma un tanto peculiar llamado tornike.
El idioma tornike emplea las mismas palabras que el inglés pero en un orden diferente.
Empecemos por lo básico. En este idioma, al igual que en el inglés,  se le llama oración o frase
a una cadena de palabras separadas por espacios (la primera palabra comienza con la primera letra
en mayúscula seguida de letras minúsculas) y termina finalmente con un punto, es decir,
que satisface la expresión regular `^[A-Z][a-z ]*\.$`.
Para traducir las oraciones del inglés al tornike tenemos que reorganizar las palabras de la oración
de manera que se cumplan las siguientes condiciones:

* Cada palabra está ordenada por longitud, ascendente.
Es decir, las palabra más corta de la frase será la primera y la más larga la última.
* Las palabras de igual longitud deben aparecer en el mismo orden que en la oración original.
* La oración reorganizada debe formatearse para satisfacer la expresión regular ^[A-Z][a-z ]*\.$

Por ejemplo, considera la frase `Cats and hats`. Primero, las palabras se ordenan por longitud,
manteniendo el orden original para las de igual longitud: `[and, cats, hats]`.
A la frase reorganizada tendremos que aplicarle el formato, obteniendo como resultado final: `And cats hats`.


## Descripción de la función

Completa la función `traducir` en el editor de código disponible a continuación.
La función debe devolver una frase formada correctamente en el idioma tornike.

`traducir` tiene los siguientes parámetros:

* `frase`:  un string representando una frase bien formada.


## Restricciones

* 2 ≤ | frase| < 105
