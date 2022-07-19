## Práctica 2. 6 puntos
2 Práctica 2. Números enteros y reales.

Realiza los ejercicios de acuerdo a las indicaciones

2.1 Ejercicio 1 (1.5 puntos)

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius.


```gradosFarenheit=int(input('Ingrese los grados Farenheit'))
gradosCelsius= (gradosFarenheit -32 )/1.8
print(f'Los grados Celsius son :{gradosCelsius:.2f}')
```



2.2 Ejercicio 2 (1.5 puntos)

Dados dos números, mostrar la suma, resta, división y multiplicación de
ambos.


```num1=int (input('Ingrese el primer número'))
num2=int (input('ingrese el segundo número'))
sum = num1 + num2
res= num1 - num2
div= num1/ num2
mult= num1 * num2
print (f'Los números dados son: {num1} y {num2}\n El resultado de la suma de {num1} + {num2} es: {sum} \n El resultado de la resta de {num1} - {num2} es: {res}\n El resultado de la división de {num1} / {num2} es: {div}\n El resultado de la multiplicacion de {num1} * {num2} es: {mult}')
```

2.3 Ejercicio 3 (1.5 puntos)

Calcular el perímetro y área de un rectángulo dada su base y su altura.
Respuesta:

```baseRect=float(input("Ingrese la base del rectángulo:"))
alturaRect=float(input("ingrese la altura del rectángulo:"))
periRect=2*baseRect + alturaRect*2
areaRect= baseRect * alturaRect
print(f'El perímetro del rectángulo es:{periRect:.2f}\n El área del rectángulo es:{areaRect:.2f}')


