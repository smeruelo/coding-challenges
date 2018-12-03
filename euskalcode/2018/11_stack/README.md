# Stack

Llevamos años viendo en asignaturas como "Fundamentos de la programación" los conceptos de pilas o stacks.
Sabías que tarde o temprano llegaría el día en el que tendrías que implementar una pila o stack que
llevase tu firma. Ese momento ha llegado. En este problema tendrás que implementar tu propia pila
que acepte los siguientes comandos y realice las operaciones asociadas a ellos:

* `push k`: Introduce el número entero (integer) k en la parte superior de la pila.
* `pop`: Extrae el elemento superior de la pila.
* `inc e k`: suma ‘k’ a cada uno de los últimos ‘e’ elementos de la de la pila.


## Function Description

Completa la función `miSuperPila` en el editor de código disponible a continuación.
La función debe crear una pila (stack) vacía y realizar cada una de las operaciones en orden.
Después de realizar cada operación, debe imprimir el valor del elemento superior de la pila
en una nueva línea. Si la pila está vacía, debe imprimir `EMPTY`.

`miSuperPila` tiene los siguientes parámetros

* `operations[operations[0],...operations[n-1]]`:  un array de strings


## Restricciones

* 1 ≤ n ≤ 2 × 105
* -109 ≤ k ≤ 109
* 1 ≤ e ≤ |S|, donde |S| es el tamaño de la pila a la hora de realizar la operación.
* Se garantiza que nunca haremos pop cuando la pila esté vacía.
