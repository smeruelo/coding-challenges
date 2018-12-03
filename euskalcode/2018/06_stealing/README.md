# Stealing

Mikel es el dueño de una tienda de venta de artículos de todo tipo.
Para llevar el control, tiene un catálogo de productos en forma de lista con el nombre y el precio
de cada artículo. En cada venta, sus empleados registran el nombre y el precio de venta de cada
artículo vendido. Mikel sospecha que uno de sus empleados, Ander, está modificando el precio
de venta de algunos de los artículos. En esta prueba tendrás que escribir un programa que encuentre
la cantidad de veces que Ander registró un precio de venta incorrecto.


## Descripción de la función

Completa la función `verificaArticulos` en el editor de código disponible a continuación.
La función debe devolver un número entero que indique el número de precios de venta
incorrectamente registrados por Ander.

`verificaArticulos` tiene los siguientes parámetros:

* `origItems[origItems[0],...origItems[n-1]]`:  un array de n strings, donde cada origItems[i]
es el nombre de un artículo.

* `origPrices[origPrices[0],...origPrices[n-1]]`:  un array de n números de punto flotante
(floating point numbers), donde cada origPrices[i] es el precio de origItems[i]

* `items[items[0],...items[m-1]]`:  un array de m strings que contienen el nombre de cada item[j]
vendido por Ander.

* `prices[prices[0],...prices[m-1]]`:  un array de m números de punto flotante
(floating point numbers), donde cada prices[j] es el precio de venta registrado por Ander para el items[j].


## Restricciones

* 1 ≤ n ≤ 105
* 1 ≤ m ≤ n
* 1.00 ≤ origPrices[i], prices[j] ≤ 100000.00, donde 0 ≤ i < n, y 0 ≤ j < m
