🧮 Calculadora de Números Binarios
📌 Explicación de cómo funciona
🧩 1. Creación de la función

Primero se crea una función que recibe:

🔢 Un número

📊 Su base (por ejemplo: binario, decimal, hexadecimal)

La función se encargará de convertir el número a la base indicada.

Dentro de la función:

Se declara una variable llamada resultado, que almacenará el valor final.

También se utiliza una cadena de texto que servirá especialmente cuando el resultado sea en hexadecimal, ya que ahí se necesitan letras (A, B, C, D, E, F).

🔁 2. Uso del ciclo while

Después se utiliza un ciclo:

while numero > 0:

Este ciclo significa que:

👉 Mientras el número sea mayor que 0, el proceso se repetirá.

Dentro del while ocurre lo siguiente:

🟡 a) Se obtiene el residuo

Se obtiene el residuo de dividir el número entre la base.

Ese residuo es importante porque:

Es el dígito que formará parte del nuevo número convertido.

Pero sale en orden inverso (desacomodado).

🟢 b) Se acomoda el resultado

Como los residuos salen al revés, se usa la variable resultado para:

Ir agregando cada nuevo valor al inicio

Así el número queda en el orden correcto

🔵 c) Se actualiza el número

Al final del ciclo:

El número se divide entre la base.

Esto permite continuar el proceso con el nuevo valor.

El ciclo se repite hasta que el número llegue a 0.

🔚 3. Return y Print
🏁 return

Se usa para:

Devolver el resultado final ya convertido.

Es lo que regresa la función.

🖨 print

Se usa para:

Mostrar en pantalla el resultado final.

Recibe el valor que devuelve la función y lo imprime.

✅ Resumen General

El programa:

Crea una función para convertir un número.

Usa un while para dividir el número entre la base.

Guarda los residuos en orden correcto.

Devuelve el resultado final.

Lo muestra en pantalla con print