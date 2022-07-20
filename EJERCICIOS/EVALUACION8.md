# Práctica 8. (6 puntos)
## Ejercicio 1 (2 puntos)
Escribe un programa python que pida un número por teclado y que cree un
diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los
valores sean los cuadrados de las claves.

Ejemplo: si se ingresa el 4 imprima el cuadrado de 1, de 2, de 3 y de 4





## Ejercicio 2 (2 puntos)
Escribe un programa que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de cada carácter en la cadena.

Ejemplo: si se ingresa "paloma" p=1 a=2 l=1 o=1 m=1

```
diccionario = {}
cadena = input("Ingrese una cadena: ")
for palabra in cadena:
	if palabra in diccionario:
		diccionario[palabra]=1
	else:
		diccionario[palabra]=1	
for letra,valor in diccionario.items():
	print (f'{letra}= {valor}')

```

## Ejercicio 3 (2 puntos)
Vamos a crear un programa en python donde vamos a declarar un diccionario para
guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta
y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de
los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras
cada consulta el programa nos preguntará si queremos hacer otra consulta.

```
precios = {"fresa": 39.50, "pera": 25, "manzana": 17.20, "piña": 30,"melon":13.99,"uva":36}
while True:
    fruta = input("Ingrese la fruta")
    if fruta not in precios:
        print("Fruta no existe.")
    else:
        kilo = int(input("Ingrese los kilos de la fruta"))
        print("El precio es de %.2f" % (kilo * precios[fruta]))
    frutaDos = input("Desea agregar otra fruta(s/n)")
    while frutaDos.lower() != "s" and frutaDos.lower() != "n":
        frutaDos = input("Desea agregar otra fruta (s/n)")
    if frutaDos.lower() == "n":
        break

