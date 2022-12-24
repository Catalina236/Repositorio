secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
num=int(input("Escribe un número, xd:"))
while num!=secret_number:
   print("¡Ja, ja! ¡Estás atrapado en un bucle, xdxdxdxddddddddddddddd!")
   num=int(input("Escribe un número, xd:"))
if num==secret_number:
    print("El número secreto es: ", secret_number)
    print("Felicidades, lograste salir de mi bucle, xdxdddd")