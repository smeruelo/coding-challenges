# Icecreams

A Lorena le encanta ir a comprar helados a la tienda que tiene junto a su casa.
Este mes hay una promoción en la que regalan un helado gratis al entregar envoltorios de
compras anteriores. En esta prueba tendrás que calcular la cantidad máxima de helados
que Lorena puede disfrutar.

Lorena comienza con un presupuesto de n euros. Cada helado cuesta c euros.
La promoción proporciona 1 helado gratis por cada m envoltorios recogidos.

Por ejemplo, Lorena comienza con n = 4 euros para comprar helados al precio de c = 1 euros cada uno.
La cantidad de envoltorios necesarios para obtener un helado gratis es m = 2.
Ella compra 4 helados, entrega esos 4 envoltorios para recibir 2 helados más.
Después entrega esos 2 envoltorios para recibir otro helado.
En este punto ya no puede adquirir más helados, ya que solo tiene un envoltorio,
pero ha disfrutado de 7 helados.


## Descripción de la función

Completa la función `numeroHelados` en el editor de código disponible a continuación.
Para cada caso, la función debe imprimir en una nueva línea un número entero que indique
el máximo de helados que Lorena puede comer.

`numeroHelados` tiene los siguientes parámetros:

* `n`:  un número entero (integer), el dinero que dispone inicialmente Lorena.
* `c`:  un número entero (integer), el precio de un helado.
* `m`:  un número entero (integer), el número de envoltorios necesarios para obtener otro helado gratis.


## Restricciones

* 1 ≤ t ≤ 103
* 2 ≤ n ≤ 105
* 1 ≤ c ≤ n
* 2 ≤ m ≤ n
